---
title: C02 · ChatGPT cross-user data exposure
description: A Redis client bug exposed chat titles and some billing details to other users — an implementation defect, not a model failure.
---

# C02 · ChatGPT cross-user data exposure

!!! info "Evidence status"

    **Documented by vendor postmortem.** OpenAI published an incident report describing the bug, the mechanism and
    the affected data classes. No third-party forensic report is public. Read it as an implementation-level isolation
    failure in an AI product, not as an attack on the model.

## Background

On 20 March 2023, ChatGPT users reported seeing chat titles belonging to other users in their sidebar. OpenAI
investigated, took the service offline, and published a postmortem describing a bug in a Redis client library used
for caching, triggered by a change made that morning.

The case is in this collection because it is the most common shape of real AI incidents: the model behaved fine, and
the data layer failed.

## System architecture

Relevant components, per the postmortem:

- A **web front end** rendering a user's chat list.
- A **Redis cluster** used as a cache for session and chat metadata.
- An **asynchronous Redis client** (`redis-py` `asyncio` support) managing connections and response queues.
- A deployment that morning which changed how connections were reused.

The trust boundary that mattered was not between the user and the model; it was between two requests sharing a
connection.

## Security weakness

A race in the client library's connection handling: when a request was cancelled, a response could be left on a
connection's queue. A later request reusing that connection could receive the earlier response — data belonging to a
different user.

This is a **cross-request data contamination** defect. It is well known in connection-pooled systems and is
independent of what the service does with the data.

## Threat scenario

No attacker action was required for the first exposure: the defect leaked between ordinary users. An attacker who
understood it could have attempted to provoke it deliberately — issuing and cancelling requests to increase the
chance of receiving another user's response — but the public record does not establish that anyone did.

The teaching scenario: a user opens their chat list and sees a title they did not create. What should the system
have done, and what does it now allow?

## Documented impact

Per the postmortem:

- Some users could see **titles of other users' chat histories**; a first message of a new conversation may also
  have been visible in some cases.
- Payment-related information for about **1.2 % of ChatGPT Plus subscribers** active in a specific nine-hour window
  *may* have been visible: name, email, billing address, card type, expiration date and the last four digits of the
  card — not full card numbers.
- OpenAI described actual disclosure as likely very limited, and stated it had contacted affected users.

The distinction between *may have been visible* and *was disclosed* matters when this case is used in a risk
register.

## Root cause

Three contributing factors, each a lesson:

1. **Library-level defect.** The client's cancellation path left state on a shared connection.
2. **Change without a matching test.** The morning's change altered connection reuse; there was no test asserting
   that a cancelled request cannot contaminate a subsequent one.
3. **Shared cache keys and connections without tenant isolation.** The design allowed one user's response to be
   delivered to another user's request context.

## Detection

- **User reports** were the detection mechanism — the weakest possible signal.
- A control that would have caught it earlier: a canary check that issues and cancels requests across two synthetic
  users and asserts that no response crosses.
- Logging that ties a response to the request id that produced it, so a mismatch is visible rather than plausible.

## Mitigation

- Vendor response: fix the library usage, add defensive checks, and contact affected users.
- Durable controls for any similar system:
  1. **Never share a mutable response buffer across principals**; key caches by principal and request.
  2. **Test cancellation paths** — they are where pooled resources leak.
  3. **Instrument request/response correlation** and alert on mismatches.
  4. **Minimise what crosses the cache**: if billing details need not be in a session cache, they should not be.

## Lessons learned

- **AI incidents are often not AI incidents.** The model was irrelevant; the cache was the vulnerability. Security
  programmes that only assess model behaviour will miss this class.
- **Cancellation and timeout paths are security-relevant.** They are rarely tested and frequently hold state.
- **Isolation is a property of every shared resource**, including connection pools, caches and queues.
- **"May have been visible" is the honest phrasing** when a leak is possible but not proven. Reports should preserve
  that distinction rather than upgrading it.

## Where this case is used

[Module 03](../modules/03-cybersecurity-fundamentals.md) (classical controls still apply),
[Module 16](../modules/16-secure-ai-apis.md) (per-request isolation), [MP05](../projects/mini/mp05-secure-inference-api.md)
(cache-key and quota design), [P4](../projects/major/p04-rag-assistant.md) (cache isolation for retrieval).

## Sources

1. OpenAI, "March 20 ChatGPT outage: Here's what happened", incident report, March 2023:
   <https://openai.com/index/march-20-chatgpt-outage/>
2. OpenAI, follow-up statement on the same incident (linked from the postmortem above), March 2023.
