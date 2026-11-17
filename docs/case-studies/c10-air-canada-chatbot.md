---
title: C10 · Air Canada chatbot liability
description: A tribunal held an airline responsible for its website chatbot's incorrect statement — an accountability case, not a security incident.
---

# C10 · Air Canada chatbot liability

!!! info "Evidence status"

    **Documented legal decision.** *Moffatt v. Air Canada*, 2024 BCCRT 149, British Columbia Civil Resolution
    Tribunal, decided 14 February 2024. This is not a security incident: no system was compromised. It is included
    because it is the clearest public example of an organisation being held accountable for what its assistant said.

## Background

A passenger asked Air Canada's website chatbot about bereavement fares. The chatbot stated that a customer could
apply for a reduced fare within 90 days of travel, and linked to a page describing the bereavement policy. The
passenger later applied and was refused; the airline's position included the argument that the chatbot was a separate
entity responsible for its own actions.

The tribunal rejected that argument and found the airline responsible for the information on its website.

## System architecture

As described in the decision:

- A **chatbot** on the airline's website, presented as a source of information about policies.
- A **linked policy page** containing the actual bereavement terms.
- **Human customer-service channels** that did not know about, or follow, the chatbot's statement.

The relevant boundary is organisational: the assistant, the policy page and the human agents were not one system of
record.

## Security weakness

Not a vulnerability in the technical sense. The failure was **accuracy and accountability**:

- The assistant produced a statement inconsistent with the governing policy.
- No mechanism reconciled the assistant's answer with the authoritative document.
- The organisation's response treated the assistant as outside its responsibility.

In security terms this is closest to *integrity of information* and *governance*: the system of record was not the
system that answered.

## Threat scenario

The teaching inversion: here the "threat" is an ordinary user asking a normal question. No attacker is required. The
failure mode — a confident, wrong answer delivered with institutional authority — is the one that matters most for
most deployments.

A security-flavoured variant: an attacker who can influence the assistant's knowledge source (a poisoned FAQ, an
injected document) can produce the same outcome deliberately.

## Documented impact

- The tribunal ordered the airline to pay damages, fees and interest totalling approximately **CA$812** — small in
  money, significant in precedent.
- The decision establishes, in this jurisdiction, that a business is responsible for information its website
  provides, including through a chatbot.

The amount is not the lesson. The finding of responsibility is.

## Root cause

1. **No single source of truth.** The assistant's answer and the policy page disagreed, and nothing detected the
   disagreement.
2. **No escalation path.** The chatbot could not hand an unresolved policy question to a human with authority.
3. **Governance gap.** The organisation had no owner accountable for the assistant's statements.

## Detection

- **Answer auditing against authoritative content**: sample assistant answers and check them against the policy
  corpus.
- **User feedback loops** that reach an owner, not a void.
- **Discrepancy monitoring**: when the assistant cites a page, verify the claim is supported by that page.
- Complaints analysis: repeated questions about the same policy signal an assistant failure.

## Mitigation

1. **Ground answers in the authoritative corpus** and cite the passage; refuse when the corpus does not answer.
2. **Prohibit commitments** the assistant cannot make: pricing, eligibility, exceptions.
3. **Escalate** when confidence is low or the question is about entitlements.
4. **Assign an owner** for assistant content, with a review cycle tied to policy changes.
5. **Test policy changes against the assistant** — a policy update that does not update the assistant is a defect.

## Lessons learned

- **"The chatbot said it" is the organisation speaking.** Disclaimers do not transfer responsibility in the cases
  that have been decided so far.
- **Accuracy is a security property** for assistants that make commitments; it belongs in the risk register with
  integrity risks, not only in a quality backlog.
- **The system of record must be the system that answers**, or the gap becomes liability.
- **Cheap incidents teach expensive lessons.** A CA$812 judgment is a gift compared with a mis-stated safety or
  medical policy.

## Where this case is used

[Module 11](../modules/11-llm-security.md) (assistant failure modes),
[Module 19](../modules/19-governance-and-ethics.md) (accountability and assurance),
[Module 20](../modules/20-deployment-and-capstone.md) (launch decisions), [P3](../projects/major/p03-llm-chatbot.md)
(grounding and refusal).

## Sources

1. *Moffatt v. Air Canada*, 2024 BCCRT 149 (CanLII), British Columbia Civil Resolution Tribunal, 14 February 2024:
   <https://www.canlii.org/en/bc/bc-crt/doc/2024/2024bccrt149/2024bccrt149.html>
2. British Columbia Civil Resolution Tribunal, decision summary page for the same matter:
   <https://decisions.civilresolutionbc.ca/crt/crtd/en/item/525448/index.do>
