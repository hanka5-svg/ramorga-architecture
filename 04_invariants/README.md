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

## Related Documents

- [Field Engine](../02_field_engine/README.md)
- [Meniscus Engine](../03_meniscus_engine/README.md)
- [Pipeline](../pipeline/README.md)
