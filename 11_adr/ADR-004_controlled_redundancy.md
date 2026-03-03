ADR ID: ADR-004
Title: Controlled Constitutional Redundancy
Status: Accepted
Date: 2026-03-03

RAMORGA is a constitutional architecture governed by invariants.
Key principles such as homeostasis, non-escalation, and human primacy
appear across multiple architectural layers.

This repetition may appear redundant from a purely structural perspective.
However, the architecture intentionally avoids single-point semantic authority.

The architecture adopts controlled constitutional redundancy.

Core principles are intentionally restated across:
- Invariants
- Module contracts
- Architecture tests
- Security controls
- Diagrams

Each repetition serves a distinct architectural function
and operates at a different enforcement layer.

Controlled redundancy ensures that constitutional rules:
- remain visible at all architectural entry points,
- are enforceable through multiple mechanisms,
- cannot be bypassed by local interpretation or optimization.

Redundancy is functional, not semantic.
No layer redefines principles; each layer enforces them
within its own responsibility domain.

Positive:
- Increased architectural resilience
- Reduced risk of semantic drift
- Clear enforcement paths for invariants

Negative:
- Apparent repetition across modules
- Slightly increased documentation volume

The trade-off is accepted as necessary
for long-term architectural stability.

- ADR-001: Invariant-Driven Architecture
- ADR-002: Separation of Field and Meniscus Responsibilities
- ADR-003: Invariant-Based Security Model
