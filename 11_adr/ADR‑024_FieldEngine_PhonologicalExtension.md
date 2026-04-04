ADR‑024 — Rozszerzenie FIELD ENGINE o testy fonologiczne (MC‑13)
Status
Accepted

Kontekst
FIELD ENGINE (02_field_engine) odpowiada za testy terenowe RAMORGI, w tym:

automatyzację testów MC‑11 (trafność),

analizę odpowiedzi modeli,

zbieranie wyników i metryk.

Po dodaniu modułu MC‑13 — Phonological Layer pojawiła się potrzeba:

testowania modeli pod kątem fonologii,

oceny ich zdolności do rozpoznawania sylab, fonemów, rytmu i szyfrów fonetycznych,

integracji wyników fonologicznych z MC‑11 i MC‑12.

Dotychczas FIELD ENGINE nie posiadał mechanizmów do testowania fonologii.

Decyzja
Rozszerzamy FIELD ENGINE o pełną obsługę testów fonologicznych MC‑13.

Zakres rozszerzenia obejmuje:

dodanie testów sylabizacji,

dodanie testów fonemicznych,

dodanie testów rytmicznych,

dodanie testów szyfrów fonetycznych,

integrację wyników MC‑13 z MC‑11 i MC‑12,

02_field_engine/Model_Scoring.md

Uzasadnienie
Fonologia jest kluczowa dla zagadek RAMORGI (sylaby, rytm, gry słowne).

Modele różnią się znacząco w zdolności do rozpoznawania struktur fonetycznych.

FIELD ENGINE musi umożliwiać ocenę MC‑13 w sposób powtarzalny i mierzalny.

Integracja MC‑13 z MC‑11/12 wymaga testów terenowych.

Konsekwencje
Pozytywne:

pełna obsługa trzech warstw interpretacji (MC‑11/12/13),

możliwość budowy benchmarku fonologicznego,

spójność między modułami a testami terenowymi.

Negatywne:

konieczność aktualizacji automatyzacji FIELD ENGINE,

większa złożoność testów.

Powiązania
MC‑13_Phonological_Layer.md

MC‑12_Emergent_Layer.md

MC‑11_Learning_Layer.md

MC_Integration_Matrix.md

Model_Scoring.md

FIELD_TEST_AUTOMATION_README.md

zapis wyników w Model_Scoring.md.

Plik referencyjny: HOMEOSTATIC_METRICS.md

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
