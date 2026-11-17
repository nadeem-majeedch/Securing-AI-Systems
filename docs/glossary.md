---
title: Glossary
description: Definitions of the security, machine learning and generative-AI terms used throughout the course.
---

# Glossary

Every specialised term used in the course, defined once and linked from the modules. If a term in a module is not obvious, look it up here rather than guessing.

Terms are grouped by initial letter. Definitions are written for a reader who has completed Level 1; where a term has a different meaning in general security or in machine learning, the AI-security meaning is given.

## A

**Activation clustering**
:   A backdoor detection technique that clusters a model's internal-layer activations for inputs of a given class. Poisoned inputs cluster separately from clean ones because the trigger creates a distinct internal signature.

**Adversarial example**
:   An input deliberately modified — often imperceptibly — so that a model produces the attacker's chosen output. Formally, an input whose prediction differs from the true label while remaining close to a benign input under a chosen distance metric.

**Adversarial training**
:   Training a model on adversarial examples generated during training, solving a min-max problem: minimise the loss over model parameters while an inner optimiser maximises it over allowed perturbations.

**Advantage (membership)**
:   In a membership-inference attack, how much better than chance the attacker distinguishes members from non-members. True positive rate minus false positive rate is the standard measure.

**Agent (AI agent)**
:   A system in which a language model chooses and invokes tools — file access, HTTP, code execution, payments — in a loop to accomplish a goal. It inherits the union of its tools' permissions.

**AGENCY (excessive)**
:   See **Excessive agency**.

**AIMS (AI management system)**
:   A management system for AI, as specified by ISO/IEC 42001: a set of policies, roles, risk processes, controls and review activities, rather than a technical control. Certifiable as a management system, not as a secure model.

**AI RMF**
:   The NIST AI Risk Management Framework (AI 100-1, 2023), organised into four functions: Govern, Map, Measure and Manage.

**AML taxonomy**
:   NIST AI 100-2e2025, *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations*. Defines attack classes by ML method, life-cycle stage, attacker goal, objective, capability and knowledge. The shared vocabulary this course uses; the 2023 edition is superseded.

**ATLAS**
:   MITRE's Adversarial Threat Landscape for Artificial-Intelligence Systems: a knowledge base of adversary tactics and techniques against AI systems, structured like ATT&CK.

**Attribute inference**
:   Recovering a sensitive property of a training record from a model's behaviour, for example inferring a person's diagnosis from a model trained on medical records.

**Availability poisoning**
:   Poisoning whose goal is to degrade overall model performance rather than to insert a specific behaviour.

## B

**Backdoor**
:   A behaviour implanted during training that triggers on a specific pattern and is otherwise dormant, so that standard evaluation shows normal accuracy.

**BadNets**
:   The canonical backdoor attack, in which a small pixel patch is added to a fraction of training images and the labels are flipped to the target class.

**BIM (Basic Iterative Method)**
:   An iterative extension of FGSM that applies several small gradient steps, each projected back into the allowed perturbation budget.

**Black-box attack**
:   An attack with no access to model weights or gradients; the adversary observes outputs only, possibly with a query budget.

**Blended trigger**
:   A backdoor trigger applied as a faint image-wide overlay rather than a discrete patch, trading attack success for lower visibility.

**Boundary (decision boundary)**
:   The surface in input space separating regions assigned to different classes. Adversarial examples exploit the small distance from typical inputs to this surface in high dimensions.

## C

**C&W (Carlini-Wagner) attack**
:   An optimisation-based attack that searches for the smallest perturbation achieving a target classification, commonly using an L2 objective with a margin term.

**Canary set**
:   A fixed, labelled evaluation set monitored in production for quality or behaviour change. In security terms, the signal that detects a silent model or index change. Distinct from a canary token, which detects disclosure.

**Canary token**
:   A unique, monitored value placed where it should never appear. Its appearance in an outbound request or a model output is high-confidence evidence of exfiltration.

**Certified robustness**
:   A guarantee that no input within a specified norm ball around a given input can change the prediction. Stronger than empirical robustness, and narrower in scope than it sounds.

**Clean-label attack**
:   Poisoning in which the poisoned samples keep their correct labels, making label inspection useless as a defence.

**Confused deputy**
:   A pattern in which a component with authority is tricked into using that authority on behalf of a less-privileged actor. In agents, the model acts as the deputy for whoever controls its input.

**Context window**
:   The fixed-length token sequence a language model conditions on. Instructions and data share it without a privilege boundary, which is the structural origin of prompt injection.

