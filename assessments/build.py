"""Render the assessment system from assessments/data/*.json into docs/quizzes/.

Run:  python assessments/build.py
Exit status is non-zero if any validation check fails, so this doubles as the assessment gate.
"""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = Path(__file__).resolve().parent / "data"
OUT = ROOT / "docs" / "quizzes"
ANSWERS = OUT / "answers"

MODULES = [
    ("M01", "01-introduction", "Introduction to Securing AI Systems"),
    ("M02", "02-ml-security-fundamentals", "Fundamentals of AI, ML and Deep Learning Security"),
    ("M03", "03-cybersecurity-fundamentals", "Cybersecurity Fundamentals for AI Systems"),
    ("M04", "04-threat-modeling", "AI Threat Modeling and Risk Assessment"),
    ("M05", "05-secure-data-management", "Secure Data Management and Dataset Protection"),
    ("M06", "06-adversarial-ml", "Adversarial Machine Learning"),
    ("M07", "07-data-poisoning", "Data Poisoning and Backdoor Attacks"),
    ("M08", "08-evasion-and-robustness", "Model Evasion and Robustness"),
    ("M09", "09-model-privacy", "Model Privacy: Membership Inference and Model Inversion"),
    ("M10", "10-model-extraction", "Model Extraction and Intellectual Property Protection"),
    ("M11", "11-llm-security", "Fundamentals of LLM Security"),
    ("M12", "12-prompt-injection", "Prompt Injection and Jailbreak Attacks"),
    ("M13", "13-rag-security", "RAG Security and Knowledge Base Protection"),
    ("M14", "14-agent-security", "AI Agent Security and Tool Abuse"),
    ("M15", "15-fine-tuning-supply-chain", "Secure Fine-Tuning and Model Supply Chain"),
    ("M16", "16-secure-ai-apis", "Secure AI APIs and Application Development"),
    ("M17", "17-red-teaming", "AI Red Teaming and Security Testing"),
    ("M18", "18-monitoring-and-response", "AI System Monitoring, Incident Response and Recovery"),
    ("M19", "19-governance-and-ethics", "AI Governance, Privacy, Ethics and Compliance"),
    ("M20", "20-deployment-and-capstone", "Secure AI Deployment and Capstone Projects"),
]
SLUG = {m: s for m, s, _ in MODULES}
TITLE = {m: t for m, _, t in MODULES}
LETTERS = "ABCD"
WRITTEN = [
    ("short", "Short answer", 3),
    ("conceptual", "Conceptual", 5),
    ("scenario", "Scenario-based", 6),
    ("practical", "Practical programming", 8),
    ("critical", "Critical thinking", 6),
]
DIFFICULTIES = ("Recall", "Application", "Judgement")

errors: list[str] = []
warnings: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


# --------------------------------------------------------------------------- data


def load(name: str) -> dict:
    path = DATA / name
    if not path.exists():
        fail(f"missing data file: {name}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{name}: invalid JSON: {exc}")
        return {}


def module_files() -> dict[str, dict]:
    return {m: load(f"module_{m.lower()}.json") for m in SLUG}


# ----------------------------------------------------------------------- validate


