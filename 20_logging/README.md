# RAMORGA Logging Model

The Logging module defines how RAMORGA records execution traces, state transitions, and diagnostic information.

---

## Logging Requirements

- All logs must be deterministic.
- Logs must not contain sensitive or protected fields.
- Logs must support snapshot-based reconstruction.
- Logs must be minimal and invariant-compliant.

---

## Log Types

- **State Logs** — record FieldState, MeniscusState, PipelineState signatures.
- **Transition Logs** — record changes between states.
- **Invariant Logs** — record violations and enforcement actions.
- **Runtime Logs** — record execution timing and errors.

---

## Log Structure

- Timestamp (monotonic)
- Module identifier
- State signature hash
- Transition summary
- Error or invariant status

---

## Related Documents

- [Runtime](../18_runtime/README.md)
- [Debugging](../21_debugging/README.md)
- [Recovery](../22_recovery/README.md)
- [Invariants](../04_invariants/README.md)
