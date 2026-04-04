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

---

## Homeostatic Impact

### O₁ — Signals
(what signals this ADR affects or protects)

### O₂ — Field
(how it modifies or stabilizes the relational field)

### O₃ — Structure
(what structural constraints or invariants it introduces)

### O₄ — Behavior
(what runtime behavior it enforces or forbids)

---

## Invariant Preservation
- Relational invariants:
- Semantic invariants:
- Safety invariants:
- EGD relevance:

---

## Boundary Conditions
- Allowed:
- Forbidden:
- Escalation path:
- Recovery path:

---

## Continuity Guarantees
- No discontinuities in O₁–O₄
- No semantic drift
- No false O₄
- No topicification

---

---

## Homeostatic Impact

### O₁ — Signals
(Opisz, jakie sygnały ten ADR wprowadza / ogranicza / chroni.)

### O₂ — Field
(Opisz, jak ADR wpływa na pole relacyjne: stabilizacja, brak eskalacji, brak dryfu.)

### O₃ — Structure
(Opisz, jakie struktury / kontrakty / ograniczenia wprowadza ADR.)

### O₄ — Behavior
(Opisz, jakie zachowania runtime są wymagane / zabronione.)

---

## Invariant Preservation

- Relational invariants:
- Semantic invariants:
- Safety invariants:
- Other invariants:

---

## Boundary Conditions

### Dozwolone
- …

### Zabronione
- …

### Escalation / Recovery
- Co się dzieje przy naruszeniu? Jak wygląda powrót do homeostazy?

---

## EGD Compliance

- Czy ADR dotyka relacji człowiek–model?
- Jak unika fałszywego O₄?
- Jak zapobiega symulacji stanów wewnętrznych?