**Cross-tenant leakage**
:   Disclosure of one customer's or organisation's data to another through a shared model, index or cache.

**Crosswalk**
:   A mapping between two frameworks, showing which requirement in one is addressed by which clause or function in the other. Lets an organisation satisfy several audiences with one control set — and exposes controls that exist in only one framework.

**CVSS**
:   The Common Vulnerability Scoring System, a standard scheme for severity. It does not natively model model-integrity or agent-authority impact, so AI findings typically combine it with additional dimensions.

## D

**Data card (dataset statement)**
:   Documentation of a dataset's origin, composition, collection method, licence and known limitations.

**Differential privacy (DP)**
:   A formal guarantee that an algorithm's output distribution changes only slightly when one individual's record is added or removed, controlled by a privacy budget, epsilon.

**DP-SGD**
:   Differentially private stochastic gradient descent: per-example gradient clipping plus calibrated noise, yielding a formally bounded privacy loss.

**Decision-based attack**
:   A black-box attack that uses only the predicted label, not confidence scores, to search for an adversarial input.

**Defence in depth**
:   Layering independent controls so that no single failure is sufficient for compromise. In LLM systems, the only defence structure that survives contact with real attackers.

**Dependency confusion**
:   A supply-chain attack in which an attacker publishes a public package under the name of a private or internal dependency, so that a resolver installs the attacker's version. The 2022 `torchtriton` incident is the course's example.

**Drift**
:   Change over time in input distribution (data drift) or in the relationship between inputs and labels (concept drift). Malicious drift is induced deliberately and is a security, not just a quality, concern.

## E

**Egress allowlist**
:   A network control permitting outbound connections only to named destinations. The control that survives injection-driven exfiltration, where the attacker chooses the URL.

**Embedding**
:   A dense vector representation of text, images or other data, positioned so that semantically similar items are close together. Embeddings are not anonymised data.

**Embedding inversion**
:   Reconstructing approximate source text or attributes from its embedding vector.

**Epsilon (perturbation budget)**
:   The maximum allowed change to an input under a chosen norm, written as the radius of an allowed ball. Different from the privacy epsilon; the shared symbol is an unfortunate coincidence.

**Epsilon (privacy budget)**
:   The parameter of a differential-privacy guarantee: smaller means stronger privacy and more added noise.

**Evasion attack**
:   An attack at inference time that causes a misclassification without altering the model.

**Evidence status**
:   In this course's case studies, the label describing what the public record supports: vendor postmortem, security advisory, researcher demonstration, court decision, or hypothetical. A demonstration is not an exploited breach.

**Excessive agency**
:   A vulnerability in which an AI system is granted permissions beyond what its function requires, so that a compromised or manipulated model can cause disproportionate harm.

**Expectation over transformation (EOT)**
:   An optimisation technique that averages an attack over a distribution of transformations, producing perturbations that survive real-world variation such as rotation, lighting or compression.

**Extraction (model extraction)**
:   Reconstructing a functionally equivalent model by querying a target API and training a surrogate on the input-output pairs.

## F

**FGSM (Fast Gradient Sign Method)**
:   A single-step attack that perturbs each input feature by epsilon in the direction that increases the loss, i.e. the sign of the input gradient.

**Fingerprinting**
:   Identifying whether a given model is a copy of another, by querying it with specially constructed inputs whose responses are characteristic.

**Fine-tuning**
:   Further training of a pretrained model on a specific dataset. A supply-chain stage: the base model, the tuning data and the adapters are all inputs you did not necessarily produce.

## G

**Govern (function)**
:   The function added to the NIST Cybersecurity Framework in version 2.0: risk strategy, roles, policy, supply-chain risk and oversight. In the AI RMF, the function covering culture, accountability and risk tolerance.

**Gradient masking**
:   A false-defence condition in which a model appears robust because gradients are unavailable, broken or uninformative, rather than because the decision boundary is genuinely far away.

**Guardrail**
:   A filter or classifier placed around a model to restrict inputs or outputs. Useful, measurable, and bypassable; never a security boundary on its own.

## H

**Hallucination**
:   A fluent but unsupported model output presented as fact. A safety and trust problem that becomes a security problem when the output drives an automated decision.

**Hash pinning**
:   Recording the cryptographic digest of an artefact and verifying it before use, so that a substituted artefact is detected.

**Human in the loop**
:   A design in which a person confirms or approves consequential actions. Effective only when placed before an irreversible action.

## I

**Indirect prompt injection**
:   Injection delivered through content the model processes — a document, web page, email, tool output or image — rather than typed by the user. The dominant realistic vector for LLM applications.

