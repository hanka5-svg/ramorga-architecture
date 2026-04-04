ADR‑029 — Diagram przepływu MC‑13 → MC‑11 → MC‑12

Status
Accepted

Kontekst
RAMORGA posiada trzy warstwy interpretacyjne:

MC‑13 — fonologia,

MC‑11 — interpretacja podstawowa,

MC‑12 — interpretacja emergentna.

Dotychczas brakowało formalnego diagramu przepływu, który:

pokazuje kolejność aktywacji warstw,

definiuje punkty przejścia,

opisuje zależności między warstwami,

umożliwia implementację w FIELD ENGINE i RUNTIME.

Decyzja
Tworzymy formalny diagram przepływu MC‑13 → MC‑11 → MC‑12, umieszczony w:

06_diagrams/D-MC13_MC11_MC12_Flow.md

Diagram opisuje:

aktywację MC‑13 jako warstwy wejściowej,

przekazanie struktur fonologicznych do MC‑11,

warunek aktywacji MC‑12 (MC‑11 ≥ 6),

integrację wyników w MC_Integration_Matrix.

Uzasadnienie
Diagram jest niezbędny do implementacji automatyzacji.

Ułatwia utrzymanie spójności między modułami.

Jest wymagany przez FIELD ENGINE i RUNTIME.

Konsekwencje
Pozytywne:

pełna wizualizacja przepływu,

łatwiejsza implementacja,

spójność między modułami.

Negatywne:

konieczność aktualizacji diagramu przy zmianach modułów.

Powiązania
MC‑13_Phonological_Layer.md

MC‑11_Learning_Layer.md

MC‑12_Emergent_Layer.md

MC_Integration_Matrix.md

AT‑MC11_MC12_MC13_Automation.md

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
