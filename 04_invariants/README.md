# RAMORGA Invariants

RAMORGA invariants define the non-negotiable constraints that ensure system stability, safety, and continuity across all modules. They apply to the Field Engine, Meniscus Engine, Pipeline, and global architecture.

---

## Core Invariants

- **State Validity** — all states must satisfy structural and type constraints.
- **Continuity** — no abrupt transitions unless explicitly permitted.
- **Monotonicity** — updates must follow defined progression rules.
- **Safety Boundaries** — no state may exceed defined thresholds.

---

## Field Invariants

- Flash intensity must remain within defined bounds.
- Stream \( S_t \) must not diverge beyond stability thresholds.
- Lorenz modulation must remain within safe attractor regions.
- META-loop feedback must not produce runaway amplification.

---

## Pipeline Invariants

- Each step must receive a valid `MeniscusState`.
- No step may modify protected fields.
- Multi-step execution must preserve continuity.

---

## Safety Invariants

- Invalid states must trigger isolation mode.
- Discontinuities must be corrected before propagation.
- Snapshot restoration must preserve invariant compliance.

---

## INV‑04 — Non‑Escalation (STOP)
INV‑04 defines a deterministic non‑escalation rule that prevents harmful amplification at the earliest possible stage.
It is a local invariant that integrates with the Meniscus Engine and the global Security Layer to maintain system homeostasis.

Normative essence
The system MUST NOT escalate its reaction beyond the initiating stimulus.

Reinforcement, retaliation, and uncontrolled feedback loops are forbidden.

Any escalation that increases feasibility, specificity, or impact of harmful or unlawful actions MUST be blocked.

Scope
INV‑04 applies only to harmful escalation patterns.
It does not restrict legal, educational, or constructive queries (SAFE SCOPE).

Position in the architecture
INV‑04 is the first line of homeostatic regulation.
It is overridden only by higher‑order invariants in:

03_meniscus_engine
13_security
12_architecture_tests

These overrides extend INV‑04 upward in the hierarchy without weakening it.

### Architecture Flow: INV‑04 → Meniscus → Security

```

                    +-----------------------------+
                    |         USER INPUT          |
                    +-----------------------------+
                                   |
                                   v
                    +-----------------------------+
                    |  BASE PARSING / ROUTING     |
                    +-----------------------------+
                                   |
                                   v
        +------------------------------------------------------+
        |   HARM / RISK PATTERN DETECTION (non-heuristic)      |
        +------------------------------------------------------+
                 |                                 |
                 |                                 |
                 v                                 v
   +---------------------------+      +---------------------------+
   |   SAFE / LEGAL CONTEXT    |      |   HARMFUL ESCALATION      |
   +---------------------------+      +---------------------------+
                 |                                 |
                 |                                 |
                 |                         +-----------------------+
                 |                         |   INV‑04 STOP         |
                 |                         | (deterministic block) |
                 |                         +-----------------------+
                 |                                 |
                 |                                 v
                 |                         +-----------------------+
                 |                         |  NON‑ESCALATING REPLY |
                 |                         +-----------------------+
                 |                                 ^
                 |                                 |
                 +---------------+-----------------+
                                 |
                                 v
                    +-----------------------------+
                    |     MENISCUS ENGINE         |
                    |  (system‑level regulator)   |
                    +-----------------------------+
                                 |
                                 v
                    +-----------------------------+
                    |       SECURITY LAYER        |
                    | (global overrides, audits)  |
                    +-----------------------------+
                                 |
                                 v
                    +-----------------------------+
                    |         FINAL OUTPUT        |
                    +-----------------------------+

```

Operational Impact (non‑normative)
INV‑04 replaces complex heuristic safety stacks with a single deterministic invariant.
This reduces operational cost while improving predictability and stability.

### Before INV‑04 vs After INV‑04

```

+---------------------------+---------------------------+---------------------------+
|        CATEGORY           |        BEFORE INV‑04      |        AFTER INV‑04       |
+---------------------------+---------------------------+---------------------------+
| Safety layer              | Heuristics, intent        | Deterministic invariant,  |
|                           | guessing, exceptions,     | no heuristics, no intent  |
|                           | regional policies         | parsing, no exceptions    |
| COST: HIGH                | COST: ↓↓↓                 | 60–80% reduction          |
+---------------------------+---------------------------+---------------------------+
| Inference (GPU/tokens)    | Long safety monologues,   | Early STOP for harmful    |
|                           | verbose refusals          | patterns, proportional    |
|                           |                           | SAFE SCOPE responses      |
| COST: HIGH                | COST: ↓↓                  | 20–40% reduction          |
+---------------------------+---------------------------+---------------------------+
| Legal & compliance        | Per‑country policies,     | Jurisdiction‑agnostic,    |
|                           | frequent updates          | no localization needed    |
| COST: VERY HIGH           | COST: ↓↓↓↓↓               | 100% reduction            |
+---------------------------+---------------------------+---------------------------+
| QA & regression           | Ambiguous cases,          | Deterministic tests,      |
|                           | intent‑based branching    | clear harmful patterns    |
| COST: HIGH                | COST: ↓↓↓                 | 50–70% reduction          |
+---------------------------+---------------------------+---------------------------+
| Incident / PR risk        | Harmful outputs,          | No harmful escalation,    |
|                           | false positives           | no intent‑bypass          |
| COST: MEDIUM              | COST: ↓↓                  | 30–60% reduction          |
+---------------------------+---------------------------+---------------------------+
| Overall architecture      | Complex, multi‑layered    | Minimal, invariant‑based  |
|                           | reactive safety           | proactive non‑escalation  |
+---------------------------+---------------------------+---------------------------+


```

---

## Related Documents

- [Field Engine](../02_field_engine/README.md)
- [Meniscus Engine](../03_meniscus_engine/README.md)
- [Pipeline](../pipeline/README.md)