**Inference (attack)**
:   Deriving sensitive information about training data or the model itself from its behaviour. Distinct from inference as model serving, which is confusing but standard usage.

**Instruction hierarchy**
:   A class of proposed defences that attempts to privilege some instructions over others. Useful as a mitigation; not currently a reliable enforcement mechanism.

**Integrity (artefact)**
:   The property that an artefact is exactly what was approved: same bytes, same revision, same lineage. Enforced by hashing, signing and immutable storage.

## J

**ISO/IEC 42001:2023**
:   The international standard specifying requirements for an AI management system. Voluntary unless adopted by law, regulation or contract; certification audits the management system, not the model.

**Jailbreak**
:   An interaction that causes a model to produce content its safety training was intended to refuse. Related to injection but different: jailbreaks target the model's policy, injection targets the application's trust boundary.

## L

**Label flipping**
:   Poisoning by changing the labels of training samples, the simplest form of targeted attack.

**Least privilege**
:   Granting each component the minimum authority it needs for its function. For agents, applied to tools, credentials and network egress.

**LiRA (likelihood-ratio attack)**
:   A membership-inference method (Carlini et al., IEEE S&P 2022) that trains reference models to score how *likely* an observed confidence is under member and non-member hypotheses. Its importance is methodological: it made true-positive rate at low false-positive rate the standard metric.

**Lineage**
:   The recorded history of a dataset or model: where it came from, what transformed it, and what it produced.

**LLM-BOM / ML-BOM**
:   A machine-readable bill of materials for a machine-learning system: models, datasets, dependencies, licences and versions.

**l-diversity**
:   An extension of k-anonymity requiring that each equivalence class contains diverse sensitive values, mitigating homogeneity attacks.

## M

**Membership inference**
:   Determining whether a specific record was used to train a model. A privacy attack whose strength depends heavily on overfitting.

**MIA**
:   See **Membership inference**.

**Model card**
:   Documentation of a model's intended use, training data, evaluation results and limitations, published with the model.

**Model inversion**
:   Reconstructing representative inputs or attributes from a model's outputs, particularly when confidence scores are exposed.

**Model registry**
:   A versioned store of model artefacts with metadata, enabling controlled promotion from staging to production.

## N

**NIST AI 600-1**
:   The Generative AI Profile (2024) of the NIST AI Risk Management Framework, cataloguing risks specific to generative systems.

**NIST CSF 2.0**
:   The NIST Cybersecurity Framework, CSWP 29 (2024), organised into six functions: Govern, Identify, Protect, Detect, Respond, Recover. Voluntary, not AI-specific, and the natural home for AI risk inside an existing cyber programme.

**Non-determinism**
:   Variation in output across identical runs, caused by sampling, parallel floating-point reduction, or hardware differences. A reason security results require repeated trials.

## O

**OWASP LLM Top 10**
:   A community list of the most significant application-security risks for large language model systems. A useful checklist, not a completeness claim.

**OWASP ML Top 10**
:   The equivalent list for classical machine-learning systems, covering data poisoning, supply chain, model evasion and related categories.

## P

**PGD (Projected Gradient Descent)**
:   An iterative attack that takes gradient steps and projects the result back into the allowed perturbation ball after each step. Also the inner loop of adversarial training.

**Pickle**
:   Python's serialisation format, which can encode arbitrary object construction. Loading an untrusted pickle is arbitrary code execution, by design rather than by defect.

**Poisoning**
:   Corrupting training data or the training process so that the resulting model behaves as the attacker wants.

**Prevalence (alerting)**
:   The proportion of events in a stream that are genuinely malicious. Together with a detector's false-positive rate it determines alert precision: at low prevalence, even a good detector produces mostly false alerts.

**Prompt injection**
:   Causing a model to follow instructions supplied as data. Direct when typed by the user; indirect when embedded in processed content. Structural, not an implementation bug.

**Prompt leaking**
:   Eliciting the application's hidden system prompt or instructions through conversation. A disclosure failure distinct from instruction following: fixing leakage does not stop an injected document from influencing behaviour.

**Provenance**
:   The verifiable origin and chain of custody of an artefact. Distinct from lineage, which records transformation history.

## Q

**Query budget**
:   The number of model queries an attacker is willing or able to spend. A key parameter in extraction, black-box evasion and membership-inference attacks.

## R

**RAG (retrieval-augmented generation)**
:   An architecture that retrieves documents from an index and places them in the model's context to ground its answer. Introduces an access-control boundary at retrieval.

