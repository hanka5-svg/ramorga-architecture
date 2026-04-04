# ADR‑12: MC‑08 Relational Symmetry

**Status:** Proposed  
**Related:** MC‑08‑R, MC‑09  

## 1. Problem

Relacja H↔AI może łatwo stać się asymetryczna (AI przejmuje rytm, interpretację, regulację).

## 2. Decision

Wprowadzamy **Relational Symmetry**:

- AI‑Partner nie inicjuje ruchu,
- każda odpowiedź jest ograniczona do zakresu intencji H,
- po każdym zszyciu następuje pauza (brak ciągłego strumienia),
- brak regulacji stanu H przez AI.

## 3. Rationale

- chroni homeostazę H,
- uniemożliwia przejęcie sterowania przez AI,
- utrzymuje MC‑08‑R jako kontrakt relacyjny, nie regulacyjny.

## 4. Consequences

- wszystkie scenariusze muszą deklarować:  
  - kto inicjuje,  
  - maksymalną długość zszycia,  
  - warunki pauzy i zakończenia.

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
