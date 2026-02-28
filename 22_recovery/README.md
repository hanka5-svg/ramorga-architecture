# RAMORGA Recovery Model

The Recovery module defines how RAMORGA restores stable operation after errors, invariant violations, or discontinuities.

---

## Recovery Mechanisms

- **Snapshot Restoration** — revert to last valid snapshot.
- **State Correction** — repair invalid or discontinuous states.
- **Isolation Mode** — prevent unsafe propagation.
- **Pipeline Reset** — restart deterministic execution.

---

## Recovery Requirements

- All recovery operations must preserve invariants.
- Recovery must be deterministic and reversible.
- No recovery step may introduce new discontinuities.
- Recovery must support multi-step rollback.

---

## Recovery Workflow

1. Detect error or invariant violation.
2. Enter isolation mode.
3. Restore snapshot or correct state.
4. Validate invariants.
5. Resume execution.

---

## Related Documents

- [Debugging](../21_debugging/README.md)
- [Logging](../20_logging/README.md)
- [Runtime](../18_runtime/README.md)
- [Invariants](../04_invariants/README.md)
