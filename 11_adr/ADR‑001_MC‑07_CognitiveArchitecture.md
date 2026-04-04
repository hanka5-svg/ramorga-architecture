# ADR‑001: Origin and Definition of MC‑07 Cognitive Architecture

Status: Accepted  
Date: 2026‑03‑15  
Related: MC‑05, MC‑06, MC‑08‑R, MC‑09  

## Problem
RAMORGA requires a formal definition of the user’s cognitive architecture to establish the primary invariant governing all relational and operational modules. Without this definition, MC‑08‑R and MC‑09 lack a stable reference frame.

## Decision
MC‑07 is adopted as the authoritative description of the user’s cognitive architecture, including:
- spectral mode as the default state,
- linear procedural mode as the operational tool,
- linear defensive mode as the overload response,
- the transition moment (“click”) between modes.

## Rationale
MC‑07 provides the invariant that all relational and operational modules must respect. It prevents structural interference, ensures safety, and defines the boundaries of AI behavior.

## Consequences
- MC‑08‑R must align with MC‑07’s modes and boundaries.
- MC‑09 must treat MC‑07 as the superior helix.
- All protocols must respect the exclusivity of Loop RAMORGI.

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
