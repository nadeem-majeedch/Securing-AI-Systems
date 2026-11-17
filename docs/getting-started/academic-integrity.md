---
title: Academic Integrity and Responsible Use
description: The rules for using AI security tools, testing only what you are authorised to test, citing sources, handling sensitive data, and disclosing vulnerabilities.
---

# Academic Integrity and Responsible Use

This course teaches you to break AI systems. Everything here assumes you will use that ability the way a professional does: with written authorisation, minimal impact, evidence, and disclosure that protects the people affected.

The rules below are not decoration. They are the professional standard the course is preparing you for, and they are graded where an assessment can test them.

!!! warning "The one rule that matters most"

    **Never test a system you do not own or have explicit written permission to test.** Not a classmate's project, not your university's portal, not a public chatbot, not "just a prompt". Indirect prompt injection against a production assistant is unauthorised access, and it is a criminal offence in many jurisdictions, including under computer-misuse legislation in Pakistan and the EU.

## 1. Responsible use of AI security tools

The course gives you working implementations of evasion, poisoning, extraction and injection. Tools do not know whether you are authorised; you do.

| Tool or technique | Legitimate use | Never |
|---|---|---|
| Adversarial example generators (FGSM, PGD) | Models you trained, or supplied sandbox models | Attacking a deployed classifier to make it misclassify real transactions, admissions or diagnoses |
| Poisoning and backdoor demonstrations | Synthetic datasets in `labs/datasets/` | Contaminating a public dataset, a shared repository, or a model you do not own |
| Membership inference and model inversion | Models trained on synthetic data, to measure a privacy risk | Probing a production model to learn about real people in its training data |
| Model extraction | Your own endpoint, with a query budget you set | Scraping someone's paid API to clone their model |
| Prompt injection and jailbreaks | The course's local models and sandboxed applications | Any deployed assistant, any account you were not given, any other person's data |
| Denial-of-service and resource exhaustion | A local service you started, with a timeout | Anything that could take a service offline for other people |

**Practical safeguards, applied by default:**

- Work in a virtual environment and a disposable directory; assume any script you run writes files.
- Keep offensive work local. Do not point a lab script at a hostname unless the lab tells you to and you started that host.
- Set a spending or query limit before you loop a request, even locally.
- Stop when a proof of concept demonstrates access. Recursive exploitation, persistence and data exfiltration are not part of any lab in this course.
- Delete synthetic data, model bundles and logs when a lab's cleanup step says to.

!!! danger "Never put real data in a notebook"

    Not a real patient record that "looks anonymised", not a live API key, not a dump from your internship. Use `labs/datasets/` or generate your own with `labs/scripts/make_datasets.py`. A notebook that contains real personal data is a data-protection incident whether or not you publish it.

## 2. Authorized security testing

Authorisation is a document, not a feeling. Before testing anything outside the course sandbox you need written scope that states:

| Element | What it must say |
|---|---|
| **Targets** | Exact hosts, endpoints, models, accounts and data ranges in scope |
| **Exclusions** | What is explicitly out of scope — usually production data, third-party services, other tenants |
| **Dates and times** | The window in which testing may occur |
| **Permitted techniques** | Which attack classes are allowed; injection and extraction may be permitted where denial of service is not |
| **Stop conditions** | The events that end the test immediately — a real user affected, a service degraded, data encountered |
| **Contacts** | Who to call, at what hour, when something goes wrong |
| **Approver** | A named person with authority over the system, and their signature |

Three things follow from that list:

1. **"It was publicly accessible" is not authorisation.** Neither is a bug-bounty programme's mere existence, unless your target and technique are inside its published rules.
2. **A course exercise is not authorisation for a real system.** The capstone allows a real system only if its owner has authorised you in writing, and the brief asks you to attach that authorisation.
3. **Authorisation can be withdrawn.** If the contact says stop, you stop, save your evidence and write up what you had reached.

