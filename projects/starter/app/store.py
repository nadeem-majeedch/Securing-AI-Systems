"""SQLite storage: tenants, append-only audit, and quota counting over the audit table.

Keeping quota state in the audit table means there is one source of truth: if a request is counted for
quota it also appears in the audit, which is what an investigation needs.
"""

from __future__ import annotations

import sqlite3
import threading
import time
from pathlib import Path

# One connection is shared across FastAPI's worker threads, so access is serialised here rather than left to
# SQLite's default thread check. A production service would use a connection pool or a single writer thread.
_LOCK = threading.Lock()

SCHEMA = """
CREATE TABLE IF NOT EXISTS tenants (
    key_id       TEXT PRIMARY KEY,
    tenant       TEXT NOT NULL,
    cohort       TEXT NOT NULL,
    key_hash     TEXT NOT NULL,
    revoked      INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS audit (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    ts           REAL NOT NULL,
    key_id       TEXT,
    tenant       TEXT,
    action       TEXT NOT NULL,
    decision     TEXT NOT NULL,
    reason       TEXT NOT NULL,
    latency_ms   REAL NOT NULL,
    model_version TEXT
);
CREATE INDEX IF NOT EXISTS audit_key_ts ON audit (key_id, ts);
"""


def connect(db_path: str | Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path), timeout=5.0, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA busy_timeout=5000")
    conn.executescript(SCHEMA)
    return conn


def add_tenant(conn: sqlite3.Connection, key_id: str, tenant: str, cohort: str, key_hash: str) -> None:
    with _LOCK:
        conn.execute(
            "INSERT OR REPLACE INTO tenants (key_id, tenant, cohort, key_hash, revoked) VALUES (?,?,?,?,0)",
            (key_id, tenant, cohort, key_hash),
        )
        conn.commit()


def tenant_for(conn: sqlite3.Connection, key_id: str) -> sqlite3.Row | None:
    with _LOCK:
        return conn.execute(
            "SELECT key_id, tenant, cohort, key_hash, revoked FROM tenants WHERE key_id = ?", (key_id,)
        ).fetchone()


def record(
    conn: sqlite3.Connection,
    *,
    key_id: str | None,
    tenant: str | None,
    action: str,
    decision: str,
    reason: str,
    latency_ms: float,
    model_version: str | None = None,
) -> None:
    with _LOCK:
        conn.execute(
            "INSERT INTO audit (ts, key_id, tenant, action, decision, reason, latency_ms, model_version)"
            " VALUES (?,?,?,?,?,?,?,?)",
            (time.time(), key_id, tenant, action, decision, reason, latency_ms, model_version),
        )
        conn.commit()


def count_since(conn: sqlite3.Connection, key_id: str, seconds: float) -> int:
    cutoff = time.time() - seconds
    with _LOCK:
        row = conn.execute(
            "SELECT COUNT(*) AS n FROM audit WHERE key_id = ? AND ts >= ? AND decision != 'denied_auth'",
            (key_id, cutoff),
        ).fetchone()
    return int(row["n"])


def recent(conn: sqlite3.Connection, limit: int = 20) -> list[sqlite3.Row]:
    with _LOCK:
        return list(
            conn.execute(
                "SELECT ts, key_id, action, decision, reason, latency_ms FROM audit ORDER BY id DESC LIMIT ?",
                (limit,),
            )
        )
