---
title: Privacy
description: What this course stores about you, what it does not, and how to remove the one thing it keeps.
---

# Privacy

Short version: **the course knows nothing about you.** It has no accounts, no analytics, no tracking cookies, no telemetry and no server that records a visit. The only data it stores is a completion date you choose to record, kept in your own browser.

This page states that precisely, because a privacy claim is only worth something if you can check it.

## 1. What is stored

One thing, and only if you press a button:

| What | Where | Why | Who can see it |
|---|---|---|---|
| The fact that you marked a module complete, with the date | Your browser's `localStorage`, key `sas.progress.v1` | So the roadmap can show your progress when you come back | You, in that browser, on that device. Nobody else |

That is the complete list. Nothing is sent anywhere: the script that writes it (`docs/assets/javascript/progress.js`) makes no network request of any kind.

**What is not collected:** name, email, student number, IP-based profiles, device fingerprints, behaviour analytics, quiz answers, laboratory results, reading time, or anything else about you. There is no form on this site that submits to a server. The search index is downloaded once and searched in your browser.

## 2. No accounts, no trackers, no third-party requests

| Mechanism | Used? | Detail |
|---|---|---|
| User accounts or login | **No** | No authentication exists on the site |
| Cookies for tracking | **No** | The site sets no cookies of its own |
| Analytics (Google Analytics, Plausible, Matomo, Umami, …) | **No** | No analytics script is installed |
| Advertising, tag managers, session recording, heatmaps | **No** | None present |
| Error monitoring that identifies visitors | **No** | None present |
| Content delivery networks for fonts or libraries | **No** | Fonts are your system's own. Mermaid, the only third-party runtime library, is served from this site, not a CDN |
| Embedded video, maps or social widgets | **No** | None embedded |

The one third-party component is the vendored Mermaid library, stored in this repository and served from the same site. It renders diagrams locally; it contacts nothing.

**Why this matters beyond convenience.** The course is about surveillance, data minimisation and supply-chain trust. A course that tracked its readers while teaching data minimisation would be teaching one thing and doing another.

## 3. What the course cannot control

Being honest about the boundary:

- **Your host or university network** may log the pages you request at the server or proxy level, as any website visit is logged. That is outside this course, and governed by that organisation's policy.
- **A learning-management-system wrapper** or an institutional portal that displays this material may have its own analytics. That is the institution's processing, not the course's.
- **Your browser or extensions** may keep history, caches or synchronised profiles.
- **If you are studying for credit**, your institution holds your enrolment and assessment records. Nothing in this course adds to them.

## 4. Removing the stored data

Delete the one key, or clear site data:

```javascript
// In the browser console on any page of the course
localStorage.removeItem('sas.progress.v1')
```

Or use your browser's "clear cookies and site data" for this site. Nothing else is stored, so nothing else needs clearing. Private or incognito windows keep the data only for the session — the completion marker will still work while the window is open.

## 5. Your laboratory work

The course does not see your notebooks, your results or your reports. They live on your machine.

Two things worth remembering anyway, because they are your privacy, not the course's:

- **Never put real personal data in a notebook.** Use the synthetic datasets in `labs/datasets/` or regenerate them. A notebook that contains a real record is a data-protection problem even if you never publish it.
- **Decide before you share.** If you publish your portfolio on GitHub, check what is committed: outputs, logs, dataset copies and screenshots can carry information you did not intend to share. [Academic integrity and responsible use](academic-integrity.md) §5 covers the handling rules.

## 6. Children and consent

The course is written for undergraduate students and assumes adult learners. It collects no personal data from anyone, so there is no consent mechanism to trigger — and no minimum age gate, because there is nothing to process.

## 7. Changes to this page

If anything here ever changes — for example if an institution asks for an optional feedback form — this page changes in the same release, `CHANGELOG.md` records it, and the change appears in the repository history. A privacy statement that can change silently is not a privacy statement.

Questions about privacy, or about the one stored key, go to the instructor of record through the Department of Data Science (PUCIT), University of the Punjab.

---

*Related: [Academic integrity and responsible use](academic-integrity.md) · [Credits and attribution](../attribution.md) · the repository's `SECURITY.md` for reporting a privacy defect in the site.*
