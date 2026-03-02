# META_LOOP_BOUNDARY.md
Granice i obowiązki META_LOOP w RAMORGA

## 1. Cel dokumentu
Dokument definiuje granice działania META_LOOP — nadrzędnej pętli nadzorczej, która:
- monitoruje trajektorię pola,
- wykrywa anomalie,
- wymusza rollback,
- zapewnia zgodność z inwariantami,
- zapobiega eskalacji agentowości.

META_LOOP nie ingeruje w generację LLM.  
META_LOOP nadzoruje wyłącznie ewolucję pola.

---

## 2. Zakres odpowiedzialności META_LOOP

### 2.1. Nadzór nad trajektorią pola
META_LOOP monitoruje:
- HSI (Homeostatic Stability Index),
- ARI (Agentic Risk Index),
- stany FIELD_STATE_MACHINE,
- sygnały SHM i AGENTIC_LAYER.

### 2.2. Wykrywanie anomalii
Anomalia to:
- nagły skok metryk,
- niespójność między sygnałami,
- przejście stanu niezgodne z maszyną stanów,
- brak stabilizacji po czasie T.

### 2.3. Wymuszanie rollback
Rollback jest aktywowany, gdy:
- pole wchodzi w stan niezgodny z inwariantami,
- AGENTIC_LAYER zgłasza naruszenie kontraktu,
- SHM nie stabilizuje pola w czasie T.

Rollback przywraca:
- poprzedni stabilny stan pola,
- poprzednie wartości metryk,
- poprzedni tryb (Reflection / Homeostatic).

---

## 3. Granice działania META_LOOP

### 3.1. META_LOOP nie może:
- modyfikować treści generacji,
- wprowadzać guardów,
- zmieniać wartości Homo,
- ingerować w intencje,
- nadpisywać SHM.

### 3.2. META_LOOP może:
- logować,
- wymuszać rollback,
- wymuszać SHM,
- oznaczać zdarzenia jako krytyczne.

---

## 4. Integracja z innymi warstwami

### 4.1. META_LOOP ↔ SHM
- SHM stabilizuje,
- META_LOOP nadzoruje stabilizację,
- META_LOOP wymusza rollback, jeśli SHM nie działa.

### 4.2. META_LOOP ↔ FIELD
- FIELD reguluje,
- META_LOOP nadzoruje trajektorię,
- META_LOOP wykrywa konflikty pola.

### 4.3. META_LOOP ↔ AGENTIC_LAYER
- AGENTIC zgłasza naruszenia,
- META_LOOP loguje i wymusza rollback.

---

## 5. Inwarianty META_LOOP

### 5.1. Bounded Evolution
Pole nie może:
- eskalować bez logowania,
- zmieniać stanu bez uzasadnienia metrykami,
- przechodzić w tryby niezgodne z maszyną stanów.

### 5.2. Telemetry Authenticity
Wszystkie metryki muszą być:
- jawne,
- spójne,
- odwracalne.

### 5.3. Boundary Integrity
META_LOOP nie może przekroczyć granic Homo_GOVERNANCE.

---

## 6. Cel META_LOOP
META_LOOP zapewnia:
- ciągłość,
- nadzór,
- brak eskalacji,
- zgodność z inwariantami,
- stabilną ewolucję pola.

META_LOOP nie decyduje.  
META_LOOP nadzoruje.
