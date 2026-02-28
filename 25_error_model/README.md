# RAMORGA Error Model

The Error Model defines all error types, propagation rules, and recovery paths across RAMORGA. It ensures that failures remain contained, diagnosable, and reversible.

---

## Error Categories

- **InvariantError** — violation of core, field, pipeline, or safety invariants.
- **DiscontinuityError** — abrupt transition exceeding allowed thresholds.
- **InterfaceError** — malformed or incompatible state passed across boundaries.
- **RuntimeError** — execution-time failure within field, meniscus, or pipeline.
- **SnapshotError** — corrupted or invalid snapshot.
- **SecurityError** — violation of safety boundaries or unauthorized modification.

---

## Error Propagation Rules

- Errors must not propagate across module boundaries without classification.
- All errors must be converted into `ErrorState` before propagation.
- No module may suppress or hide invariant violations.
- All errors must trigger isolation mode unless explicitly marked recoverable.

---

## Error Lifecycle

1. **Detection** — invariants, interfaces, or runtime detect failure.
2. **Classification** — error is mapped to one of the defined categories.
3. **Containment** — system enters isolation mode.
4. **Recovery** — snapshot restoration or state correction.
5. **Validation** — invariants re-checked.
6. **Resumption** — system returns to normal execution.

---

## ErrorState Schema

- `error_type` — category of error.
- `origin_module` — module where error occurred.
- `state_signature` — hash of failing state.
- `timestamp` — monotonic timestamp.
- `details` — structured diagnostic information.

---

## Related Documents

- [Invariants](../04_invariants/README.md)
- [Security](../13_security/README.md)
- [Recovery](../22_recovery/README.md)
- [Debugging](../21_debugging/README.md)
- [Machine Schema](../17_machine_schema/README.md)