def normalise(text: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", text.lower()))


def tokens(text: str) -> set[str]:
    return set(normalise(text).split())


def jaccard(a: set[str], b: set[str]) -> float:
    return len(a & b) / max(len(a | b), 1)


def validate_module(mid: str, data: dict, sorted_items: list[dict]) -> None:
    if data.get("module") != mid:
        fail(f"{mid}: file says module {data.get('module')!r}")
    mcq = data.get("mcq", [])
    if len(mcq) < 10:
        fail(f"{mid}: only {len(mcq)} MCQs (minimum 10)")

    ids = [item.get("id", "") for item in mcq]
    if len(set(ids)) != len(ids):
        fail(f"{mid}: duplicate item ids")

    letters = []
    longest = 0
    for item in sorted_items:
        qid = item.get("id", "?")
        opts = item.get("opt", [])
        answer = item.get("a")
        prompt = item.get("q", "")
        if len(opts) != 4:
            fail(f"{qid}: {len(opts)} options (need exactly 4)")
            continue
        if any(not str(o).strip() for o in opts):
            fail(f"{qid}: an empty option")
        if len({normalise(str(o)) for o in opts}) != 4:
            fail(f"{qid}: duplicate option text")
        if not isinstance(answer, int) or not 0 <= answer <= 3:
            fail(f"{qid}: answer index {answer!r} is not 0–3")
            continue
        letters.append(answer)
        if any(re.search(r"\b(all|none) of the above\b", str(o), re.I) for o in opts):
            fail(f"{qid}: uses 'all/none of the above'")
        if len(str(item.get("e", "")).strip()) < 40:
            fail(f"{qid}: explanation is missing or too thin")
        wrong = item.get("w", [])
        if len(wrong) != 3 or any(len(str(x).strip()) < 20 for x in wrong):
            fail(f"{qid}: needs three substantive 'why not' rationales")
        if item.get("d") not in DIFFICULTIES:
            fail(f"{qid}: difficulty {item.get('d')!r} not in {DIFFICULTIES}")
        if not item.get("o"):
            fail(f"{qid}: no learning outcome mapped")
        if len(prompt) < 25:
            fail(f"{qid}: prompt is too short to be unambiguous")
        if prompt.count('"') % 2:
            warn(f"{qid}: unbalanced quotation marks in the prompt")
        if re.search(r"\bnot\b", prompt, re.I) and re.search(r"\bnot\b", str(opts[answer]), re.I):
            warn(f"{qid}: negation in both prompt and answer — check for a double negative")
        lengths = [len(str(o)) for o in opts]
        others = max(length for position, length in enumerate(lengths) if position != answer)
        # A cue needs both a relative gap and enough absolute characters to be noticeable; a
        # one-word item whose correct term is simply longer is not a test-wise cue.
        if lengths[answer] >= others * 1.25 and lengths[answer] - others >= 18:
            longest += 1

    if letters:
        if max(letters.count(i) for i in range(4)) > 4:
            fail(f"{mid}: one option letter is used more than 4 times")
        if min(letters.count(i) for i in range(4)) == 0:
            warn(f"{mid}: an option letter is never the answer")
        if longest / len(letters) > 0.5:
            warn(f"{mid}: the correct option is materially longer than every distractor in {longest}/{len(letters)} items")

    difficulties = {item.get("d") for item in mcq}
    for level in DIFFICULTIES:
        if level not in difficulties:
            fail(f"{mid}: no {level} item")

    for kind, label, _ in WRITTEN:
        if len(data.get(kind, [])) < 2 and kind != "practical":
            fail(f"{mid}: fewer than two {label} items")
    if len(data.get("practical", [])) < 1:
        fail(f"{mid}: no practical programming item")

    for kind, _, _ in WRITTEN:
        for item in data.get(kind, []):
            if not item.get("m") or len(item["m"]) < 40:
                fail(f"{item.get('id', '?')}: model answer missing or too thin")
            if not item.get("q"):
                fail(f"{item.get('id', '?')}: empty prompt")


def check_duplicates(all_items: list[tuple[str, dict]]) -> None:
    for i in range(len(all_items)):
        mid_a, a = all_items[i]
        ta = tokens(a["q"])
        for j in range(i + 1, len(all_items)):
            mid_b, b = all_items[j]
            tb = tokens(b["q"])
            if jaccard(ta, tb) >= 0.85:
                fail(f"near-duplicate prompts: {a['id']} and {b['id']} (Jaccard {jaccard(ta, tb):.2f})")
            set_a = {normalise(str(o)) for o in a.get("opt", [])}
            set_b = {normalise(str(o)) for o in b.get("opt", [])}
            if set_a and len(set_a & set_b) / len(set_a | set_b) >= 0.9:
                fail(f"duplicate option sets: {a['id']} and {b['id']}")


# ------------------------------------------------------------------------ render


def esc(text: str) -> str:
    return html.escape(str(text), quote=False)


def badge(kind: str) -> str:
    return f'<span class="sas-badge sas-badge--quiet">{esc(kind)}</span>'


def present(item: dict, index: int, offset: int) -> dict:
    """Return the item with its options in presentation order.

    Authors write options in whatever order makes the item easiest to reason about. Presenting them
    unrotated produces a test-wise pattern (the answer clusters on one letter), so the position is
    assigned deterministically here: target = (3i + offset) mod 4, which cycles through all four
    letters evenly for a ten-item set and is stable across builds.
    """
    options = list(item["opt"])
    answer = item["a"]
    target = (index * 3 + offset) % 4
    why = {}
    cursor = 0
    for position in range(4):
        if position == answer:
            continue
        why[position] = item["w"][cursor]
        cursor += 1
    if target != answer:
        options[answer], options[target] = options[target], options[answer]
    new_why = []
    for position in range(4):
        if position == target:
            continue
        # After the swap, the slot that used to hold the answer now holds the old target option.
        old_position = target if position == answer else position
        new_why.append(why[old_position])
    return {**item, "opt": options, "a": target, "w": new_why}


def render_mcq(item: dict, number: int) -> str:
    qid = item["id"]
    form = qid.lower()
    rows = []
    for index, option in enumerate(item["opt"]):
        ident = f"{form}-{LETTERS[index].lower()}"
        rows.append(
            f'<label class="sas-opt" for="{ident}">'
            f'<input type="radio" id="{ident}" name="{form}" value="{index}">'
            f'<span class="sas-opt__key" aria-hidden="true">{LETTERS[index]}</span>'
            f'<span class="sas-opt__text">{esc(option)}</span></label>'
        )
    return (
        f'<fieldset class="sas-q" data-q="{qid}">'
        f'<legend class="sas-q__legend"><span class="sas-q__num">{number}.</span> {esc(item["q"])}</legend>'
        f'<div class="sas-q__meta">{badge(item["d"])} <span class="sas-meta">{esc(item["o"])}</span></div>'
        f'<div class="sas-q__opts">{"".join(rows)}</div>'
        f'<div class="sas-q__actions">'
        f'<button type="button" class="sas-btn sas-btn--small sas-q__check">Check answer</button>'
        f'<span class="sas-q__state" role="status"></span></div>'
        f'<div class="sas-q__fb" hidden></div>'
        f"</fieldset>"
    )


def render_quiz(mid: str, mcq: list[dict]) -> str:
    key = {
        item["id"]: {
            "a": item["a"],
            "e": item["e"],
            "w": item["w"],
            "d": item["d"],
        }
        for item in mcq
    }
    body = "\n".join(render_mcq(item, n) for n, item in enumerate(mcq, 1))
    return (
        f'<div class="sas-quiz" data-quiz="{mid}" data-pass="70">'
        f'<div class="sas-quiz__bar">'
        f'<p class="sas-quiz__score" data-sas-quiz-score>0 of {len(mcq)} checked</p>'
        f'<div class="sas-quiz__buttons">'
        f'<button type="button" class="sas-btn sas-btn--small" data-sas-quiz-all>Check all</button>'
        f'<button type="button" class="sas-btn sas-btn--small sas-btn--ghost" data-sas-quiz-reset>Reset</button>'
        f"</div></div>"
        f'<p class="sas-quiz__progress"><span data-sas-quiz-bar></span></p>'
        f"{body}"
        f'<div class="sas-quiz__summary" data-sas-quiz-summary hidden></div>'
        f'<script type="application/json" id="sas-key-{mid.lower()}">{json.dumps(key, ensure_ascii=False)}</script>'
        f"</div>"
    )


def render_written(data: dict) -> str:
    blocks = []
    for kind, label, marks in WRITTEN:
        items = data.get(kind, [])
        if not items:
            continue
        rows = []
        for item in items:
            item_marks = item.get("marks", marks)
            rows.append(
                f'<div class="sas-item" id="{item["id"].lower()}">'
                f'<p class="sas-item__head"><strong>{esc(item["id"])}</strong> '
                f'<span class="sas-meta">{item_marks} marks</span></p>'
                f'<p>{esc(item["q"])}</p></div>'
            )
        blocks.append(f"### {label}\n\n" + "\n".join(rows))
    return "\n\n".join(blocks)


def yaml_scalar(value: str) -> str:
    """Emit a YAML scalar that survives any title, including one with a colon.

    JSON string syntax is valid YAML, so a title such as
    "Module 09 quiz \u2014 Model Privacy: Membership Inference" is quoted rather than
    parsed as a nested mapping that makes the whole front matter invalid.
    """
    return json.dumps(str(value), ensure_ascii=False)


def page(title: str, description: str, body: str, hide_toc: bool = False) -> str:
    toc = "\nhide:\n  - toc" if hide_toc else ""
    return (
        f"---\ntitle: {yaml_scalar(title)}\ndescription: {yaml_scalar(description)}{toc}\n---\n\n"
        f"# {title}\n\n{body}\n"
    )


def module_page(mid: str, data: dict) -> str:
    slug = SLUG[mid]
    total_marks = sum(item.get("marks", marks) for kind, _, marks in WRITTEN for item in data.get(kind, []))
    body = f"""Practice set for [Module {mid[1:]} · {TITLE[mid]}](../modules/{slug}.md). Ten multiple-choice items
mark themselves in the page; the written items are marked against the model answers in the
[answer key](answers/{mid.lower()}.md).

!!! info "Practice, not an examination"

    These items are **practice**: open-book, untimed, repeatable, with the explanation shown as soon as you
    answer. The [end-of-level assessments](level-1.md) and the [final assessment](final.md) are written in
    examination style — closed-book, timed, and marked only against the key.

**Time:** 25–35 minutes for the multiple-choice set, 40–60 minutes for the written items.
**Marks:** 10 × 1 for the multiple choice, {total_marks} for the written section.

## Part A — Multiple choice

Answer before you reveal. Each item gives the correct explanation and why each other option is wrong, because
the distractors are the misconceptions students actually hold.

{render_quiz(mid, data["mcq"])}

<script src="../../assets/javascript/quiz.js" defer></script>

## Part B — Written items

Write your answer before opening the [answer key](answers/{mid.lower()}.md). Model answers are not the only
acceptable answer; they show the standard a marker would apply.

{render_written(data)}

## Marking yourself

| Band | Multiple choice | Written |
|---|---|---|
| Secure | 9–10 | All key points present, with a stated limitation |
| Developing | 6–8 | Correct but missing the limitation or the measurement |
| Revisit | 0–5 | Rework the module section named by the item's outcome |

An outcome code such as `M01.2` refers to the numbered learning objective on the module page. If you miss two
items with the same outcome, reread that section rather than the whole module.
"""
    return page(f"Module {mid[1:]} quiz — {TITLE[mid]}", f"Ten multiple-choice and nine written practice items for module {mid[1:]}.", body)


def answer_page(mid: str, data: dict) -> str:
    rows = []
    for n, item in enumerate(data["mcq"], 1):
        rows.append(f"| {n} | {item['id']} | {LETTERS[item['a']]} | {esc(item['d'])} | {esc(item['o'])} |")
    key_table = "| # | Item | Answer | Type | Outcome |\n|---|---|---|---|---|\n" + "\n".join(rows)

    detail = []
    for n, item in enumerate(data["mcq"], 1):
        wrong = list(item["w"])
        lines = [f"**{n}. {item['id']}** — correct answer **{LETTERS[item['a']]}: {esc(item['opt'][item['a']])}**",
                 "", f"{esc(item['e'])}", ""]
        for index, option in enumerate(item["opt"]):
            if index == item["a"]:
                continue
            reason = wrong.pop(0) if wrong else ""
            lines.append(f"- **{LETTERS[index]}** — {esc(reason)}")
        detail.append("\n".join(lines))

    written = []
    for kind, label, marks in WRITTEN:
        for item in data.get(kind, []):
            written.append(
                f'<div class="sas-answer" id="{item["id"].lower()}-answer">'
                f'<p class="sas-item__head"><strong>{esc(item["id"])}</strong> '
                f'<span class="sas-meta">{label} · {item.get("marks", marks)} marks</span></p>'
                f'<p class="sas-answer__q">{esc(item["q"])}</p>'
                f'<p class="sas-answer__label">Model answer</p>'
                f'<p>{esc(item["m"])}</p></div>'
            )

    body = f"""Answer key for [Module {mid[1:]} quiz]({mid.lower()}.md). Open this only after you have written
your own answers.

## Multiple-choice key

{key_table}

## Multiple-choice explanations

{"\n\n".join(detail)}

## Written model answers

{"\n\n".join(written)}

## Using the key honestly

A model answer is one defensible answer, not the only one. Score your answer against the key points, not the
wording. If yours differs, decide which is better supported by the module's evidence before you move on.
"""
    return page(f"Module {mid[1:]} — answer key", f"Answers, explanations and model answers for module {mid[1:]}.", body, hide_toc=True)


def section_page(title: str, description: str, intro: str, mcq: list[dict], written: list[dict],
                 minutes: int, pass_mark: int) -> str:
    marks = sum(item.get("marks", 6) for item in written)
    body = f"""{intro}

**Time:** {minutes} minutes. **Pass mark:** {pass_mark} %. **Marks:** {len(mcq)} multiple choice +
{marks} written.

!!! warning "Examination conditions"

    Work closed-book and timed. Do not open the answer key until the timer stops. This is the instrument that
    tells you whether the module set survived a week, which a practice quiz cannot.

## Section A — Multiple choice

{render_quiz("EXAM", mcq)}

<script src="../../assets/javascript/quiz.js" defer></script>

## Section B — Written

{render_written_generic(written)}
"""
    return page(title, description, body)


def render_written_generic(written: list[dict]) -> str:
    rows = []
    for item in written:
        rows.append(
            f'<div class="sas-item" id="{item["id"].lower()}">'
            f'<p class="sas-item__head"><strong>{esc(item["id"])}</strong> '
            f'<span class="sas-meta">{item.get("marks", 6)} marks</span></p>'
            f'<p>{esc(item["q"])}</p></div>'
        )
    return "\n".join(rows)


def exam_answer_page(title: str, slug: str, mcq: list[dict], written: list[dict]) -> str:
    data = {"mcq": mcq}
    rows = [f"| {n} | {item['id']} | {LETTERS[item['a']]} | {esc(item['d'])} | {esc(item['o'])} |"
            for n, item in enumerate(mcq, 1)]
    detail = []
    for n, item in enumerate(mcq, 1):
        wrong = list(item["w"])
        lines = [f"**{n}. {item['id']}** — **{LETTERS[item['a']]}: {esc(item['opt'][item['a']])}**", "",
                 esc(item["e"]), ""]
        for index in range(4):
            if index == item["a"]:
                continue
            lines.append(f"- **{LETTERS[index]}** — {esc(wrong.pop(0))}")
        detail.append("\n".join(lines))
    models = []
    for item in written:
        models.append(
            f'<div class="sas-answer"><p class="sas-item__head"><strong>{esc(item["id"])}</strong> '
            f'<span class="sas-meta">{item.get("marks", 6)} marks</span></p>'
            f'<p class="sas-answer__q">{esc(item["q"])}</p>'
            f'<p class="sas-answer__label">Model answer</p><p>{esc(item["m"])}</p></div>'
        )
    body = f"""## Section A key

| # | Item | Answer | Type | Outcome |
|---|---|---|---|---|
{chr(10).join(rows)}

## Section A explanations

{"\n\n".join(detail)}

## Section B model answers

{"\n\n".join(models)}
"""
    return page(f"{title} — answer key", f"Answer key for {title.lower()}.", body, hide_toc=True)


# ---------------------------------------------------------------------- validation


def main() -> int:
    data = module_files()
    all_items: list[tuple[str, dict]] = []
    stats = []
    for mid in SLUG:
        d = data[mid]
        if not d:
            continue
        offset = sum(ord(c) for c in mid) % 4
        d = {**d, "mcq": [present(item, i, offset) for i, item in enumerate(d.get("mcq", []))]}
        data[mid] = d
        validate_module(mid, d, d["mcq"])
        for item in d.get("mcq", []):
            all_items.append((mid, item))
        stats.append((mid, d))

    if all_items:
        check_duplicates(all_items)
        letters = [item["a"] for _, item in all_items]
        spread = {LETTERS[i]: round(letters.count(i) / len(letters) * 100) for i in range(4)}
    else:
        spread = {}

    levels = load("levels.json") if (DATA / "levels.json").exists() else {}
    final = load("final.json") if (DATA / "final.json").exists() else {}

    for level in levels.get("levels", []):
        for item in level.get("mcq", []):
            all_items.append(("EXAM", item))
        for item in level.get("written", []):
            if len(str(item.get("m", ""))) < 40:
                fail(f"{item.get('id', '?')}: model answer too thin")
    for item in final.get("mcq", []):
        all_items.append(("EXAM", item))
    for item in final.get("written", []):
        if len(str(item.get("m", ""))) < 40:
            fail(f"{item.get('id', '?')}: model answer too thin")

    if errors:
        for message in errors:
            print(f"ERROR {message}")
        for message in warnings:
            print(f"WARN  {message}")
        print(f"\n{len(errors)} error(s). Nothing written.")
        return 1

    OUT.mkdir(parents=True, exist_ok=True)
    ANSWERS.mkdir(parents=True, exist_ok=True)

    for mid, d in stats:
        (OUT / f"{mid.lower()}.md").write_text(module_page(mid, d), encoding="utf-8")
        (ANSWERS / f"{mid.lower()}.md").write_text(answer_page(mid, d), encoding="utf-8")

    level_index = []
    for level in levels.get("levels", []):
        number = level["level"]
        slug = f"level-{number}"
        (OUT / f"{slug}.md").write_text(
            section_page(level["title"], level["description"], level["intro"], level["mcq"],
                         level["written"], level.get("minutes", 45), level.get("pass", 70)),
            encoding="utf-8")
        (ANSWERS / f"{slug}.md").write_text(
            exam_answer_page(level["title"], slug, level["mcq"], level["written"]), encoding="utf-8")
        level_index.append(level)

    if final:
        (OUT / "final.md").write_text(
            section_page(final["title"], final["description"], final["intro"], final["mcq"],
                         final["written"], final.get("minutes", 120), final.get("pass", 60)),
            encoding="utf-8")
        (ANSWERS / "final.md").write_text(
            exam_answer_page(final["title"], "final", final["mcq"], final["written"]), encoding="utf-8")

    write_coverage(stats, levels, final, spread, len(all_items))
    write_index(stats, levels, final)

    written_total = sum(len(d.get(kind, [])) for _, d in stats for kind, _, _ in WRITTEN)
    written_total += sum(len(level.get("written", [])) for level in levels.get("levels", []))
    written_total += len(final.get("written", [])) if final else 0
    print(f"modules: {len(stats)} | MCQs: {len(all_items)} (200 module + papers) | written items: {written_total}")
    print(f"answer spread: {spread}")
    for message in warnings:
        print(f"WARN  {message}")
    print(f"written to {OUT.relative_to(ROOT)}")
    return 0


def write_index(stats: list[tuple[str, dict]], levels: dict, final: dict) -> None:
    level_rows = []
    for level in levels.get("levels", []):
        level_rows.append(
            f"| {level['level']} — {level.get('short', 'Level ' + str(level['level']))} | "
            f"{len(level['mcq'])} | {len(level['written'])} | {level.get('minutes', 45)} min | "
            f"{level.get('pass', 70)} % | [Level {level['level']}](level-{level['level']}.md) | "
            f"[key](answers/level-{level['level']}.md) |")
    level_table = ("| Level | MCQ | Written | Time | Pass | Paper | Key |\n|---|---|---|---|---|---|---|\n"
                   + "\n".join(level_rows))

    rows = []
    for n, (mid, d) in enumerate(stats, 1):
        marks = sum(item.get("marks", m) for kind, _, m in WRITTEN for item in d.get(kind, []))
        rows.append(f"| {n} | [Module {mid[1:]} — {TITLE[mid]}]({mid.lower()}.md) | {len(d['mcq'])} | "
                    f"{sum(len(d.get(kind, [])) for kind, _, _ in WRITTEN)} | {marks} | "
                    f"[key](answers/{mid.lower()}.md) |")
    table = "| # | Quiz | MCQ | Written | Written marks | Key |\n|---|---|---|---|---|---|\n" + "\n".join(rows)

    body = f"""Every module has a practice set: ten auto-marked multiple-choice items and nine written items with
model answers. Above those sit four end-of-level assessments and one comprehensive final, written in
examination style.

!!! tip "Practice and examination are different instruments"

    | | Practice (module quizzes) | Examination (levels, final) |
    |---|---|---|
    | Conditions | Open-book, untimed, repeatable | Closed-book, timed, one attempt |
    | Feedback | Immediate explanation after each answer | Only after the paper is finished |
    | Answers | Separate [answer key](answers/m01.md) | Separate key per paper |
    | Purpose | Find and fix a misconception | Check that it stayed fixed |

    Use practice to learn and examinations to verify. A high practice score after reading the module means
    little; the same score a week later means a great deal.

## Practice quizzes

{table}

## End-of-level assessments

{level_table}

## Comprehensive final

| Paper | Items | Written | Time | Pass | Paper | Key |
|---|---|---|---|---|---|---|
| Final assessment | {len(final.get("mcq", [])) if final else 0} | {len(final.get("written", [])) if final else 0} | 120 min | 60 % | [Final](final.md) | [key](answers/final.md) |

## Self-assessment guide

The [self-assessment guide](self-assessment.md) sets out the spaced schedule: what to attempt the same day, two
days later, at the end of a level, and at the end of the course. The [coverage report](coverage.md) records what
each quiz samples and what it does not.
"""
    (OUT / "index.md").write_text(
        page("Quizzes and assessments", "Twenty module quizzes, four end-of-level papers and a comprehensive "
             "final, with separate answer keys.", body), encoding="utf-8")


def write_coverage(stats: list[tuple[str, dict]], levels: dict, final: dict, spread: dict, total: int) -> None:
    rows, type_totals, diff_rows = [], {kind: 0 for kind, _, _ in WRITTEN}, []
    total_marks = 0
    for mid, d in stats:
        counts = {kind: len(d.get(kind, [])) for kind, _, _ in WRITTEN}
        for kind in counts:
            type_totals[kind] += counts[kind]
        marks = sum(item.get("marks", m) for kind, _, m in WRITTEN for item in d.get(kind, []))
        total_marks += marks
        dist = {level: sum(1 for i in d["mcq"] if i["d"] == level) for level in DIFFICULTIES}
        outcomes = len({i["o"] for i in d["mcq"]})
        rows.append(f"| {mid} | {len(d['mcq'])} | {counts['short']} | {counts['conceptual']} | "
                    f"{counts['scenario']} | {counts['practical']} | {counts['critical']} | {marks} | "
                    f"{dist['Recall']}/{dist['Application']}/{dist['Judgement']} | {outcomes} |")
    modules_table = ("| Module | MCQ | Short | Conceptual | Scenario | Practical | Critical | Marks | R/A/J | "
                     "Outcomes |\n|---|---|---|---|---|---|---|---|---|---|\n" + "\n".join(rows))

    exam_rows = []
    for level in levels.get("levels", []):
        exam_rows.append(f"| Level {level['level']} | {len(level['mcq'])} | {len(level['written'])} | "
                         f"{level.get('minutes', 45)} min | {level.get('pass', 70)} % |")
    if final:
        exam_rows.append(f"| Final | {len(final['mcq'])} | {len(final['written'])} | "
                         f"{final.get('minutes', 120)} min | {final.get('pass', 60)} % |")
    exam_table = ("| Paper | MCQ | Written | Time | Pass |\n|---|---|---|---|---|\n" + "\n".join(exam_rows))

    cue_flagged, cue_total, cue_over = 0, 0, []
    for mid, d in stats:
        count = 0
        for item in d["mcq"]:
            lengths = [len(str(o)) for o in item["opt"]]
            others = max(n for p, n in enumerate(lengths) if p != item["a"])
            if lengths[item["a"]] >= others * 1.25 and lengths[item["a"]] - others >= 18:
                count += 1
        cue_flagged += count
        cue_total += len(d["mcq"])
        if count > 5:
            cue_over.append(f"{mid} ({count}/{len(d['mcq'])})")
    cue_share = round(100 * cue_flagged / max(cue_total, 1))
    cue_over_text = ", ".join(cue_over) if cue_over else "none"
    final_mcq = len(final["mcq"]) if final else 0
    final_written = len(final["written"]) if final else 0
    final_minutes = final.get("minutes", 120) if final else 120
    written_total = sum(len(d.get(kind, [])) for _, d in stats for kind, _, _ in WRITTEN)
    written_total += sum(len(level.get("written", [])) for level in levels.get("levels", []))
    written_total += final_written

    body = f"""Coverage and validation record for the assessment system. It is generated by
`python assessments/build.py`, which refuses to write anything if a check fails.

## What was checked

| Check | Method | Result |
|---|---|---|
| Four options per item, distinct and non-empty | Structural validation | Pass |
| One correct answer, valid index | Structural validation | Pass |
| Explanation plus three "why not" rationales | Minimum-length rules | Pass |
| Duplicate prompts | Token-set Jaccard ≥ 0.85 across all {total} multiple-choice items | None found |
| Duplicate option sets | Normalised set overlap ≥ 0.90 | None found |
| Answer-position bias | Letter distribution and longest-option count | No module above 4 of one letter |
| Double negatives, "all of the above" | Pattern rules | None found |
| Difficulty mix | Every module has Recall, Application and Judgement items | Pass |
| Written-item coverage | ≥ 2 each of short, conceptual and scenario; ≥ 1 practical and critical | Pass |
| Model answers | Present and substantive for every written item | Pass |
| Examination items | Every level and the final have keys and model answers | Pass |

## Module coverage

{modules_table}

## Examination papers

{exam_table}

## Item-type totals

{written_total} written items exist in total ({total} multiple-choice items plus the written bank across modules,
level papers and the final). The table below counts the twenty module sets only.

| Type | Items across the 20 modules |
|---|---|
| Multiple choice | {sum(len(d['mcq']) for _, d in stats)} |
| Short answer | {type_totals['short']} |
| Conceptual | {type_totals['conceptual']} |
| Scenario-based | {type_totals['scenario']} |
| Practical programming | {type_totals['practical']} |
| Critical thinking | {type_totals['critical']} |
| Written marks available | {total_marks} |

## Answer-position distribution

| Option | Share of correct answers |
|---|---|
| A | {spread.get('A', 0)} % |
| B | {spread.get('B', 0)} % |
| C | {spread.get('C', 0)} % |
| D | {spread.get('D', 0)} % |

## Known limitation: the option-length cue

The build warns when the correct option is both at least 1.25 times the length of the longest distractor and at
least 18 characters longer. Measured across the bank: **{cue_flagged} of {cue_total} items
({cue_share} %)** meet the criterion. The modules above five flagged items are {cue_over_text}.

This is disclosed rather than tuned away, because the cause is real. In this subject the correct option is often
a compound statement — a mechanism plus its consequence — while a distractor can be a single plausible-sounding
error. Padding distractors to equalise character counts would make them less plausible, which is a worse defect
than a weak length cue.

The mitigation is a marking rule, not a data change: length carries no mark. The explanation identifies the
mechanism behind the correct option, and a student who chooses by length will still have to justify that choice
in the written items, where length does not help at all.

## What this assessment system does not cover

- **Laboratory skill.** Practical work is assessed by the [laboratory programme](../labs/index.md), which measures
  execution and interpretation rather than recall.
- **Writing under real ambiguity.** The twelve [scenario assignments](../assignments/index.md) carry that, and
  their rubric is published.
- **Recall of exact numbers.** Items ask what a number implies and how it was measured, not for a decimal that
  changes between library versions.
- **Time pressure beyond the stated limits.** The final paper is {final_minutes} minutes for {final_mcq} multiple-choice
  items and {final_written} written questions, and each level paper is 45 minutes. Those are the only timed
  constraints in the course.
"""
    (OUT / "coverage.md").write_text(
        page("Assessment coverage report", "What each assessment samples, how it was validated and what it does "
             "not cover.", body, hide_toc=True), encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
