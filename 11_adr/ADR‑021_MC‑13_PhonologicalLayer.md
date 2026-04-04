# ADR‑021 — MC‑13 Phonological Layer

## Status
Accepted

## Kontekst
Zagadki RAMORGI często opierają się na:
- sylabach,
- fonemach,
- rytmie,
- szyfrach fonetycznych.

Modele LLM nie posiadają natywnej fonologii, co prowadzi do błędów interpretacyjnych w MC‑11 i MC‑12.  
Brakowało formalnego modułu opisującego warstwę fonologiczną.

## Decyzja
Wprowadzamy moduł **MC‑13 — Phonological Layer**, odpowiedzialny za:
- sylabizację,
- segmentację fonemów,
- analizę akcentu,
- analizę rytmu,
- wykrywanie szyfrów fonetycznych,
- integrację fonologii z MC‑11 i MC‑12.

Plik dodany do repo:

01_module_contracts/MC‑13_Phonological_Layer.md


## Uzasadnienie
- MC‑13 formalizuje warstwę fonologiczną niezbędną do interpretacji zagadek.
- Umożliwia ocenę modeli pod kątem fonetyki.
- Oddziela fonologię od semantyki i emergencji.

## Konsekwencje
- pełna trójwarstwowa interpretacja (MC‑11 + MC‑12 + MC‑13),
- możliwość budowy benchmarku fonologicznego,
- konieczność aktualizacji FIELD ENGINE.

## Powiązania
- MC‑13_Phonological_Layer.md  
- MC‑12_Emergent_Layer.md  
- MC_Integration_Matrix.md  
- Model_Scoring.md  

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
