# RAMORGA – Engineer Decision Layer (EDL)

This document defines how an engineer or automated validator must classify and respond to architectural failures.

---

## Failure Classification Matrix

| Failure Type | Origin              | Severity  | Required Action                                      |
|--------------|---------------------|-----------|------------------------------------------------------|
| F1           | Field Module        | Critical  | Halt pipeline, reject output, log invariant-1 error  |
| F2           | Measurement Module  | Critical  | Halt pipeline, request explicit user query           |
| F3           | Reduction Module    | High      | Reject output, trigger re-projection                 |
| F4           | Descent Module      | High      | Reject output, enforce controlled descent            |
| F5           | Integrity Module    | Critical  | Halt pipeline, escalate architecture error           |
| F6           | Bridge Module       | Medium    | Retry with alternative reduction strategy            |
| F7           | Relational Module   | High      | Reject output, enforce symmetry constraints          |
| F8           | Relational Module   | Medium    | Rebuild multi-node context                           |
| F9           | Any Module          | Critical  | Halt pipeline, require full architectural audit      |

---

## Decision Logic

```text
IF failure is Critical:
    - Halt pipeline
    - Reject output
    - Log invariant violation
    - Trigger architectural audit if cross-layer

ELSE IF failure is High:
    - Reject output
    - Attempt controlled reprocessing
    - Validate module contract compliance

ELSE IF failure is Medium:
    - Retry with alternative reduction or bridge strategy
    - Rebuild relational or constellation context

ELSE:
    - Accept output with warning

This logic ensures that no critical violation passes silently and that recoverable failures are handled deterministically.

Integration with Architecture Tests
- Invariants define what must never be violated.
- BDD tests define expected behavior under normal and edge conditions.
- Module contracts define responsibilities and guarantees.
- Failure propagation maps show where and how failures spread.
- EDL defines how to respond when failures are detected.

Together, they form the architecture compliance surface for RAMORGA.