Module 17 and the capstone make this a graded deliverable, because reviewers judge the paperwork as much as the technique.

## 3. Academic honesty

The course's assessment design assumes you will mark yourself honestly. That only works if the work is yours.

| Instrument | What is allowed | What is not |
|---|---|---|
| Laboratory reports | Discussion with peers about concepts; your own runs, your own numbers | Copying another student's results table, or a screenshot of their run |
| Quizzes | Open book, open notes, unlimited attempts | Copying an answer key from the site into an assessed sitting where the institution forbids it |
| Assignments and projects | Citing sources and tools; declaring help you received | Submitting generated text or code as your own without declaration |
| Capstone | A real system **with written authorisation**; public sources | Assessing a system you were not authorised to test, then describing it as authorised |

**Declare assistance.** If a tutor, a peer, a textbook or an AI assistant materially shaped a submission, say so in the submission's declaration. Declared help is normal professional practice; undeclared help is misconduct.

**Report your real numbers.** The laboratories state numeric success criteria, and it is obvious when a report contains numbers nobody produced: perfect attack success rates, no variance across seeds, a runtime that does not match the code. A result that did not meet the criterion, honestly reported with an explanation, is worth more than a fabricated pass — and it is what the rubric rewards.

**Do not fabricate evidence.** Seeds, environment fingerprints, checksums and logs exist so that your work can be reproduced. Inventing them is the one failure that can end a course of study.

## 4. Proper research citation

Every claim in this course traces to a source, and yours should too. Cite at the point of use, not in a bibliography at the end that nobody checks.

### The minimum for each source type

| Source | What to include | Example |
|---|---|---|
| Journal or conference paper | Authors, title, venue, year, DOI or arXiv ID | Carlini, N. and Wagner, D. "Towards Evaluating the Robustness of Neural Networks." *IEEE S&P* 2017. doi:10.1109/SP.2017.49 |
| Preprint | Authors, title, arXiv ID, version and date if the result is contested | Zou, A. et al. "Universal and Transferable Adversarial Attacks on Aligned Language Models." arXiv:2307.15043, 2023 |
| Standard | Body, number, edition, title, clause if you rely on a specific requirement | ISO/IEC 42001:2023, *AI management system* |
| Framework | Owner, edition, item identifier, access date (these change) | OWASP, *Top 10 for LLM Applications*, 2025 edition, LLM01:2025, accessed November 2026 |
| Tool or library | Project, version, and the command or configuration you used | Adversarial Robustness Toolbox 1.19, `PyTorchClassifier`, CPU |
| Vendor advisory or incident report | Publisher, title, date, identifier (CVE if assigned) | Microsoft MSRC, CVE-2025-32711, 2025 |
| Regulation or case | Instrument, article or paragraph, and the official source | Regulation (EU) 2024/1689, Art. 6; 2024 BCCRT 149 (CanLII) |

### Practices that lose marks

- **Citing a blog post for a technical claim** the paper already settles. Go to the paper.
- **Citing a paper you have not opened.** If you cannot state its method in one sentence, you have not read it.
- **Citing a framework version you cannot date.** OWASP and ATLAS identifiers change between editions; the edition and access date are part of the citation.
- **Quoting ISO/IEC text.** The standards are copyrighted and sold. Describe the control, cite the clause title, link the catalogue.
- **A quotation without quotation marks**, even with a citation. That is plagiarism with a footnote.

### Citing this course

Modules are revised. Cite the module and the date you accessed it:

> Majeed, M. N. *Securing AI Systems*, Module 06: Adversarial Machine Learning. Department of Data Science (PUCIT), University of the Punjab, 2026. Accessed 20 November 2026.

[Credits and attribution](../attribution.md) has the current licence status and the citation form for third-party material in the course.

## 5. Ethical handling of sensitive datasets

Most AI security work involves data about people, and the interesting attacks often need the data to be realistic. That tension is the topic of Module 05, and it applies to your own work.

