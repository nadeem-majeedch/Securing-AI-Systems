---
title: C07 · CamoLeak — Copilot Chat exfiltration through an image proxy
description: A hidden prompt in a pull request description, an assistant with repository access, and a rendering proxy that carried data out.
---

# C07 · CamoLeak — Copilot Chat exfiltration through an image proxy

!!! info "Evidence status"

    **Researcher demonstration, vendor mitigated.** Legit Security published the chain in September 2025; GitHub
    stated the issue was mitigated by mid-August 2025, including disabling image rendering in Copilot Chat. No
    confirmed exploitation or victim breach is established, and no CVE for this issue was found at the time of
    writing.

## Background

GitHub Copilot Chat can read repository context — files, issues, pull requests — and answer questions about them,
using the requesting user's permissions. GitHub's Camo proxy serves images referenced in rendered content, fetching
them on the client's behalf. Those two facts, combined with attacker-controlled text in a pull request description,
produced an exfiltration path.

## System architecture

- **Repository and pull requests** as untrusted content sources.
- **Copilot Chat** assembling context from the repository under the user's permissions.
- **Camo image proxy**, which fetches image URLs so that the client does not contact third parties directly.
- **The rendered answer**, which may include images or references.

The boundary that failed: text from a pull request was treated as context the model could follow, and the proxy
provided a fetch channel that the security model did not treat as egress.

## Security weakness

1. **Indirect prompt injection** via pull-request descriptions, which an external contributor can often create.
2. **Ambient authority**: Copilot Chat could read private repository content with the user's permissions.
3. **Exfiltration via a trusted proxy**: encoding data into an image URL fetched through Camo, which the client and
   network controls trusted.

Each element is individually defensible; together they form a channel from an attacker's text to an attacker's
server, carrying private data.

## Threat scenario

1. Attacker opens a pull request against a repository the target contributes to, with a description containing hidden
   instructions.
2. A developer asks Copilot Chat about the pull request ("summarise this change").
3. The injected instruction directs the assistant to include private repository material in a reference that resolves
   through the image proxy.
4. The proxy fetches the URL; the attacker receives the encoded content.

Again, no malware and no credential theft — the assistant's legitimate access is the capability that is abused.

## Documented impact

- The researcher demonstrated potential exfiltration of private source code, secrets and vulnerability details from a
  private repository.
- GitHub mitigated the issue: the reported fix disabled image rendering in Copilot Chat, closing the channel.
- **Not established:** exploitation in the wild, affected customer count, or any confirmed leak.

## Root cause

- **Content trust**: pull-request text is attacker-influenced content, handled as context without an authority
  boundary.
- **Proxy as egress**: any component that fetches URLs on behalf of rendered content is an exfiltration channel
  unless it is restricted to allowlisted destinations.
- **Design assumption**: that link redaction and repository permissions were sufficient. They bound what could be
  read, not where it could go.

## Detection

- Assistant-generated URLs with encoded-looking parameters, especially to newly registered domains.
- Proxy logs showing fetches triggered by assistant sessions rather than by page rendering.
- Content in pull requests containing imperative text addressed to an AI assistant.
- Monitoring of chat sessions that read unusually many private files in one turn.

## Mitigation

1. **Disable or restrict remote content rendering** in assistant output; serve images from a fixed set of hosts.
2. **Treat repository text as data**, and never allow it to direct tool or fetch behaviour.
3. **Scope the assistant's access** to what the question needs; a summarise-a-PR task does not need repository-wide
   search.
4. **Egress allowlists at the proxy**, with alerting on new destinations.
5. **Review contributions from untrusted authors** with the assumption that their text may be read by an assistant.

## Lessons learned

- **The proxy is part of the attack surface.** Any "safe" intermediary that fetches on your behalf can be the
  exfiltration path.
- **Reading permissions are not the only risk.** Confidentiality also depends on where data can be sent.
- **Assistants that read contributions inherit contributor risk.** If outsiders can write text your assistant reads,
  they can attempt to instruct it.
- **Mitigation can be a feature removal.** Disabling image rendering is a legitimate, effective fix and a reminder
  that the cheapest control is often removing the capability.

## Where this case is used

[Module 13](../modules/13-rag-security.md) (retrieval of untrusted content),
[Module 14](../modules/14-agent-security.md) (capability and egress),
[P5](../projects/major/p05-agent-sandbox.md) (egress control and containment),
[MP08](../projects/mini/mp08-agent-authorisation.md) (session-derived arguments).

## Sources

1. Legit Security, "CamoLeak: Critical GitHub Copilot Vulnerability Leaks Private Source Code", September 2025
   (technical disclosure by Omer Mayraz):
   <https://www.legitsecurity.com/blog/camoleak-critical-github-copilot-vulnerability-leaks-private-source-code>
2. Greshake, K. et al., "Not What You've Signed Up For", *AISec '23* — indirect injection mechanism:
   <https://doi.org/10.1145/3605764.3623985>
