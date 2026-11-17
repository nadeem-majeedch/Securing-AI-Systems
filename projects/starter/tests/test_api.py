"""Deny-path tests. These are the evidence that the controls exist.

Delete any of these and you lose the ability to claim the corresponding control. Add to them; do not
replace them with tests of the happy path.
"""

from __future__ import annotations

import importlib

import pytest
from fastapi.testclient import TestClient

from app import main as main_module


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setenv("SAS_RPM", "3")
    monkeypatch.setenv("SAS_ENABLED", "1")
    importlib.reload(main_module)
    app = main_module.create_app(tmp_path / "test.db")
    with TestClient(app) as test_client:
        yield test_client


GOOD = {"cohort": "alpha", "features": [0.4, -1.2, 2.0, 0.1]}


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_missing_key_is_401(client):
    response = client.post("/predict", json=GOOD)
    assert response.status_code == 401
    assert response.json() == {"detail": "unauthorised"}


def test_unknown_key_is_401(client):
    response = client.post("/predict", json=GOOD, headers={"X-API-Key": "not-a-key"})
    assert response.status_code == 401


def test_valid_request_scores(client):
    response = client.post("/predict", json=GOOD, headers={"X-API-Key": "demo-key-a"})
    assert response.status_code == 200
    body = response.json()
    assert 0.0 <= body["score"] <= 1.0
    assert body["band"] in {"low", "medium", "high"}


def test_other_cohort_is_403(client):
    response = client.post("/predict", json={"cohort": "beta", "features": GOOD["features"]},
                           headers={"X-API-Key": "demo-key-a"})
    assert response.status_code == 403


def test_feature_out_of_range_is_422(client):
    response = client.post("/predict", json={"cohort": "alpha", "features": [0, 0, 0, 99]},
                           headers={"X-API-Key": "demo-key-a"})
    assert response.status_code == 422


def test_oversized_body_is_413(client):
    payload = {"cohort": "alpha", "features": [0, 0, 0, 0], "padding": "x" * 5000}
    response = client.post("/predict", json=payload, headers={"X-API-Key": "demo-key-a"})
    assert response.status_code == 413


def test_quota_is_enforced(client):
    headers = {"X-API-Key": "demo-key-a"}
    for _ in range(3):
        assert client.post("/predict", json=GOOD, headers=headers).status_code == 200
    response = client.post("/predict", json=GOOD, headers=headers)
    assert response.status_code == 429
    assert response.headers["Retry-After"] == "60"


def test_denial_is_audited(client):
    client.post("/predict", json={"cohort": "beta", "features": GOOD["features"]},
                headers={"X-API-Key": "demo-key-a"})
    rows = client.get("/audit/recent", headers={"X-API-Key": "demo-key-a"}).json()
    assert any(row["reason"] == "cohort_mismatch" and row["decision"] == "denied" for row in rows)


def test_kill_switch_keeps_health_alive(client, monkeypatch):
    monkeypatch.setenv("SAS_ENABLED", "0")
    response = client.post("/predict", json=GOOD, headers={"X-API-Key": "demo-key-a"})
    assert response.status_code == 503
    assert client.get("/health").json()["status"] == "disabled"


def test_security_headers_present(client):
    response = client.get("/health")
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["Cache-Control"] == "no-store"
