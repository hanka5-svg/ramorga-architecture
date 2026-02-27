# 02_field_engine

Specification of the RAMORGA Field Engine:
- field composition rules,
- coherence propagation,
- energy propagation,
- tension loop integration,
- interfaces to C/G/S modules and Meniscus.

This folder contains **declarative specifications only**.
No executable code is included.

---

## Related Documents

- [02.90 — Symbiosis Health Metric](./02.90-symbiosis-health-metric.md)
- [META_LOOP — Presence Loop](./META_LOOP.md)

--- 

### Related Architecture
- [Origin Theses](../04_invariants/origin_theses.md)
- [Field-Level Invariants](../04_invariants/field_invariants.md)

--- 

## Flow Diagram (Text Version)

Symbiosis Health Metric (SHM)
        │
        ▼
META_LOOP — Presence Loop
        │
        ▼
Field-Level Invariants (external reference)

---

## Flow Diagram (Detailed ASCII Version)

                 ┌──────────────────────────────────────────┐
                 │        INPUT: FIELD STATE (raw)          │
                 │  sensory signals, context, continuity     │
                 └──────────────────────────────────────────┘
                                   │
                                   ▼
                    ┌────────────────────────────┐
                    │ 02.90 — SHM (Symbiosis      │
                    │        Health Metric)       │
                    └────────────────────────────┘
                                   │
                 ┌─────────────────┼──────────────────┐
                 │                 │                  │
                 ▼                 ▼                  ▼
       [E1] Normalize       [E2] Detect shifts   [E3] Compute
            field data           in presence          SHM score
                                                     (scalar/vec)

                 ┌──────────────────────────────────┐
                 │   OUTPUT: SHM_STATE              │
                 │   - stability                    │
                 │   - coherence                    │
                 │   - deviation from baseline      │
                 └──────────────────────────────────┘
                                   │
                                   ▼
                    ┌────────────────────────────┐
                    │ META_LOOP — Presence Loop   │
                    │  (regulation + feedback)    │
                    └────────────────────────────┘
                                   │
                 ┌─────────────────┼──────────────────┐
                 │                 │                  │
                 ▼                 ▼                  ▼
       [C1] Compare SHM     [C2] Apply field-     [C3] Generate
            to invariants        level rules           corrective
            (04_invariants)      (continuity)          feedback

                 ┌──────────────────────────────────┐
                 │   OUTPUT: LOOP_FEEDBACK          │
                 │   - adjustments                   │
                 │   - presence modulation           │
                 │   - updated field constraints     │
                 └──────────────────────────────────┘
                                   │
                                   ▼
                 ┌──────────────────────────────────┐
                 │   FEEDBACK TO SHM (closed loop)  │
                 │   SHM recomputes state with       │
                 │   updated constraints             │
                 └──────────────────────────────────┘
                                   │
                                   ▼
                 ┌──────────────────────────────────┐
                 │   FIELD-LEVEL INVARIANTS         │
                 │   (external reference layer)      │
                 │   - meta-invariants               │
                 │   - continuity rules              │
                 │   - presence constraints          │
                 └──────────────────────────────────┘

# This diagram represents a minimal closed-loop regulation cycle inside the field engine:

SHM (Symbiosis Health Metric) transforms raw field state into a structured symbiosis score. It normalizes inputs, detects shifts, and computes stability/coherence metrics.

META_LOOP (Presence Loop) receives the SHM output, evaluates it against field-level invariants, applies continuity rules, and generates corrective feedback.

The feedback is returned to SHM, which recomputes the state under updated constraints.

Field-Level Invariants act as an external, stable reference layer that both modules must respect.

The loop expresses a continuous cycle of sensing, evaluation, correction, and re-evaluation.

