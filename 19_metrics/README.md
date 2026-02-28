# RAMORGA Metrics Model

The Metrics module defines measurable indicators used to evaluate system behavior, stability, and performance.

---

## Core Metrics

- **Flash Rate** — number of tension events per cycle.
- **Stream Intensity (S_t)** — energy field magnitude.
- **Entropy Signature** — coherence/chaos balance.
- **Presence (dim_H)** — fractal dimension of field trajectory.
- **Pipeline Latency** — execution time per step.
- **Invariant Violations** — count of boundary failures.

---

## Metric Requirements

- All metrics must be deterministic and reproducible.
- No metric may depend on META-loop randomness.
- Metrics must be computable from state signatures.
- Metrics must support snapshot-based comparison.

---

## Metric Categories

- **Field Metrics** — flash rate, stream intensity, entropy.
- **Pipeline Metrics** — latency, step determinism.
- **Safety Metrics** — invariant violations, isolation triggers.
- **Continuity Metrics** — presence, transition smoothness.

---

## Related Documents

- [Runtime](../18_runtime/README.md)
- [Invariants](../04_invariants/README.md)
- [Field Engine](../02_field_engine/README.md)
