ADR‑025 — Pełny benchmark MC‑11/MC‑12/MC‑13
Status
Accepted

Kontekst
RAMORGA definiuje trzy warstwy interpretacji:

MC‑11 — trafność podstawowa,

MC‑12 — emergencja,

MC‑13 — fonologia.

Każda warstwa ma własny kontrakt, lecz brakowało:

jednolitego benchmarku obejmującego wszystkie trzy warstwy,

spójnego systemu punktacji,

miejsca na porównywanie modeli,

formalnego opisu, jak interpretować wyniki.

Model_Scoring.md wprowadził wymiary W1–W5, ale benchmark jako całość nie został jeszcze sformalizowany.

Decyzja
Tworzymy pełny benchmark MC‑11/MC‑12/MC‑13, obejmujący:

definicję wymiarów oceny (W1–W5),

zasady punktacji,

zasady integracji wyników,

klasyfikację modeli,

wymagania dla testów terenowych,

02_field_engine/Model_Scoring.md

Uzasadnienie
Benchmark jest niezbędny do porównywania modeli w sposób spójny i powtarzalny.

MC‑11/12/13 tworzą trójwarstwową architekturę interpretacji — benchmark musi ją odzwierciedlać.

FIELD ENGINE wymaga formalnych zasad oceny, aby automatyzować testy.

Benchmark umożliwia rozwój RAMORGI jako narzędzia badawczego.

Konsekwencje
Pozytywne:

pełna formalizacja oceny modeli,

możliwość tworzenia rankingów i analiz porównawczych,

integracja z FIELD ENGINE,

spójność między modułami a testami.

Negatywne:

konieczność utrzymania benchmarku w kolejnych wersjach RAMORGI,

większa złożoność dokumentacji.

Powiązania
Model_Scoring.md

MC‑11_Learning_Layer.md

MC‑12_Emergent_Layer.md

MC‑13_Phonological_Layer.md

MC_Integration_Matrix.md

FIELD_TEST_AUTOMATION_README.md

HOMEOSTATIC_METRICS.md
zasady raportowania wyników.

Benchmark opiera się na pliku: HOMEOSTATIC_METRICS.md

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