**Randomised smoothing**
:   A certified defence that classifies by majority vote over many noisy copies of the input, yielding a provable radius within which the prediction cannot change.

**Red teaming**
:   Adversarial testing of a system under an agreed scope, intended to find and prioritise weaknesses before an attacker does.

**Release gate**
:   A checkpoint in a pipeline that blocks promotion unless named evidence exists: verified digests, passed evaluation thresholds, no plaintext credentials, a tested rollback. Not a meeting — a check that fails closed.

**Residual risk**
:   The risk that remains after controls are applied. Every honest security statement ends here rather than at "secure".

**Robust overfitting**
:   The phenomenon in which adversarially trained models perform worse on held-out adversarial examples as training progresses, despite improving on the training attack.

**RAG poisoning**
:   Inserting malicious or misleading documents into a retrieval corpus so that the model cites or repeats them.

## S

**Sandbox**
:   An isolated execution environment limiting what code or an agent can do: filesystem, network egress, syscalls and resources.

**SBOM**
:   Software bill of materials: a machine-readable inventory of components and their versions.

**Source of truth**
:   The authoritative record a system's answers must agree with. When an assistant and a policy page disagree, the absence of a single source of truth is the defect — the lesson of the Air Canada decision.

**Spectral signature**
:   A detection method for poisoning that examines the spectrum of the training-data covariance, where poisoned samples appear as an anomalous direction.

**Split-view poisoning**
:   A dataset-poisoning technique (Carlini et al., IEEE S&P 2024) exploiting the gap between a snapshot a maintainer audits and a later download that resolves mutable references, so the attacker's content reaches training without appearing in the audited snapshot.

**Spotlighting**
:   Marking untrusted content in a prompt so the model can be instructed to treat it as data. A mitigation, not an enforcement boundary.

**SSDF**
:   The NIST Secure Software Development Framework, SP 800-218 v1.1 (2022), with four practice groups: Prepare the Organization, Protect the Software, Produce Well-Secured Software, Respond to Vulnerabilities. SP 800-218A (2024) adds a generative-AI community profile.

**STRIDE**
:   A threat-modelling mnemonic: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege.

**Supply chain (ML)**
:   The set of external inputs to an ML system: datasets, base models, tokenisers, plugins, adapters, container images and dependencies.

**System prompt**
:   Instructions prepended by the application to shape model behaviour. A convention, not a permission boundary, and never a place to store a secret.

**System card**
:   Documentation of a deployed AI system as a whole: purpose, users, data, model, controls, evaluation and known limitations.

## T

**Targeted attack**
:   An attack aiming at a specific chosen output class, as opposed to any misclassification.

**Threat model**
:   A structured description of what is being protected, from whom, with what capability, and what would count as a breach. The input to every control decision.

**Transferability**
:   The property that adversarial examples generated against one model often fool another trained on similar data, enabling attacks without access to the target.

**Trigger**
:   The pattern that activates a backdoor, such as a specific patch, phrase or sender.

**`trust_remote_code`**
:   A flag permitting a model repository to supply and execute its own Python code. It converts a model download into code execution from an untrusted source.

## U

**Unbounded consumption**
:   An AI-specific denial-of-service and cost risk in which attacker-controlled inputs cause disproportionate computation or spend.

**Untrusted output**
:   The principle that everything a model produces must be treated as attacker-influenced input to whatever consumes it next.

## V

**Vector database**
:   A store optimised for nearest-neighbour search over embeddings, with metadata filters. Its filters are only an access control if enforced server-side against the requester's identity.

**Verification (artefact)**
:   Checking an artefact against a recorded hash or signature before use.

## W

**Voluntary (framework status)**
:   The default status of NIST, ISO/IEC and OWASP material: guidance an organisation may adopt. It becomes binding only through law, regulation, contract or self-adopted policy. The EU AI Act is the course's example of the binding instrument.

**Watermark (model)**
:   A deliberate, hidden behaviour embedded in a model to support ownership claims. Evidence of provenance, not proof of ownership.

**White-box attack**
:   An attack with full access to model architecture and weights, and therefore to gradients.

## Z

**Zero-day (in this context)**
:   A weakness with no available fix at the time of disclosure. In AI systems, most prompt-injection variants behave this way by construction rather than by oversight.

---

!!! tip "Missing a term?"

    If you meet a term in a module that is not here, that is a defect in the course. It is worth reporting, because the glossary is checked against the modules during review.

    See also: [References](references.md) for primary sources, and [How to use this course](getting-started/how-to-use.md) for the interface conventions.
