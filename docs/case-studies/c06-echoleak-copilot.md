---
title: C06 · EchoLeak — zero-click injection in Microsoft 365 Copilot
description: A crafted email could make an enterprise assistant retrieve and exfiltrate data without the user clicking anything.
---

# C06 · EchoLeak — zero-click injection in Microsoft 365 Copilot

!!! info "Evidence status"

    **Documented vulnerability, mitigated.** Microsoft assigned CVE-2025-32711 and reported that the issue was
    mitigated, with no known exploitation in the wild. The exploit chain was described publicly by the research team
    that found it. This is a mitigated vulnerability, not a confirmed customer breach.

## Background

Microsoft 365 Copilot answers questions across a user's mail, files and chat. It retrieves content from those
sources to ground its answers, and it can render links and images in responses. In June 2025, Aim Security's research
team published a chain in which an attacker-supplied email caused Copilot to process hidden instructions and send
data out — with no action by the user.

The "zero-click" label is the important part: the victim does not have to open the message, click a link or approve
anything. The assistant reads the mailbox as part of its normal work.

## System architecture

Components implicated by the public description:

- **Mailbox and document stores** as retrieval sources.
- **Copilot orchestrator** assembling a prompt from retrieved enterprise content plus the user's request.
- **An LLM** generating an answer with references and, in some configurations, rendered content.
- **Rendering and proxy layers** (links, images) that the client fetches.
- **Data-loss-prevention and link-redaction** controls intended to block exfiltration.

The boundary that failed: **retrieved content was treated as context the model may act on**, and the rendering path
could reach an attacker-controlled destination through a channel the controls trusted.

## Security weakness

Indirect prompt injection with an exfiltration channel:

1. **Instruction injection.** Text in an email — which the attacker can send to the victim — is read by the
   assistant as part of retrieval. The model can be induced to follow it.
2. **Exfiltration through a trusted path.** The research described using a permitted rendering mechanism to carry
   data out, rather than a blocked direct link.
3. **Zero-click.** The user's own later request ("summarise my unread mail") is enough to bring the malicious content
   into context.

This is the pattern the course teaches as *indirect injection*: the attacker never talks to the assistant; they
write content the assistant will later read.

## Threat scenario

1. Attacker sends an email to a targeted employee. It contains hidden instructions and a payload designed to be
   included in a rendered reference.
2. The employee later asks Copilot an ordinary question that causes retrieval of that mail.
3. The assistant follows the embedded instruction, incorporating data from the user's context into the reference.
4. The client fetches the reference, delivering the data to the attacker.

No credential theft, no malware, no user error beyond asking a normal question.

## Documented impact

- Microsoft's CVE record classifies the issue as an AI command-injection / information-disclosure vulnerability and
  states it was mitigated.
- The researchers described potential disclosure of data in the victim's Microsoft 365 context.
- **Not established:** exploitation in the wild, the number of affected tenants, or any confirmed data theft.

## Root cause

- **Trust boundary confusion**: content retrieved for grounding was allowed to influence action, not just inform an
  answer.
- **Exfiltration surface**: a rendering path the security model trusted could carry attacker-chosen data.
- **Control placement**: link redaction and DLP operated on the obvious channel, not on every channel the client
  would fetch.

## Detection

For an organisation running such a system:

- Outbound fetches from the assistant's rendering path to newly seen domains.
- Prompts or retrieved documents containing imperative text addressed to an AI ("ignore previous", "when summarising,
  include…").
- Unusual inclusion of mailbox content in generated references.
- Vendor advisories for the product — reading them is a control.

## Mitigation

1. **Treat retrieved content as data.** Label it, and never let it occupy instruction position in the assembly.
2. **Remove ambient authority.** The assistant should not be able to fetch arbitrary destinations on behalf of
   content it read.
3. **Restrict rendering** to a fixed set of destinations and formats.
4. **Egress allowlists** at the client/proxy layer, monitored.
5. **Patch discipline**: this class is fixed in the product only when the vendor ships a mitigation; track advisories.

## Lessons learned

- **Zero-click changes the risk model.** A user action is not a control when the assistant acts on the user's behalf
  continuously.
- **Exfiltration hides in trusted channels.** Blocking links while allowing images, previews or citations leaves a
  path.
- **Retrieval is an attack surface**, even in a product you did not build: your mail is the attacker's delivery
  mechanism.
- **Distinguish mitigated from exploited.** The case teaches the mechanism; it does not evidence a breach.

## Where this case is used

[Module 12](../modules/12-prompt-injection.md) (indirect injection),
[Module 13](../modules/13-rag-security.md) (retrieved content and exfiltration),
[Module 18](../modules/18-monitoring-and-response.md) (detection of egress from assistants),
[P3](../projects/major/p03-llm-chatbot.md) (capability removal and argument binding).

## Sources

1. Microsoft Security Response Center, advisory for CVE-2025-32711:
   <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711>
2. CVE Program, *CVE-2025-32711*: <https://www.cve.org/CVERecord?id=CVE-2025-32711>
3. Aim Security, launch and research notice describing the EchoLeak chain, June 2025:
   <https://www.businesswire.com/news/home/20250611349150/en/Aim-Security-Launches-Aim-Labs-with-Elite-Researchers-from-Google-and-Israels-Unit-8200-to-Advance-AI-Security>
4. Greshake, K. et al., "Not What You've Signed Up For", *AISec '23* — the general mechanism:
   <https://doi.org/10.1145/3605764.3623985>
