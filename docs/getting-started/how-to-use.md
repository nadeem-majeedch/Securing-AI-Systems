---
title: How to Use This Course
description: Reading modes, interface conventions, progress tracking and notebook workflow for the Securing AI Systems course.
---

# How to Use This Course

This page explains the interface: what the boxes mean, how to read a module efficiently, and how progress is tracked. It takes five minutes and saves considerably more than that.

## Reading modes

The same material is written to be read in three ways. Pick one deliberately rather than drifting between them.

| Mode | When | How |
|---|---|---|
| **Skim** | First contact with a part, or revision before an exam | Read the module overview, the threat and control table, and the "what you will be able to do" list. Skip the maths and the lab |
| **Study** | First proper pass | Read linearly, run the demonstration, complete the lab, take the quiz |
| **Reference** | During a project or after the course | Use search and the glossary; go straight to the controls checklist |

The trap is reading in *study* mode for everything and finishing nothing. Skim a part before you study it; you will retain more because the pieces have somewhere to attach.

## Interface conventions

### Admonitions

The coloured blocks are not decoration. Each type means something specific:

!!! note "Information"
    Context that helps but is not essential. Safe to skip on a revision pass.

!!! tip "Practical advice"
    A shortcut, a habit worth adopting, or an efficiency gain from experience.

!!! warning "Careful"
    A step where a mistake costs you time — a version mismatch, a wrong flag, a destructive command.

!!! danger "Do not do this"
    A step that can lose work, break your environment, or cross an ethical or legal boundary.

!!! example "Worked example"
    A concrete instance of the concept just explained. These are the fastest route to understanding.

!!! quote "Primary source"
    A short quotation with attribution. Follow the link; the original is always better than a summary.

### Status badges

Every module page carries a status badge. It is an honest signal, not a progress animation.

<span class="sas-badge sas-badge--complete">Complete</span>
The module satisfies the full content contract: theory, demonstration, laboratory, exercises, quiz and review.

<span class="sas-badge sas-badge--review">In review</span>
Content is written and undergoing accuracy and safety review. Expect changes.

<span class="sas-badge sas-badge--draft">Draft</span>
Content exists but may be incomplete. Laboratories may not yet be runnable.

<span class="sas-badge sas-badge--planned">Planned</span>
Scope is defined, teaching content is not yet written. The page tells you what the module will cover.

### Risk labels

Threat and control tables use three labels. They never rely on colour alone — the word is always present.

<span class="sas-badge sas-badge--danger">High</span>
Exploitable with modest effort, or consequences that are hard to reverse.

<span class="sas-badge sas-badge--warn">Medium</span>
Requires specific conditions or more capability than average.

<span class="sas-badge sas-badge--ok">Low</span>
Requires significant capability, or the impact is contained.

### Code blocks

Code blocks declare their language and are copyable with the icon in the top-right corner. Commands that differ by operating system appear as tabs:

=== "Windows"

    ```bash
    python -m venv .venv
    .venv\Scripts\activate
    ```

=== "macOS / Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

Annotations in code are marked with a `+` comment marker; hover or focus the marker to read the note.

### Diagrams

Diagrams are Mermaid, which means they are text: you can read them, copy them, and open them larger. Every diagram is followed by a collapsible text description, because a diagram is invisible to a screen reader.

## Your progress

Each module page has a **Mark this module complete** button. It records completion in your browser's local storage, on your device only.

- Nothing is sent anywhere: no account, no cookie, no analytics.
- Progress survives closing the browser but not clearing site data.
- The [learning roadmap](../roadmap.md) shows a per-part total, so you can see the shape of what remains.
- If your browser blocks local storage, the button still toggles for the session; it simply will not persist.

!!! tip "Progress is not completion"

    A tick means you finished the module's work, not that you mastered it. The quiz and the "communicate the risk" exercise are the real tests.

## Working with notebooks

Laboratories are Jupyter notebooks. Three habits make them work:

1. **Run cells in order from a fresh kernel.** Out-of-order execution is the single largest source of "the lab is broken" reports. Use *Restart Kernel and Run All* before you conclude something is wrong.
2. **Do not edit the provided cells.** Add your own below them, marked clearly. That way the lab's expected results remain comparable.
3. **Record results in the lab log.** Each lab has a results table; fill it in. A lab you cannot report is a lab you did not do.

Expected outputs are stated in the text. Small differences are normal and are explained by hardware, library patch versions and floating-point non-determinism — if a number differs in the second decimal place, that is usually fine. If a success rate differs by tens of percentage points, something is genuinely wrong: check the seed first, then the attack parameters.

## Taking notes that work

The course rewards a specific kind of note-taking. For each module, keep one page with four headings:

```text
1. What could go wrong here?      # attack surface, in your own words
2. How would I know?              # the signal or measurement that detects it
3. What stops it?                 # controls, and their limits
4. What did I actually run?       # commands, numbers, surprises
```

By Module 20 you will have twenty pages that constitute a personal reference you actually understand — far more useful than a downloaded cheat sheet.

## Using search

Search is client-side and indexes the entire published course. A few queries that work well:

- `prompt injection RAG` — finds cross-cutting content in Parts II and III
- `ATLAS` — every page that maps to MITRE ATLAS techniques
- `epsilon` — the perturbation budgets used across Level 2
- `authorisation` — scope and ethics guidance

The glossary defines every specialised term; if a term in a module is not obvious, look it up there rather than guessing.

## If you are teaching with this course

Instructor material — answer keys, rubrics with exemplars, session plans and timing notes — is maintained separately and is not part of the published site. See the repository's `CONTRIBUTING.md` and `DEVELOPMENT.md` for how that material is organised and reviewed.

## Next

<div class="sas-grid sas-grid--2" markdown>

<div class="sas-card" markdown>
<div class="sas-card__title">Check your prerequisites</div>
Ten minutes now avoids confusion later.

[Continue →](prerequisites.md)
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">Set up your environment</div>
One virtual environment, one install command, one check.

[Continue →](environment.md)
</div>

</div>
