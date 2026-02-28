# Meniscus Engine

The Meniscus Engine defines the intermediate regulatory layer between the Field Engine and the Pipeline. It stabilizes transitions, buffers state changes, and ensures that field-level dynamics remain compatible with pipeline execution.

---

## Responsibilities

- Maintain a stable intermediate state between field updates and pipeline steps.
- Normalize and validate incoming field states.
- Apply meniscus-specific transformations (compression, smoothing, gating).
- Detect and handle discontinuities or invalid transitions.
- Provide a consistent interface for the pipeline.

---

## Data Flow

1. Field Engine produces a `FieldState`.
2. Meniscus Engine receives and normalizes the state.
3. Meniscus Engine applies gating and smoothing.
4. Meniscus Engine outputs a `MeniscusState` to the Pipeline.

---

## Meniscus Modes

- **Passive Mode** — direct passthrough with minimal normalization.
- **Stabilization Mode** — smoothing and gating enabled.
- **Correction Mode** — discontinuity handling and state repair.
- **Isolation Mode** — blocks propagation when invariants are violated.

---

## Interfaces

### Input
- `FieldState` from `02_field_engine`.

### Output
- `MeniscusState` for `PipelineV13`.

---

## Related Documents

- [Field Engine](../02_field_engine/README.md)
- [Field Dynamics](../02_field_engine/field_dynamics.md)
- [Invariants](../04_invariants/README.md)
- [Pipeline](../pipeline/README.md)
