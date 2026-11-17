"""Secure-by-default inference service skeleton.

Controls present: API-key authentication, cohort authorisation derived from the key (never the body),
strict input validation, per-key quotas, an append-only audit of every decision, security headers, a
body-size limit and a kill switch.

Controls absent on purpose: threat model, measurement of any defence, multi-tenancy beyond a cohort
string, rotation, and a key-issuing endpoint. Those are the project.
"""

from __future__ import annotations

import os
import time
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from . import model, security, store

DB_PATH = Path(os.environ.get("SAS_DB", "starter.db"))
RPM = int(os.environ.get("SAS_RPM", "10"))
RPD = int(os.environ.get("SAS_RPD", "1000"))
MAX_BODY = 4096


class PredictRequest(BaseModel):
    cohort: str = Field(min_length=1, max_length=32)
    features: list[float] = Field(min_length=4, max_length=4)


def _enabled() -> bool:
    return os.environ.get("SAS_ENABLED", "1") != "0"


def create_app(db_path: str | Path | None = None) -> FastAPI:
    path = Path(db_path or DB_PATH)

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        conn = store.connect(path)
        for principal in security.demo_principals():
            store.add_tenant(conn, principal["key_id"], principal["tenant"], principal["cohort"],
                             principal["key_hash"])
        app.state.conn = conn
        yield
        conn.close()

    app = FastAPI(title="SAS starter service", version="0.1.0", lifespan=lifespan)

    @app.middleware("http")
    async def hardening(request: Request, call_next):
        length = request.headers.get("content-length")
        if length and length.isdigit() and int(length) > MAX_BODY:
            return JSONResponse({"detail": "request body too large"}, status_code=413)
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Cache-Control"] = "no-store"
        response.headers["Referrer-Policy"] = "no-referrer"
        return response

    def principal(x_api_key: str | None = Header(default=None, alias="X-API-Key")):
        conn = app.state.conn
        started = time.perf_counter()
        if not x_api_key:
            store.record(conn, key_id=None, tenant=None, action="predict", decision="denied_auth",
                         reason="missing_key", latency_ms=(time.perf_counter() - started) * 1000)
            raise HTTPException(status_code=401, detail="unauthorised")
        candidate_ids = [p["key_id"] for p in security.demo_principals()]
        for key_id in candidate_ids:
            row = store.tenant_for(conn, key_id)
            if row is None:
                continue
            if security.key_matches(x_api_key, row["key_hash"]):
                if row["revoked"]:
                    store.record(conn, key_id=key_id, tenant=row["tenant"], action="predict",
                                 decision="denied_auth", reason="revoked_key",
                                 latency_ms=(time.perf_counter() - started) * 1000)
                    raise HTTPException(status_code=401, detail="unauthorised")
                return {"key_id": key_id, "tenant": row["tenant"], "cohort": row["cohort"]}
        store.record(conn, key_id=None, tenant=None, action="predict", decision="denied_auth",
                     reason="unknown_key", latency_ms=(time.perf_counter() - started) * 1000)
        raise HTTPException(status_code=401, detail="unauthorised")

    @app.get("/health")
    def health():
        return {
            "status": "ok" if _enabled() else "disabled",
            "model_version": model.MODEL_VERSION,
            "predictions_enabled": _enabled(),
        }

    @app.post("/predict")
    def predict(body: PredictRequest, who: dict = Depends(principal)):
        conn = app.state.conn
        started = time.perf_counter()

        def deny(status: int, reason: str, detail: str):
            store.record(conn, key_id=who["key_id"], tenant=who["tenant"], action="predict",
                         decision="denied", reason=reason,
                         latency_ms=(time.perf_counter() - started) * 1000)
            raise HTTPException(status_code=status, detail=detail)

        if not _enabled():
            deny(503, "kill_switch", "predictions are disabled")

        if body.cohort != who["cohort"]:
            deny(403, "cohort_mismatch", "cohort does not match the key")

        for value in body.features:
            if not -10.0 <= value <= 10.0:
                deny(422, "feature_out_of_range", "feature outside permitted range")

        if store.count_since(conn, who["key_id"], 60) >= RPM:
            store.record(conn, key_id=who["key_id"], tenant=who["tenant"], action="predict",
                         decision="denied", reason="quota_minute",
                         latency_ms=(time.perf_counter() - started) * 1000)
            return JSONResponse({"detail": "quota exceeded"}, status_code=429,
                                headers={"Retry-After": "60"})
        if store.count_since(conn, who["key_id"], 86400) >= RPD:
            store.record(conn, key_id=who["key_id"], tenant=who["tenant"], action="predict",
                         decision="denied", reason="quota_day",
                         latency_ms=(time.perf_counter() - started) * 1000)
            return JSONResponse({"detail": "daily quota exceeded"}, status_code=429,
                                headers={"Retry-After": "3600"})

        result = model.predict(body.features)
        latency = (time.perf_counter() - started) * 1000
        store.record(conn, key_id=who["key_id"], tenant=who["tenant"], action="predict",
                     decision="allowed", reason="all_checks_passed", latency_ms=latency,
                     model_version=str(result["model_version"]))
        return {"score": result["score"], "band": result["band"], "model_version": result["model_version"]}

    @app.get("/audit/recent")
    def audit_recent(limit: int = 20, who: dict = Depends(principal)):
        rows = store.recent(app.state.conn, limit=min(limit, 200))
        return [dict(row) for row in rows]

    return app


app = create_app()
