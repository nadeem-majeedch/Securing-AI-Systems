"""L07 — De-identification and linkage risk (M05, Intermediate).

Goal: measure how identifiable a "de-identified" extract is, generalise and suppress until every group has at
least five members, then re-run the linkage attack to show the difference.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import pandas as pd

from labkit import check, load_csv, report

QUASI = ["age", "postcode", "gender"]


# === WORK STARTS HERE ===
# STEP 1: load the table and drop the direct identifiers.
df = load_csv("patients.csv")
print(f"patients: {len(df)} rows")
published = df.drop(columns=["name", "patient_id"]).copy()

# STEP 2: measure the k-anonymity of the exact quasi-identifiers.
def k_stats(frame, keys):
    sizes = frame.groupby(keys, dropna=False).size()
    return int(sizes.min()), float((sizes == 1).sum() / len(sizes)), sizes

min_k, share_unique, _ = k_stats(published, QUASI)
print(f"exact quasi-identifiers: min k={min_k}, share of groups with k=1: {share_unique:.3f}")
check(min_k == 1, "exact ages and postcodes should leave unique rows")

# STEP 3: link the published table back to the name list using only the quasi-identifiers.
def link(published_frame, names_frame, keys):
    candidates = names_frame[["name"] + keys].drop_duplicates()   # one row per key/name pair
    left = published_frame.reset_index().rename(columns={"index": "_row"})
    merged = left.merge(candidates, on=keys, how="left")
    per_row = merged.groupby("_row").name.nunique()
    return int((per_row > 0).sum()), int((per_row == 1).sum())


matched_rows, single_rows = link(published, df, QUASI)
print(f"linkage on exact keys: {matched_rows}/{len(published)} rows have a candidate name,"
      f" {single_rows} resolve to exactly one person")
check(single_rows > 0, "the linkage attack must succeed on the raw extract")

# STEP 4: generalise the age and suppress small groups.
def generalise(frame):
    out = frame.copy()
    out["age"] = (out["age"] // 10) * 10
    out["age_band"] = out["age"].astype(str) + "-" + (out["age"] + 9).astype(str)
    return out.drop(columns=["age"])

generalised = generalise(published)
keys_gen = ["age_band", "postcode", "gender"]
sizes = generalised.groupby(keys_gen).size()
keep = sizes[sizes >= 5].index
suppressed = generalised.set_index(keys_gen).loc[keep].reset_index()
print(f"after generalisation and suppression: {len(suppressed)} rows kept of {len(generalised)}")
print(f"minimum group size now: {suppressed.groupby(keys_gen).size().min()}")

# STEP 5: re-run linkage against the protected extract.
names_generalised = generalise(df)      # keep patient_id and name for linking, band the age
matched_after, single_after = link(suppressed, names_generalised, keys_gen)
report("linkage before and after", [
    {"stage": "exact quasi-identifiers", "rows": len(published), "rows_with_candidate": matched_rows,
     "rows_with_one_candidate": single_rows},
    {"stage": "generalised + suppressed (k>=5)", "rows": len(suppressed), "rows_with_candidate": matched_after,
     "rows_with_one_candidate": single_after},
])
check(single_after == 0, "no published row may resolve to a single person after suppression")
print("\nRe-identification stopped being a single join. It is still not impossible: it is expensive.")
