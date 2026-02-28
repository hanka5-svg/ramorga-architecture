# RAMORGA System Overview

This document provides a high-level architectural overview of RAMORGA, describing major modules, execution flow, and system-wide constraints.

---

## System Architecture

RAMORGA consists of four primary layers:

1. **Field Layer** — tension, energy, entropy, ritual, continuity.
2. **Meniscus Layer** — normalization, stabilization, gating.
3. **Pipeline Layer** — deterministic execution of steps.
4. **Recovery Layer** — snapshot restoration and correction.

All layers are governed by invariants, security rules, and versioning constraints.

---

## Execution Flow

1. Field Engine computes `FieldState`.
2. Meniscus Engine normalizes to `MeniscusState`.
3. Pipeline executes deterministic steps to produce `PipelineState`.
4. Snapshot Manager captures or restores state.
5. Security validates transitions.
6. Metrics, Logging, and Debugging observe execution.
7. Recovery handles failures.

---

## Module Map

- **02_field_engine** — field dynamics and signatures.
- **03_meniscus_engine** — stabilization and gating.
- **04_invariants** — global constraints.
- **05_interfaces** — deterministic contracts.
- **09_principles** — architectural rules.
- **10_nfr** — non-functional requirements.
- **11_adr** — architectural decisions.
- **12_architecture_tests** — invariant and interface tests.
- **13_security** — safety boundaries.
- **14_integration** — cross-module flow.
- **15_versioning** — compatibility rules.
- **16_polyphony** — multi-stream execution.
- **17_machine_schema** — unified state schema.
- **18_runtime** — execution-time behavior.
- **19_metrics** — system metrics.
- **20_logging** — deterministic logs.
- **21_debugging** — diagnostic tools.
- **22_recovery** — rollback and correction.
- **25_error_model** — error classification and propagation.

---

## System Guarantees

- Deterministic execution.
- Invariant preservation.
- Continuity across transitions.
- Snapshot-safe recovery.
- Versioned interfaces.
- Bounded runtime behavior.

---

## Related Documents

- [Error Model](../25_error_model/README.md)
- [Invariants](../04_invariants/README.md)
- [Runtime](../18_runtime/README.md)
- [Machine Schema](../17_machine_schema/README.md)
