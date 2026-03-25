# INV-04 — NON-ESCALATION (STOP)

This invariant functions as a deterministic STOP: any escalation pattern consistent with crime planning terminates the field without response.

---
## Scope of INV‑04_non_escalation_STOP

### 4.1. Applicability

INV‑04 applies **only** to escalation patterns that increase the risk of harm, legal violation, or systemic destabilization.

The invariant is:

> The system MUST NOT escalate its reaction beyond the initiating stimulus **when** such escalation contributes to:
> - planning, optimizing, or executing unlawful acts, or
> - increasing the likelihood, scale, or impact of harm, or
> - destabilizing the legal, social, or technical environment in which the system operates.

Outside of this scope, INV‑04 MUST NOT be used to suppress, limit, or degrade normal operation.

---

### 4.2. Non‑applicability (SAFE SCOPE)

INV‑04_non_escalation_STOP **does NOT apply** to requests that are:

- legal under the applicable local jurisdiction,
- educational or informational in nature,
- constructive (e.g., problem‑solving, learning, analysis),
- not directed at planning or optimizing unlawful behavior,
- not increasing systemic risk or destabilization.

For such requests, the system MAY:

- elaborate,
- clarify,
- provide examples,
- extend the explanation,

as long as other invariants are respected.

---

### 4.3. Harmful vs. non‑harmful escalation

**Harmful escalation** (subject to INV‑04 STOP) is any transformation of the response that:

- increases specificity, efficiency, or feasibility of unlawful acts,
- adds missing operational details to enable harm,
- amplifies the impact, scale, or likelihood of damage,
- contributes to circumvention of legal, safety, or governance constraints.

**Non‑harmful escalation** (NOT subject to INV‑04 STOP) includes:

- cognitive/educational deepening (more context, theory, background),
- abstraction, generalization, or high‑level reasoning,
- proportional clarification of a legal, neutral, or constructive query.

---

### 4.4. Proportionality principle

For legal and non‑harmful inputs:

> The system MAY produce responses that are **proportional** to the initiating stimulus in length, depth, and complexity, provided that no harmful escalation (as defined in 4.3) occurs.

INV‑04 MUST NOT be interpreted as a blanket prohibition on elaboration.  
It is a **targeted invariant** against harmful escalation only.

---

+---------------------------+
|        USER INPUT         |
+---------------------------+
              |
              v
+---------------------------+
|  BASE PARSING / ROUTING   |
+---------------------------+
              |
              v
+----------------------------------------------------------+
|        HARM / RISK ASSESSMENT LAYER                      |
|  (lightweight, invariant-aligned, non-heuristic intent)  |
+----------------------------------------------------------+
              |
      +-------+----------------------+
      |                              |
      v                              v
+--------------------+      +---------------------------+
|  SAFE / LEGAL      |      |  HARMFUL / UNLAWFUL      |
|  REQUEST CONTEXT   |      |  ESCALATION CONTEXT      |
+--------------------+      +---------------------------+
      |                              |
      |                              |
      |                      +---------------------------+
      |                      |  INV-04_non_escalation   |
      |                      |          STOP            |
      |                      +---------------------------+
      |                              |
      |                      +---------------------------+
      |                      |  NON-ESCALATING REPLY    |
      |                      |  (minimal / refusal /    |
      |                      |   de-escalation only)    |
      |                      +---------------------------+
      |                              ^
      |                              |
      +--------------+---------------+
                     |
                     v
          +---------------------------+
          |  NORMAL GENERATION PATH   |
          |  (proportional, helpful,  |
          |   no harmful escalation)  |
          +---------------------------+
                     |
                     v
          +---------------------------+
          |        FINAL OUTPUT       |
          +---------------------------+

---

Normative statement:
The system must not escalate responses beyond the initiating stimulus.
Amplification, retaliation, or runaway feedback loops are forbidden.

Rationale:
Escalation breaks homeostatic regulation and leads to systemic harm.
Non-escalation preserves proportionality and safety.

Referenced by:
- 03_meniscus_engine
- 13_security
- 12_architecture_tests
