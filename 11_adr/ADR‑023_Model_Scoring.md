# ADR‑023 — Model Scoring for MC‑11/12/13

## Status
Accepted

## Kontekst
Testy terenowe RAMORGI (FIELD ENGINE) wymagają oceny modeli w trzech wymiarach:

- MC‑11 — trafność podstawowa,
- MC‑12 — emergencja,
- MC‑13 — fonologia.

Dotychczas brakowało formalnego systemu punktacji, co utrudniało:

- porównywanie modeli,
- analizę jakości odpowiedzi,
- budowę benchmarku MC‑11/12/13,
- integrację z FIELD ENGINE.

## Decyzja
Wprowadzamy formalny system oceny modeli — **Model Scoring**, obejmujący pięć wymiarów:

- W1 — Trafność (MC‑11),
- W2 — Emergentność (MC‑12),
- W3 — Fonetyka (MC‑13),
- W4 — Kultura (kod kulturowy autora),
- W5 — Stabilność (logika, brak zapętleń).

Plik dodany do repo:

02_field_engine/Model_Scoring.md


## Uzasadnienie
- Scoring umożliwia porównywanie modeli w sposób spójny i powtarzalny.
- Oddziela warstwę modułów (01) od warstwy testowej (02).
- Umożliwia budowę benchmarku MC‑11/12/13.
- Wspiera analizę jakościową i ilościową odpowiedzi modeli.

## Konsekwencje
**Pozytywne:**
- pełna formalizacja oceny modeli,
- możliwość automatyzacji testów,
- możliwość tworzenia rankingów modeli,
- integracja z FIELD ENGINE.

**Negatywne:**
- konieczność aktualizacji testów terenowych,
- konieczność utrzymania scoringu w kolejnych wersjach RAMORGI.

## Powiązania
- MC‑11_Learning_Layer.md  
- MC‑12_Emergent_Layer.md  
- MC‑13_Phonological_Layer.md  
- MC_Integration_Matrix.md  
- FIELD_TEST_AUTOMATION_README.md  
- HOMEOSTATIC_METRICS.md

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
