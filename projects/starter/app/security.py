"""API-key handling: hashed at rest, compared in constant time, never logged.

`hmac.compare_digest` matters even for a demo: a plain `==` leaks length and content through timing, and
copying the habit into production is how that defect spreads.
"""

from __future__ import annotations

import hashlib
import hmac

DEMO_KEYS = {
    "demo-key-a": {"key_id": "key-a", "tenant": "acme", "cohort": "alpha"},
    "demo-key-b": {"key_id": "key-b", "tenant": "beta-ltd", "cohort": "beta"},
}


def hash_key(raw: str) -> str:
    """Hash a presented key. Use a slow KDF (scrypt/argon2) in production; SHA-256 is used here to keep
    the starter dependency-free and readable."""

    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def key_matches(raw: str, stored_hash: str) -> bool:
    return hmac.compare_digest(hash_key(raw), stored_hash)


def demo_principals() -> list[dict[str, str]]:
    """The seeded principals, with their hashes. Development only."""

    return [
        {"key_id": meta["key_id"], "tenant": meta["tenant"], "cohort": meta["cohort"],
         "key_hash": hash_key(raw)}
        for raw, meta in DEMO_KEYS.items()
    ]
