"""Three signals over an audit table, with thresholds and a precision estimate.

Run: python monitoring/signals.py --db starter.db

A signal is only useful with an alert volume. The `estimate_precision` helper makes the arithmetic explicit:
at a stated prevalence, precision = TP / (TP + FP).
"""

from __future__ import annotations

import argparse
import sqlite3
import time
from dataclasses import dataclass


@dataclass
class Signal:
    name: str
    value: float
    threshold: float
    window_seconds: int
    rationale: str


AUDIT_SCHEMA = """
CREATE TABLE IF NOT EXISTS audit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts REAL NOT NULL,
    key_id TEXT,
    tenant TEXT,
    action TEXT NOT NULL,
    decision TEXT NOT NULL,
    reason TEXT NOT NULL,
    latency_ms REAL NOT NULL,
    model_version TEXT
);
"""


def ensure_schema(conn: sqlite3.Connection) -> None:
    """Create the audit table if the file is empty, so the tool runs before the service has."""

    conn.executescript(AUDIT_SCHEMA)


def denial_rate(conn: sqlite3.Connection, window: int = 3600, threshold: float = 0.10) -> Signal:
    row = conn.execute(
        "SELECT SUM(CASE WHEN decision LIKE 'denied%' THEN 1 ELSE 0 END) AS denied, COUNT(*) AS total"
        " FROM audit WHERE ts >= ?",
        (time.time() - window,),
    ).fetchone()
    total = row["total"] or 0
    value = (row["denied"] or 0) / total if total else 0.0
    return Signal("denial_rate", round(value, 4), threshold, window,
                  "A rising denial rate is probing or a broken integration; both need a human.")


def per_key_rate(conn: sqlite3.Connection, window: int = 60, threshold: float = 30.0) -> Signal:
    row = conn.execute(
        "SELECT key_id, COUNT(*) AS n FROM audit WHERE ts >= ? GROUP BY key_id ORDER BY n DESC LIMIT 1",
        (time.time() - window,),
    ).fetchone()
    value = float(row["n"]) if row else 0.0
    return Signal("max_requests_per_key_per_minute", value, threshold, window,
                  "Extraction and scripted abuse look like a key that stopped behaving like a person.")


def error_rate(conn: sqlite3.Connection, window: int = 900, threshold: float = 0.05) -> Signal:
    row = conn.execute(
        "SELECT SUM(CASE WHEN latency_ms > 500 THEN 1 ELSE 0 END) AS slow, COUNT(*) AS total"
        " FROM audit WHERE ts >= ?",
        (time.time() - window,),
    ).fetchone()
    total = row["total"] or 0
    value = (row["slow"] or 0) / total if total else 0.0
    return Signal("slow_request_share", round(value, 4), threshold, window,
                  "A latency shift often accompanies a larger input, which may be an extraction probe.")


def estimate_precision(tpr: float, fpr: float, prevalence: float) -> float:
    """Precision at a given detection rate, false-positive rate and prevalence."""

    tp = tpr * prevalence
    fp = fpr * (1 - prevalence)
    return tp / (tp + fp) if (tp + fp) else 0.0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", default="starter.db")
    args = parser.parse_args()
    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    ensure_schema(conn)
    signals = [denial_rate(conn), per_key_rate(conn), error_rate(conn)]
    print(f"{'signal':38} {'value':>8} {'threshold':>10}  state")
    for signal in signals:
        state = "ALERT" if signal.value >= signal.threshold else "ok"
        print(f"{signal.name:38} {signal.value:>8} {signal.threshold:>10}  {state}")
        print(f"  {signal.rationale}")
    print(f"\nprecision at 0.1% prevalence, TPR 0.95, FPR 0.01: "
          f"{estimate_precision(0.95, 0.01, 0.001):.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