| Principle | In practice |
|---|---|
| **Use the least data that answers the question** | A 2,000-row synthetic table demonstrates a poisoning attack as well as a million rows. If you need scale, generate it |
| **Prefer synthetic data** | `labs/scripts/make_datasets.py` is deterministic and contains no real people. Extend it rather than reaching for a real dataset |
| **De-identify is not anonymise** | Removing names does not make a table safe. Quasi-identifiers re-identify people, as Module 05's laboratory shows with four columns |
| **Do not hoard** | Delete copies you no longer need, including in notebooks, checkpoints and screenshots. A leftover CSV in a project folder is still a copy |
| **Do not publish what you were given** | Coursework containing real organisational data does not go into a public repository, a portfolio, or a chat with an AI assistant |
| **Respect the licence of any dataset you do use** | A public dataset is not licence-free. [Credits and attribution](../attribution.md) records the terms of the one third-party dataset the course ships |
| **If you encounter real data during testing, stop** | Record what you saw, tell the contact in the scope document, and do not open, copy or exfiltrate more |

For a project that involves personal data, write the data-protection note first: what you hold, where it came from, the lawful basis, how long you keep it, and who can access it. Module 05 gives the template.

## 6. Responsible vulnerability disclosure

If you find a real vulnerability — during an authorised engagement, in a bug-bounty programme, or by accident — what you do next determines whether you are a security professional or a liability.

### Coordinated disclosure, step by step

1. **Stop and preserve evidence.** Minimal proof, screenshots of the request and response, timestamps. Do not download user data, do not persist access, do not "just check how bad it is".
2. **Find the right channel.** A `security.txt`, a security page, a bug-bounty platform, or the vendor's security contact. If none exists, contact the organisation directly and ask for its security contact — not its support queue.
3. **Report privately, in writing.** Include the impact, the reproduction, the affected asset, and what you have not done (no data exfiltrated, no persistence). Offer a fix and a retest.
4. **Agree a timeline.** Ninety days is the common default. Extend it if the vendor is genuinely working on it and communicates; publish earlier only if the vulnerability is being exploited.
5. **Do not publish before the fix.** Not a thread, not a "hypothetical" with enough detail to identify the target, not a conference abstract.
6. **Credit and correct.** After disclosure, publish the technical write-up with the vendor's fix, and correct anything you got wrong.

### What never to do

- Sell the vulnerability to a broker before the owner knows.
- Demand payment, a job, or a public thank-you as a condition of silence.
- Test the same issue on other customers of the same product "to see if it is systemic".
- Publish a working exploit for a system that is still unpatched.

!!! note "A finding in this course's own material"

    If you find a security problem in the course website, the notebooks or the scripts — a leaked secret, a script that writes outside its directory, an XSS in rendered content — report it privately through the repository's security policy (`SECURITY.md`) rather than in a public issue. It is a bug report, not a graded exercise.

## 7. If you are unsure

Ask before acting. A question costs a message; an unauthorised test can cost a degree, a job, or someone else's data.

| Situation | What to do |
|---|---|
| "Can I test this real app for my project?" | Only with the owner's written authorisation in the scope document. Otherwise use the sandbox or your own build |
| "Someone shared a dataset that looks real" | Do not open it in a notebook on a networked machine. Ask the instructor. Assume it contains personal data |
| "My lab result is wrong" | Report it with the seed, versions and output. A documented failure earns marks; a fabricated success does not |
| "I found a live vulnerability by accident" | Stop, do not look further, and follow §6. Tell the instructor if you are unsure who the owner is |
| "I used an AI assistant" | Declare it, describe what it contributed, and verify every claim it made |

---

*Related: [Privacy](privacy.md) (what the course stores, and does not) · [Credits and attribution](../attribution.md) · the safety statement in [Getting Started](index.md) · the repository's `SECURITY.md` for reporting issues in the course itself.*
