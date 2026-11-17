# Securing AI Systems — laboratory programme

32 self-contained laboratories for BS Data Science students working independently. Every lab uses
synthetic data, small models, local mock services and free open-source tools. No lab attacks a real system,
and none requires a paid API key or a network connection at run time.

## Layout

```
labs/
  LAB_INDEX.md            all labs, with module, difficulty and prerequisite
  CHECKLIST.md            completion checklist
  VALIDATION_REPORT.md    what was executed, the verified results and the known limits
  datasets/               generated synthetic datasets (no downloads)
  scripts/make_datasets.py  regenerates every dataset deterministically
  common/labkit.py        shared path/table helpers (no answers)
  student/L01/LAB.md      the manual: scenario, steps, hints, tasks, submission
  student/L01/starter.py  runnable skeleton with one TODO per step
  solutions/L01/SOLUTION.md  approach, rubric and reference results
  solutions/L01/solution.py  complete, executed implementation
```

Solutions are in a sibling directory, never inside the student folder.

## Setup

```bash
python -m venv .venv
# activate it, then
python -m pip install --upgrade pip
python -m pip install -r requirements-labs.txt
python labs/scripts/make_datasets.py
python scripts/check_env.py
```

Python 3.12 or newer is required (validated on 3.14.7). Every dependency is pinned to the version the labs were
validated against. CPU only; every lab solution finishes in under 11 seconds on a laptop.

## How to work a lab

1. Read sections 1–6 of `LAB.md` and confirm the entry requirements.
2. Open `starter.py`, read the numbered TODOs, and implement them.
3. Compare your output with section 9 ("Expected results"). If it differs, read section 10 and the hints.
4. Answer the student tasks in a short report; attempt at least one challenge.
5. Only then open the solution, and use the rubric in `SOLUTION.md` to mark your own work.

## Difficulty

Beginner labs teach a single technique with a full walkthrough. Intermediate labs add an attack and its
detection. Advanced labs require a measurement or a design decision and a short written justification.
Challenge labs combine several modules and expect independent judgement.

## Safety

All offensive steps run against data and services defined inside the lab. The mock assistant, mock API,
toy agent and local index are simulated in Python. If you adapt a lab to another system, you must have
written authorisation for that system; the course does not provide it.
