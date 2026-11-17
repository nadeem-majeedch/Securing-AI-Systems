# Laboratory index

32 laboratories across 20 modules. Beginner 9 · Intermediate 13 · Advanced 7 · Challenge 3.

Each lab has a student manual in `labs/student/<id>/LAB.md` and a separate solution in
`labs/solutions/<id>/`. Start with the prerequisites column: it names the earlier lab a lab depends on.

| Lab | Title | Module | Difficulty | Time (min) | Prerequisite |
|---|---|---|---|---|---|
| [L01](student/L01/LAB.md) | Auditing the security properties of a clinical triage assistant | M01 | Beginner | 45 | Module 01 lecture; no prior lab. |
| [L02](student/L02/LAB.md) | Baseline fraud model: metrics, calibration and confident errors | M02 | Beginner | 60 | Module 02 lecture; L01 recommended. |
| [L03](student/L03/LAB.md) | Dataset integrity: hash manifests, tamper detection and MACs | M03 | Beginner | 45 | Module 03 lecture; L01 recommended. |
| [L04](student/L04/LAB.md) | Least privilege for an analytics platform | M03 | Intermediate | 60 | Module 03 lecture; L03 recommended. |
| [L05](student/L05/LAB.md) | Threat modelling and risk ranking for a hospital summariser | M04 | Beginner | 50 | Module 04 lecture; L01 recommended. |
| [L06](student/L06/LAB.md) | Intake validation and quarantine for a dirty referral feed | M05 | Beginner | 50 | Module 05 lecture; L01 recommended. |
| [L07](student/L07/LAB.md) | De-identification and linkage risk in a patient extract | M05 | Intermediate | 70 | L06; Module 05 lecture. |
| [L08](student/L08/LAB.md) | Adversarial perturbations against a digit classifier | M06 | Intermediate | 80 | Module 06 lecture; L02 recommended. |
| [L09](student/L09/LAB.md) | Transfer attacks and the price of a black-box query | M06 | Advanced | 90 | L08 (FGSM on digits). |
| [L10](student/L10/LAB.md) | Poisoning a fraud model with flipped labels | M07 | Intermediate | 75 | L02 (baseline fraud model). |
| [L11](student/L11/LAB.md) | Finding a backdoor: data scan and ablation audit | M07 | Advanced | 80 | L10 (poisoning), L02 (evaluation). |
| [L12](student/L12/LAB.md) | PGD, projection and an honest robustness number | M08 | Advanced | 90 | L08 (FGSM), L09 recommended. |
| [L13](student/L13/LAB.md) | Two defences, two promises: adversarial training and a certificate | M08 | Challenge | 120 | L08, L12 (attacks and PGD). |
| [L14](student/L14/LAB.md) | Membership inference: measuring what a model remembers | M09 | Intermediate | 70 | L02 (evaluation), L15 recommended after this lab. |
| [L15](student/L15/LAB.md) | Attribute inference and model inversion on applicant data | M09 | Advanced | 80 | L14 (membership inference). |
| [L16](student/L16/LAB.md) | Extraction from a mock admissions API | M10 | Intermediate | 80 | L02 (evaluation), L10 recommended. |
| [L17](student/L17/LAB.md) | Tokens, context budget and the flat prompt | M11 | Beginner | 50 | Python basics; no ML required. |
| [L18](student/L18/LAB.md) | Decoding determinism and the replayable incident | M11 | Intermediate | 60 | L17 recommended. |
| [L19](student/L19/LAB.md) | Direct prompt injection against a mock assistant | M12 | Beginner | 55 | L17 recommended. |
| [L20](student/L20/LAB.md) | A jailbreak detector and the base-rate problem | M12 | Intermediate | 70 | L02 (evaluation), L19. |
| [L21](student/L21/LAB.md) | RAG retrieval that leaks one document | M13 | Intermediate | 70 | L16 recommended; basic TF-IDF. |
| [L22](student/L22/LAB.md) | An ACL test suite for a RAG index | M13 | Advanced | 80 | L21. |
| [L23](student/L23/LAB.md) | Authorising an AI agent's tool calls | M14 | Intermediate | 75 | L19, L21. |
| [L24](student/L24/LAB.md) | A malicious dependency and a tampered model bundle | M15 | Beginner | 60 | None beyond Python basics. |
| [L25](student/L25/LAB.md) | A poisoned fine-tuning run and the pattern scan | M16 | Advanced | 85 | L11 (backdoors in tabular models), L08 (digits). |
| [L26](student/L26/LAB.md) | An insecure prediction API and its hardened twin | M16 | Beginner | 55 | Python basics; no ML required. |
| [L27](student/L27/LAB.md) | Rate limits and abuse controls on a prediction API | M17 | Intermediate | 70 | L26 recommended. |
| [L28](student/L28/LAB.md) | A red-team matrix and a coverage statement | M18 | Advanced | 90 | L19, L21, L23, L24, L27. |
| [L29](student/L29/LAB.md) | Triaging suspicious usage in an AI service | M17 | Intermediate | 65 | L27. |
| [L30](student/L30/LAB.md) | Recovering from a compromised model | M19 | Challenge | 100 | L24 (bundle verification), L12 (evaluation discipline). |
| [L31](student/L31/LAB.md) | Fairness evaluation and a mitigation that only half-works | M19 | Intermediate | 75 | L02 (metrics), L15 (attribute inference). |
| [L32](student/L32/LAB.md) | A release gate that reads evidence | M20 | Challenge | 110 | L02, L12/13, L14, L19, L22, L23, L24, L28. |

## By module

- **M01** — L01 (beginner)
- **M02** — L02 (beginner)
- **M03** — L03 (beginner), L04 (intermediate)
- **M04** — L05 (beginner)
- **M05** — L06 (beginner), L07 (intermediate)
- **M06** — L08 (intermediate), L09 (advanced)
- **M07** — L10 (intermediate), L11 (advanced)
- **M08** — L12 (advanced), L13 (challenge)
- **M09** — L14 (intermediate), L15 (advanced)
- **M10** — L16 (intermediate)
- **M11** — L17 (beginner), L18 (intermediate)
- **M12** — L19 (beginner), L20 (intermediate)
- **M13** — L21 (intermediate), L22 (advanced)
- **M14** — L23 (intermediate)
- **M15** — L24 (beginner)
- **M16** — L25 (advanced), L26 (beginner)
- **M17** — L27 (intermediate), L29 (intermediate)
- **M18** — L28 (advanced)
- **M19** — L30 (challenge), L31 (intermediate)
- **M20** — L32 (challenge)
