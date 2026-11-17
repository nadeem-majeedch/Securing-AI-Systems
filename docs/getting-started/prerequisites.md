---
title: Prerequisites
description: What you need to know before starting Securing AI Systems, and where to refresh it.
---

# Prerequisites

The course assumes a working undergraduate foundation in Python and machine learning. It does **not** assume any background in security — Module 01 builds that from first principles.

This page is honest about what "assumed" means, so you can judge yourself accurately rather than optimistically.

## Required

<div class="sas-grid sas-grid--2" markdown>

<div class="sas-card sas-card--plain" markdown>
**Python, confidently.** Functions, classes, virtual environments, installing packages, reading a traceback and finding the line that actually failed. You will debug more than you write.
</div>

<div class="sas-card sas-card--plain" markdown>
**NumPy and pandas.** Array broadcasting, shapes and axes, boolean indexing, the difference between a view and a copy. Most laboratory bugs in this course are shape bugs.
</div>

<div class="sas-card sas-card--plain" markdown>
**A training loop.** You have trained a classifier, watched a loss curve, and know what overfitting looks like. You do not need to have built a model from scratch.
</div>

<div class="sas-card sas-card--plain" markdown>
**Basic evaluation literacy.** Accuracy, precision, recall, confusion matrices — and why accuracy alone misleads on imbalanced data.
</div>

<div class="sas-card sas-card--plain" markdown>
**Command line comfort.** Navigating directories, running scripts, reading help output, setting environment variables.
</div>

<div class="sas-card sas-card--plain" markdown>
**Git basics.** Clone, commit, branch, diff. Enough to keep your own laboratory work under version control.
</div>

</div>

## Helpful, not required

| Topic | Why it helps | Where it appears |
|---|---|---|
| Linear algebra | Understanding perturbation geometry and decision boundaries | Module 04 onward |
| Calculus and gradients | Deriving the fast gradient sign method rather than accepting it | Module 04 |
| Probability and statistics | Attack success rates, confidence intervals, differential privacy | Modules 05, 08, 10 |
| Web fundamentals | HTTP, cookies, same-origin policy, HTML escaping | Modules 12, 17 |
| SQL | Injection through generated queries | Module 17 |
| Container basics | Sandboxing agent tool use, hardening services | Modules 11, 12, 16 |

## Self-check

Answer these honestly. If you can do five of six without looking anything up, you are ready. If you can do fewer than three, spend a day on the refresher below — it will pay for itself in Module 04.

1. What does `x.shape` return for `x = np.zeros((3, 4))`, and what does `x[:, 1]` produce?
2. Given predictions and labels for a fraud detector that flags 1 % of transactions, why is 99 % accuracy a meaningless headline?
3. In a training loop, what happens to the loss curve when the learning rate is far too high?
4. What is the difference between a model's parameters and its hyperparameters?
5. If a function returns `None` instead of a tensor, what kind of error appears, and where?
6. Why does `import torch` fail inside a virtual environment where PyTorch is not installed, even if it works in your system Python?

??? note "Answers"

    1. `(3, 4)`, and `x[:, 1]` is a 1-D array of shape `(3,)` — the second column.
    2. Because a trivial model that always predicts "not fraud" also scores 99 %. Accuracy hides the cost of false negatives, which is usually the expensive error in fraud detection.
    3. It diverges — the loss oscillates or grows instead of falling, often producing `nan`.
    4. Parameters are learned from data (weights and biases). Hyperparameters are set before training (learning rate, batch size, architecture choices) and control how learning happens.
    5. An `AttributeError` on `None.something`, at the line where the result is used — not at the line where the function failed. This is why tracebacks must be read from the bottom up.
    6. Because virtual environments isolate installed packages; the system interpreter has its own site-packages directory.

## Refresher path

If you need to rebuild foundations, this is the shortest route:

| Need | Spend | Do this |
|---|---|---|
| Python and NumPy rust | 3–4 h | Rewrite one of your old assignments without looking at it, using only the documentation |
| ML fundamentals | 6–8 h | Re-derive a logistic regression classifier by hand, then implement it in NumPy |
| Maths for Module 04 | 4–6 h | Gradients, chain rule, and the geometric meaning of a dot product; practise with small matrices |
| Evaluation intuition | 2 h | Compute precision, recall and F1 by hand on a 20-row confusion matrix, then verify in scikit-learn |

You do not need to finish all four before starting. Module 01 requires none of them; Module 04 is where the maths begins to matter, and that is several weeks in.

## What you do not need

To save you unnecessary anxiety:

- **No security certification or prior security course.** Module 01 assumes you have never threat-modelled anything.
- **No GPU.** Every laboratory is designed to run on a laptop CPU within its stated runtime budget.
- **No paid API keys.** Language-model laboratories use small local models. Nothing in this course requires a cloud account or a credit card.
- **No cloud infrastructure.** Where a lab would normally need a cluster or a managed service, it uses a local, deliberately simplified emulation, and says so.
- **No prior exposure to LLMs.** Module 13 builds what you need, in the terms a security engineer uses.

## Hardware

| | Minimum | Comfortable |
|---|---|---|
| RAM | 8 GB | 16 GB |
| Disk | 5 GB free | 15 GB free |
| CPU | Any dual-core from the last decade | 4 cores or more |
| GPU | Not required | Optional, speeds up Modules 05–07 |
| OS | Windows 10/11, macOS 12+, or a current Linux | Any |

If your machine is older, start with Levels 1 and 3, which are lighter, and return to the model-training examples in Level 2 when you have access to a lab machine.

## Next

<div class="sas-grid sas-grid--2" markdown>

<div class="sas-card" markdown>
<div class="sas-card__title">Set up your environment</div>
Python 3.11 or 3.12, one virtual environment, one verification script.

[Continue →](environment.md)
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">Choose a study plan</div>
Full pathway, condensed semester, or a specialisation track.

[Continue →](study-plans.md)
</div>

</div>
