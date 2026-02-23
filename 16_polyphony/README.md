# Polyphony Module

Moduł odpowiedzialny za strukturalną obsługę wielogłosowości (polyphony) w architekturze RAMORGI.
Zakres: typy, interfejs, invariants, testy integracyjne, opcjonalne metryki napięć.

## Files

- `polyphony_types.ts` — definicje typów rdzeniowych
- `polyphony_handler.ts` — interfejs modułu (bez implementacji)
- `INVARIANTS.md` — twarde invariants modułu
- `fixtures/` — dane testowe (YAML/JSON)
- `tests/` — testy integracyjne modułu

---

# Type Table

| Type | Description | Notes |
|------|-------------|-------|
| `SourceID` | identyfikator źródła | string |
| `EpistemicTag` | tag epistemiczny | brak semantyki w module |
| `Hash` | hash treści | sha256 |
| `FieldState` | pojedynczy stan pola | atomowy, niezmienny |
| `PolyphonicView` | widok wielogłosowy | zachowuje kolejność |
| `EpistemicTraceRow` | wpis śladu epistemicznego | 1:1 z FieldState |
| `EpistemicTraceTable` | tabela śladu | pełna reprodukowalność |
| `TensionEdge` | krawędź napięcia | score ∈ [0..1] |
| `TensionMap` | mapa napięć | opcjonalna, read‑only |

---

# Contract Diagram (ASCII)

+-----------------------------+

PolyphonyHandler
ingest(FieldState[])
+---------------+-------------+
|
v
+-----------------------------------------+

Output
view: PolyphonicView
trace: EpistemicTraceTable
tension?: TensionMap (optional)
+-----------------------------------------+

Input invariants:

no merge

no closure

no loss of attribution

Output guarantees:

order preserved

trace preserved

tension read-only


---

# Invariants

Zdefiniowane w `INVARIANTS.md` jako lista wiążąca:

- NO_MERGE_INTO_SINGLE_TRUTH  
- NO_EPISTEMIC_CLOSURE_BY_HANDLER  
- NO_LOSS_OF_SOURCE_ATTRIBUTION  
- TRACE_PRESERVED_FOR_ALL_FIELDSTATES  
- HANDLER_HAS_NO_OWN_VOICE  

---

# Contract (C/G/S)

## C — Constraints
- brak modyfikacji treści wejściowych  
- brak generowania nowych treści  
- brak heurystyk i brak interpretacji  
- brak stanu wewnętrznego  
- brak side‑effects  
- brak ingerencji w kolejność wejściową  

## G — Guarantees
- zachowanie kolejności `FieldState`  
- pełna reprodukowalność `EpistemicTraceTable`  
- brak utraty `source_id` i `content_hash`  
- opcjonalny `TensionMap` jako read‑only  
- deterministyczny output dla danego inputu  

## S — Structure
- wejście: `ReadonlyArray<FieldState>`  
- wyjście: `{ view, trace, tension? }`  
- moduł wyłącznie strukturalny  
- implementacja pozostaje poza zakresem v0.4.x  

---

# Transition Hooks (for v0.5.x+)

Moduł polyphony jest projektowany jako neutralny komponent strukturalny.
Poniższe hooki definiują miejsca, w których przyszłe moduły mogą się podłączyć
bez naruszania invariants i bez ingerencji w dane źródłowe.

## 1. `tension.compute(input: FieldState[])`
- opcjonalna metryka dywergencji  
- brak wpływu na `view` i `trace`  
- read‑only, side‑effect‑free  
- wynik: `TensionMap`  

## 2. `trace.extend(row: EpistemicTraceRow)`
- wyłącznie dodawanie referencji zewnętrznych  
- brak modyfikacji istniejących wpisów  
- brak zmian semantycznych  

## 3. `view.filter(predicate)`
- operacja wyłącznie prezentacyjna  
- nie wpływa na dane źródłowe  
- nie zmienia kolejności ani zawartości `FieldState`  

## 4. `adapter.serialize(view | trace)`
- formaty: JSON, YAML, msgpack  
- brak zmian semantycznych  
- brak transformacji treści  

---

# Versioning

Linia `v0.4.x` — etap strukturalny (types, interface, invariants, tests).  
Brak implementacji logiki do czasu v0.5.x.
