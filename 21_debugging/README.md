# RAMORGA Debugging Model

The Debugging module defines tools and procedures for analyzing system behavior, identifying failures, and validating invariants.

---

## Debugging Tools

- **State Inspector** — examines FieldState, MeniscusState, PipelineState.
- **Transition Analyzer** — detects discontinuities and invalid transitions.
- **Invariant Checker** — validates compliance with all invariants.
- **Snapshot Comparator** — compares states across snapshots.

---

## Debugging Requirements

- All debugging tools must be deterministic.
- No tool may modify system state.
- All debugging operations must be reversible.
- Debugging must not interfere with runtime execution.

---

## Debugging Workflow

1. Capture snapshot.
2. Inspect state signatures.
3. Analyze transitions.
4. Validate invariants.
5. Compare with previous snapshots.

---

## Related Documents

- [Logging](../20_logging/README.md)
- [Recovery](../22_recovery/README.md)
- [Invariants](../04_invariants/README.md)
- [Machine Schema](../17_machine_schema/README.md)
