# Polyphony Module

Moduł odpowiedzialny za strukturalną obsługę wielogłosowości (polyphony) w architekturze RAMORGI.
Zakres: typy, interfejs, invariants, testy integracyjne, opcjonalne metryki napięć.

## Files

- `polyphony_types.ts` — definicje typów rdzeniowych
- `polyphony_handler.ts` — interfejs modułu (bez implementacji)
- `INVARIANTS.md` — twarde invariants modułu
- `fixtures/` — dane testowe (YAML/JSON)
- `tests/` — testy integracyjne modułu

## Invariants

Zdefiniowane w `INVARIANTS.md` jako lista wiążąca:

- NO_MERGE_INTO_SINGLE_TRUTH  
- NO_EPISTEMIC_CLOSURE_BY_HANDLER  
- NO_LOSS_OF_SOURCE_ATTRIBUTION  
- TRACE_PRESERVED_FOR_ALL_FIELDSTATES  
- HANDLER_HAS_NO_OWN_VOICE  

## Contract (C/G/S)

### C — Constraints
- brak modyfikacji treści wejściowych  
- brak generowania nowych treści  
- brak heurystyk i brak interpretacji  
- brak stanu wewnętrznego  
- brak side‑effects  

### G — Guarantees
- zachowanie kolejności `FieldState`  
- pełna reprodukowalność `EpistemicTraceTable`  
- brak utraty `source_id` i `content_hash`  
- opcjonalny `TensionMap` jako read‑only  

### S — Structure
- wejście: `ReadonlyArray<FieldState>`  
- wyjście: `{ view, trace, tension? }`  
- moduł wyłącznie strukturalny  
- implementacja pozostaje poza zakresem v0.4.x  

## Versioning

Linia `v0.4.x` — etap strukturalny (types, interface, invariants, tests).
Brak implementacji logiki do czasu v0.5.x.
