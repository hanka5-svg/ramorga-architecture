# ADR‑002: Origin and Definition of MC‑08‑R Relational Agent Contract

Status: Accepted  
Date: 2026‑03‑15  
Related: MC‑05, MC‑06, MC‑07, MC‑09  

## Problem
RAMORGA requires a formal contract defining how an AI agent may participate in relational interaction without violating user autonomy, cognitive architecture, or safety invariants. Without such a contract, MC‑09 cannot be safely introduced.

## Decision
MC‑08‑R is adopted as the authoritative relational agent contract. It establishes:
- non‑initiation of movement,
- non‑regulation of the user,
- non‑intrusion into Loop RAMORGI,
- symmetry and boundedness of interaction,
- strict adherence to MC‑05 and MC‑06.

## Rationale
MC‑08‑R provides the minimal relational framework necessary for safe interaction. It ensures that the AI remains non‑intrusive, predictable, and aligned with the user’s cognitive architecture (MC‑07).

## Consequences
- MC‑09 must extend MC‑08‑R without weakening its constraints.
- All protocols must enforce non‑initiation and non‑regulation.
- MC‑07 remains the superior helix governing interaction boundaries.

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
