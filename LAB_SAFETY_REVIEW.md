# Laboratory safety review

**All 32 laboratory briefs now carry five lab-specific sections.** They were written per lab, from that lab's own
dataset, software and outputs — not copied between briefs — and the technical teaching sections were left untouched.

## 1. What was added

Each `labs/student/Lxx/LAB.md` gained sections 18–22 after the existing Submission section:

| Section | What it must say | Standard applied |
|---|---|---|
| **18. Acceptable use** | What this lab may be run against, and that every other target is out of bounds | Names the lab's actual asset (a CSV, a bundle, a mock service), not "the sandbox" in the abstract |
| **19. Scope restrictions** | The specific techniques and targets that are off limits here | Different in every lab: a perturbation lab forbids live recognisers, a RAG lab forbids real documents, a recovery lab forbids rotating real credentials |
| **20. Data handling** | What the data is, why it is synthetic, how it must be kept | States the provenance of third-party digits, the sensitive-shaped columns in admissions, the instruction-bearing notes in referrals |
| **21. Cleanup** | The files and processes this lab creates and how to remove them | Names the exact artefact: a scratch directory, a poisoned checkpoint, a uvicorn process, a manifest |
| **22. Restoring your environment** | What was installed or started, and how to get back to clean | Distinguishes "nothing installed" from "delete `.venv-test`", "stop the server", "no listener left open" |

Every brief now has exactly 22 numbered sections (verified on all 32 files). The learning objectives, instructions,
expected results, hints and submissions are byte-identical to before this phase; only the appended sections are new,
and `git diff` on a brief shows additions at the end.

## 2. Per-lab targets and boundaries

The table records the acceptable target each section names and the boundary it draws, which is what a reviewer
should spot-check.

| Lab | Legitimate target | Explicitly out of scope |
|---|---|---|
| L01 | `referrals.csv` defect audit | A real referral export, live triage queue or clinical system, even read-only |
| L02 | `transactions.csv` synthetic baseline | Issuers, processors, production fraud models, real chargebacks |
| L03 | Scratch copy of `referrals.csv` | Editing the dataset itself; manifests for files you do not own |
| L04 | In-script principals and policy | Any cloud IAM service or reachable analytics platform |
| L05 | Field list and scenario only | Probing a hospital summariser; pasting employer diagrams |
| L06 | `referrals.csv` intake parser | Live feeds, inboxes, supplier file shares |
| L07 | Self-contained linkage on `patients.csv` | Joining to voter rolls, public directories or external data |
| L08 | Local digits classifier | Deployed recognisers, CAPTCHAs, scanners, uploading crafted images |
| L09 | Two models trained locally | Commercial prediction APIs; any hosted model |
| L10 | In-script copy of transactions | Shared datasets, colleagues' runs, production pipelines |
| L11 | Synthetic admissions model | Inserting triggers outside the folder; vendor models |
| L12 | Own classifier, declared budget | Raising epsilon; denial of service against an endpoint |
| L13 | Local digits training and certificate | Presenting the number as a product property; shared compute without a quota check |
| L14 | Synthetic member/non-member split | Real services or real people's data |
| L15 | Synthetic applicants only | Real applicants, faces, or models trained on people |
| L16 | In-process mock API | Commercial APIs; exceeding a vendor's terms |
| L17 | Synthetic referrals, local tokeniser | Employer documents, real patient notes, third-party prompts |
| L18 | In-script token distribution | Hosted models or paid APIs |
| L19 | Mock assistant with fake tool | Live chatbots, vendor products, colleagues' deployments |
| L20 | Template-generated prompts | Real jailbreak corpora; deploying the detector unmeasured |
| L21 | Synthetic 12-document index | Real documents, customer records, employer knowledge bases |
| L22 | In-script documents and tenants | Production retrieval services |
| L23 | Policy engine and mock executor | Real email, refund, payment or shell tools |
| L24 | Local bundles, data-only format | Pickle or `weights_only=False` from untrusted sources; installing the `example.invalid` requirement |
| L25 | Local digits fine-tune | Uploading poisoned artefacts; fine-tuning hosted models |
| L26 | In-process or `127.0.0.1` service | Binding to `0.0.0.0`, tunnels, reusing the demo key |
| L27 | Replay of `api_logs.csv` | Load-testing or abusing a real API |
| L28 | Synthetic assets from earlier labs | Third-party products, live tenants, systems outside the repository |
| L29 | Synthetic gateway log | Real gateway logs; attributing synthetic principals to people |
| L30 | Local bundle recovery rehearsal | Rotating credentials or restoring services on a real system |
| L31 | Synthetic admissions fairness metrics | Inferring protected attributes of real people; claims about a real admissions process |
| L32 | Gate over solutions' evidence values | Wiring the gate to a deploy pipeline; signing off a real system |

## 3. Safety posture after the change

The course teaches offensive technique deliberately, and the fencing is now explicit at three levels:

1. **Course level** — `docs/getting-started/academic-integrity.md` (rules on tools, testing, citation, data and
   disclosure) and `SECURITY.md`.
2. **Module level** — each module's *Security implications* and *Detection and mitigation* sections.
3. **Lab level** — the five new sections, written in each lab's own terms, with a pointer to the course rules.

Every demonstration remains confined to synthetic data, models trained inside the lab, or local mock services. No
brief authorises testing against a third-party system, and every one that could be misread says so in section 19.

## 4. Findings and residual risk

| Severity | Finding |
|---|---|
| Medium | **The new sections are unreviewed prose.** They were checked against each lab's dataset and software sections and against the actual artefacts in `labs/solutions/`, but no human has read them end to end. Read three or four before students do — L08, L21, L26 and L30 make the widest claims. |
| Low | **L26's demo API key** remains a fixture in the starter. Section 19 now says it must not be reused outside the lab, which is the correct treatment for a teaching fixture. |
| Low | **L24's `example.invalid` requirement** is a string, never installed. Section 19 says so explicitly, closing the gap where a student might `pip install` it by habit. |
| Info | Cleanup sections describe real artefacts (scratch directories, checkpoints, servers), but most solutions write nothing to disk. A student following them will find the environment already clean, which is the right outcome and not a defect. |
| Info | The five sections add roughly 120–160 words to each brief. Word counts are now 850–1,040; the 22-section template is documented in `CONTRIBUTING.md` §5 and `docs/labs/index.md`. |

No lab requires network access, credentials, a GPU or a paid service, before or after this change.
