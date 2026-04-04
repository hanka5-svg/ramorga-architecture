ADR‑028 — Wersjonowanie benchmarku MC‑11/MC‑12/MC‑13

Status
Accepted

Kontekst
Benchmark MC‑11/MC‑12/MC‑13 jest fundamentem testów interpretacyjnych RAMORGI.
Po dodaniu:

MC‑12 (emergencja),

MC‑13 (fonologia),

matrycy integracyjnej,

scoringu W1–W5,

automatyzacji FIELD ENGINE,

benchmark stał się złożonym systemem, który musi być wersjonowany, aby:

zachować powtarzalność badań,

umożliwić porównywanie modeli między wersjami,

zapewnić kompatybilność wsteczną,

kontrolować zmiany w testach i scoringu.

Decyzja
Wprowadzamy formalny system wersjonowania benchmarku MC‑11/MC‑12/MC‑13:

1. Numeracja benchmarku

Format:

BENCH-MC[11-12-13]-vX.Y.Z
X — zmiany strukturalne (np. dodanie nowej warstwy, zmiana scoringu),

Y — zmiany w testach (dodanie nowych zagadek, korekta kryteriów),

Z — poprawki techniczne (format danych, automatyzacja).

2. Zasady kompatybilności
Zmiana X → wyniki nieporównywalne z poprzednimi wersjami.

Zmiana Y → wyniki częściowo porównywalne.

Zmiana Z → pełna kompatybilność.

3. Repozytorium wersji
Każda wersja benchmarku musi mieć własny wpis w:

02_field_engine/benchmark_versions/

4. Wymóg dokumentacji zmian
Każda zmiana benchmarku wymaga wpisu w 08_changelog/.

Uzasadnienie
Benchmark jest narzędziem badawczym — musi być stabilny i wersjonowany.

Modele ewoluują — wyniki muszą być porównywalne między wersjami.

FIELD ENGINE wymaga jasnych zasad aktualizacji.

Konsekwencje
Pozytywne:

stabilność badań,

możliwość porównywania modeli,

kontrola nad zmianami benchmarku.

Negatywne:

konieczność utrzymania wersji,

większa złożoność dokumentacji.

Powiązania
Model_Scoring.md

MC_Integration_Matrix.md

AT‑MC11_MC12_MC13_Automation.md

HOMEOSTATIC_METRICS.md

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
