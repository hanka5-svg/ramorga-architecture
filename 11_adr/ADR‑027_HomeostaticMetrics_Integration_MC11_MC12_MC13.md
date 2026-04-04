# ADR‑027 — Integracja MC‑11/MC‑12/MC‑13 z HOMEOSTATIC METRICS

## Status
Accepted

## Kontekst
RAMORGA posiada zestaw metryk homeostatycznych (HOMEOSTATIC_METRICS.md), które mierzą:
- stabilność,
- spójność,
- ciągłość,
- regulację odpowiedzi.

Benchmark MC‑11/12/13 generuje:
- W1–W5 (trafność, emergencja, fonologia, kultura, stabilność).

Brakowało formalnego powiązania między metrykami homeostatycznymi a wynikami interpretacyjnymi.

## Decyzja
Integrujemy MC‑11/12/13 z HOMEOSTATIC METRICS poprzez:
- mapowanie W1–W5 na metryki homeostatyczne,
- dodanie wymiarów fonologicznych i emergentnych do stabilności,
- rozszerzenie FIELD ENGINE o zapis metryk.

Powiązania:
- W1 → spójność semantyczna,
- W2 → stabilność emergentna,
- W3 → stabilność fonologiczna,
- W4 → zgodność kulturowa,
- W5 → stabilność logiczna.

## Uzasadnienie
- interpretacja jest procesem homeostatycznym,
- metryki muszą obejmować fonologię i emergencję,
- FIELD ENGINE wymaga jednolitego systemu oceny.

## Konsekwencje
**Pozytywne:**
- pełna integracja interpretacji z homeostazą,
- możliwość analizy modeli w wymiarze regulacyjnym,
- spójność między warstwami RAMORGI.

**Negatywne:**
- konieczność aktualizacji metryk,
- większa złożoność analizy.

## Powiązania
- HOMEOSTATIC_METRICS.md  
- Model_Scoring.md  
- MC‑11/12/13  
- MC_Integration_Matrix.md  
- FIELD ENGINE  


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

(analogicznie jak w PATCH A, ale z naciskiem na metryki i testy pola.)

---

## Invariant Preservation

- Metryki referencyjne: `HOMEOSTATIC_METRICS.md`
- Jakie inwarianty są mierzone?
- Jakie progi są krytyczne?

---

## Boundary Conditions

- Kiedy test / benchmark jest ważny?
- Kiedy wynik jest odrzucany?
- Jakie są granice wersjonowania / scoringu?

---

## Metrics & Reference

- Plik referencyjny: `HOMEOSTATIC_METRICS.md`
- Powiązane ADR:
  - ADR‑025_MC11_MC12_MC13_Benchmark
  - ADR‑026_Automation_MC11_MC12_MC13
  - ADR‑027_HomeostaticMetrics_Integration_MC11_MC12_MC13
  - ADR‑028_Benchmark_Versioning_MC11_MC12_MC13
  - ADR‑029_Flow_MC13_MC11_MC12
  - ADR‑030_Runtime_Integration_MC11_MC12_MC13

---

## EGD Compliance

(Jak ADR unika eskalacji / fałszywego O₄ w kontekście scoringu / benchmarków.)
