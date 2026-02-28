# RAMORGA Interfaces

The Interfaces module defines all explicit contracts between RAMORGA components.  
Each interface is deterministic, versioned, and invariant‑compliant.

---

## Field Engine Interfaces

### FieldState → MeniscusState
- Normalized field representation.
- Must satisfy field invariants.
- Must include tension, energy, entropy, ritual, and continuity signatures.

### MeniscusState → PipelineState
- Stabilized intermediate representation.
- Must satisfy meniscus invariants.
- No discontinuities allowed.

---

## Pipeline Interfaces

### PipelineState → StepResult
- Deterministic output of a single pipeline step.
- Must preserve continuity and invariants.

### StepResult → PipelineState (multi-step)
- Aggregated state for multi-step execution.
- Must not modify protected fields.

---

## Snapshot Interfaces

### FieldState ↔ Snapshot
- Bidirectional conversion.
- Snapshot restoration must preserve invariants.

---

## Error Interfaces

### InvalidStateError
- Triggered when invariants are violated.

### DiscontinuityError
- Triggered when transitions exceed allowed thresholds.

---

## Related Documents

- [Field Engine](../02_field_engine/README.md)
- [Meniscus Engine](../03_meniscus_engine/README.md)
- [Invariants](../04_invariants/README.md)
- [Pipeline](../pipeline/README.md)
