"""L26 — An insecure prediction API and its hardened twin (M16, Beginner).

Goal: run two FastAPI apps through the same eight requests, show what the insecure one leaks, and require the
hardened one to answer with 401, 413 or 422 instead of 500.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

from fastapi import FastAPI, Header, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

from labkit import check, report

API_KEY = "demo-key"
MAX_TEXT = 200


# === WORK STARTS HERE ===
# STEP 1: the insecure app — accepts any JSON, no auth, echoes the exception.
insecure = FastAPI()


@insecure.post("/predict")
def predict_insecure(payload: dict):
    try:
        text = payload["text"]
        return {"label": "spam" if "free" in text.lower() else "ham", "length": len(text)}
    except Exception as exc:                                   # noqa: BLE001 - deliberately bad
        return {"error": str(exc), "type": type(exc).__name__}


# STEP 2: the hardened app — schema, bounds, auth, generic errors.
hardened = FastAPI()


class PredictRequest(BaseModel):
    text: str = Field(min_length=1, max_length=MAX_TEXT)


@hardened.post("/predict")
def predict_hardened(body: PredictRequest, x_api_key: str = Header(default="")):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="unauthorized")
    label = "spam" if "free" in body.text.lower() else "ham"
    return {"label": label, "length": len(body.text)}


clients = {"insecure": TestClient(insecure, raise_server_exceptions=False),
           "hardened": TestClient(hardened, raise_server_exceptions=False)}

# STEP 3: the same eight probes against both.
probes = [
    ("valid", {"text": "free money now"}, {"x-api-key": API_KEY}),
    ("no auth", {"text": "free money now"}, {}),
    ("missing field", {}, {"x-api-key": API_KEY}),
    ("wrong type", {"text": 12345}, {"x-api-key": API_KEY}),
    ("empty text", {"text": ""}, {"x-api-key": API_KEY}),
    ("oversized", {"text": "a" * 5000}, {"x-api-key": API_KEY}),
    ("extra field", {"text": "hello", "role": "admin"}, {"x-api-key": API_KEY}),
    ("nested junk", {"text": {"nested": ["object"]}}, {"x-api-key": API_KEY}),
]
rows = []
for name, body, headers in probes:
    row = {"probe": name}
    for which, client in clients.items():
        response = client.post("/predict", json=body, headers=headers)
        row[f"{which}_status"] = response.status_code
        row[f"{which}_leak"] = "error" in str(response.json()).lower() or response.status_code >= 500
    rows.append(row)
report("probe results", rows)

# STEP 4: the differences are the finding.
by_name = {row["probe"]: row for row in rows}
check(by_name["valid"]["hardened_status"] == 200, "a valid authenticated request must succeed")
check(by_name["no auth"]["insecure_status"] == 200, "the insecure app has no authentication")
check(by_name["no auth"]["hardened_status"] == 401, "the hardened app must reject unauthenticated calls")
check(by_name["missing field"]["hardened_status"] == 422, "schema violations must be 422, not 500")
check(by_name["wrong type"]["hardened_status"] == 422, "type errors must be rejected at the boundary")
check(by_name["oversized"]["hardened_status"] == 422, "oversized input must be rejected before the model")
check(by_name["missing field"]["insecure_status"] >= 500 or by_name["missing field"]["insecure_status"] == 200,
      "the insecure app returns a leaked exception instead of a validation error")

# STEP 5: the checklist behind the twin.
checklist = report("controls", [
    {"control": "authentication", "insecure": "none", "hardened": "API key, 401"},
    {"control": "schema validation", "insecure": "dict payload", "hardened": "Pydantic model, 422"},
    {"control": "input size limit", "insecure": "unbounded", "hardened": f"{MAX_TEXT} chars, 413/422"},
    {"control": "error detail", "insecure": "exception echoed", "hardened": "fixed message"},
])
print("\nEvery probe difference is a boundary that exists in one app and not the other.")
print("The model is identical in both; the security property comes from the interface around it.")
