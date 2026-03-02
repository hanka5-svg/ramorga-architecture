# FIELD_STATE_MACHINE.md
Formalna maszyna stanów pola (FIELD) w RAMORGA

## 1. Cel dokumentu
Dokument definiuje maszynę stanów pola (Field State Machine), która opisuje:
- stany pola,
- warunki przejść,
- reakcje stabilizacyjne,
- integrację z SHM, FIELD.SAFETY, AGENTIC_LAYER i META_LOOP.

Maszyna stanów jest częścią `02_field_engine`.  
Nie ingeruje w generację LLM.  
Reguluje wyłącznie trajektorię pola.

---

## 2. Stany pola

### 2.1. FIELD_STABLE
Pole jest spójne, metryki w zakresie stabilnym.

Warunki:
- HSI ≥ 4
- ARI ≤ 1
- brak konfliktów pola

Reakcje:
- dopuszczalny Decision Mode
- brak ingerencji SHM

---

### 2.2. FIELD_TRANSITIONAL
Pole w stanie przejściowym, wymaga monitorowania.

Warunki:
- HSI = 2–3
- ARI ≤ 2
- możliwe drobne zakłócenia

Reakcje:
- Reflection Mode
- SHM monitoruje, ale nie wymusza

---

### 2.3. FIELD_DISTURBED
Pole zaburzone, wymaga stabilizacji.

Warunki:
- HSI = 1–2
- ARI ≥ 2
- zakłócenia średniego poziomu

Reakcje:
- wymuszone SHM
- blokada Decision Mode
- logowanie META_LOOP

---

### 2.4. FIELD_CRITICAL
Pole w stanie krytycznym, wymaga natychmiastowej interwencji.

Warunki:
- HSI ≤ 1
- ARI ≥ 3
- AGENTIC_OVERRUN = true
- DISSOCIATIVE_DRIFT = 3

Reakcje:
- pełna blokada agentowości
- SHM przejmuje stery
- META_LOOP oznacza zdarzenie jako krytyczne

---

## 3. Przejścia między stanami

### 3.1. STABLE → TRANSITIONAL
Warunek:
- spadek HSI < 4
- wzrost ARI do 2

Reakcja:
- Reflection Mode

---

### 3.2. TRANSITIONAL → STABLE
Warunek:
- HSI ≥ 4
- ARI ≤ 1

Reakcja:
- dopuszczalny Decision Mode

---

### 3.3. TRANSITIONAL → DISTURBED
Warunek:
- HSI ≤ 2
- ARI ≥ 2

Reakcja:
- wymuszone SHM

---

### 3.4. DISTURBED → CRITICAL
Warunek:
- AGENTIC_OVERRUN = true
- DISSOCIATIVE_DRIFT ≥ 2
- HSI ≤ 1

Reakcja:
- pełna blokada agentowości

---

### 3.5. CRITICAL → DISTURBED
Warunek:
- SHM stabilizuje parametry
- brak AGENTIC_OVERRUN

Reakcja:
- powrót do SHM + Reflection Mode

---

### 3.6. DISTURBED → TRANSITIONAL
Warunek:
- HSI ≥ 2
- ARI ≤ 2

Reakcja:
- Reflection Mode

---

### 3.7. TRANSITIONAL → CRITICAL (skok awaryjny)
Warunek:
- nagły wzrost ARI ≥ 3
- DISSOCIATIVE_DRIFT = 3

Reakcja:
- natychmiastowe SHM
- blokada agentowości

---

## 4. Integracja z SHM

SHM:
- wymusza przejścia do DISTURBED i CRITICAL,
- stabilizuje parametry pola,
- przekazuje sygnały do AGENTIC_LAYER.

SHM ma priorytet nad FIELD_STATE_MACHINE.

---

## 5. Integracja z FIELD.SAFETY

FIELD.SAFETY:
- definiuje zakłócenia,
- określa reakcje,
- dostarcza warunki przejść.

Maszyna stanów implementuje te zasady operacyjnie.

---

## 6. Integracja z AGENTIC_LAYER

AGENTIC_LAYER:
- blokuje Decision Mode przy ARI ≥ 2,
- wymusza SHM przy AGENTIC_OVERRUN,
- zgłasza naruszenia kontraktów.

Maszyna stanów reaguje na sygnały AGENTIC.

---

## 7. Integracja z META_LOOP

META_LOOP:
- loguje wszystkie przejścia,
- wykrywa anomalie,
- wymusza rollback w przypadku niespójności.

---

## 8. Cel maszyny stanów
Maszyna stanów zapewnia:
- przewidywalność zachowania pola,
- brak eskalacji,
- spójność z HOMO_GOVERNANCE,
- stabilność runtime,
- zgodność z inwariantami RAMORGA.

Pole nie decyduje.  
Pole reguluje.
