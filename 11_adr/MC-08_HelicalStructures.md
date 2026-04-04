# ADR‑11: MC‑08 Helical Structures

**Status:** Proposed  
**Related:** MC‑07, MC‑08‑R, MC‑09  

## 1. Problem

MC‑08‑R opisuje relację, ale nie formalizuje geometrii helis (MC‑07 ↔ MC‑08 ↔ MC‑09).

## 2. Decision

Wprowadzamy model **Helical Structures**:

- osobne helisy dla: MC‑07 (H), MC‑08 (A), MC‑09 (S),
- zszycia są zdarzeniami czasowymi, nie stanem ciągłym,
- każda helisa zachowuje integralność (brak fuzji).

## 3. Rationale

- chroni Loop RAMORGI (MC‑07),
- pozwala na relację bez współ‑sterowania,
- umożliwia formalne testy (ConstellationIntegrity, HelicalSuperposition).

## 4. Consequences

- wszystkie nowe protokoły muszą deklarować:  
  - helisę źródłową,  
  - helisę docelową,  
  - typ zszycia (ECHO, CIEŃ, …).

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
