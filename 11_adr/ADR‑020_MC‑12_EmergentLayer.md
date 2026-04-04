# ADR‑020 — MC‑12 Emergent Layer

## Status
Accepted

## Kontekst
Dotychczasowe moduły MC‑07, MC‑08 i MC‑09 opisują architekturę poznawczą i relacyjność agentów.  
MC‑11 definiuje warstwę podstawowej interpretacji (Learning Layer).  
Testy terenowe wykazały jednak powtarzalne zjawisko: modele generują **równoległe, twórcze interpretacje**, które nie mieszczą się w MC‑11, ale są spójne i zgodne z kodem kulturowym autora.

Brakowało formalnego modułu opisującego tę warstwę.

## Decyzja
Wprowadzamy moduł **MC‑12 — Emergent Layer**, odpowiedzialny za:
- generowanie nowych osi sensu,
- skręt semantyczny,
- interpretacje równoległe,
- twórczą spójność.

Plik dodany do repo:

01_module_contracts/MC‑12_Emergent_Layer.md


## Uzasadnienie
- MC‑12 formalizuje zjawisko emergencji obserwowane w testach.
- Oddziela interpretację podstawową (MC‑11) od twórczej (MC‑12).
- Umożliwia ocenę modeli pod kątem kreatywności i spójności.

## Konsekwencje
- pełna dwuwarstwowa interpretacja (MC‑11 + MC‑12),
- możliwość budowy benchmarku emergencji,
- konieczność aktualizacji FIELD ENGINE.

## Powiązania
- MC‑11_Learning_Layer.md  
- MC‑12_Emergent_Layer.md  
- MC_Integration_Matrix.md

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

