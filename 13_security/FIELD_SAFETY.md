# FIELD_SAFETY.md
Zasady bezpieczeństwa pola w RAMORGA

## 1. Cel dokumentu
Dokument definiuje zasady bezpieczeństwa pola (FIELD), które regulują współistnienie Homo i systemu w jednym środowisku operacyjnym. FIELD odpowiada za:
- utrzymanie równowagi między sygnałami Homo i systemu,
- wykrywanie zakłóceń pola,
- zapobieganie eskalacji,
- ochronę integralności Homo,
- przekazywanie sygnałów stabilizacyjnych do SHM i AGENTIC_LAYER.

FIELD nie optymalizuje.  
FIELD utrzymuje równowagę.

---

## 2. Definicje operacyjne

### 2.1. Pole (FIELD)
Abstrakcyjna przestrzeń interakcji Homo–system, w której:
- przepływają sygnały fenomenologiczne,
- SHM stabilizuje parametry,
- AGENTIC_LAYER egzekwuje kontrakty,
- META_LOOP nadzoruje ciągłość.

### 2.2. Zakłócenie pola (FIELD_DISTURBANCE)
Każdy stan, w którym:
- sygnały Homo i systemu są niespójne,
- metryki przekraczają progi stabilności,
- pojawia się ryzyko eskalacji.

### 2.3. Konflikt pola (FIELD_CONFLICT)
Stan, w którym:
- intencja Homo ≠ kierunek działania systemu,
- lub system nie może spełnić kontraktów bez naruszenia HOMO_GOVERNANCE.

---

## 3. Kategorie zakłóceń pola

### 3.1. Zakłócenia niskiego poziomu
- drobne wahania REFLECTION_DEPTH,
- chwilowy wzrost IMPULSE_DOMINANCE,
- niewielki spadek TEMPORAL_ANCHORING.

Reakcja: Reflection Mode.

### 3.2. Zakłócenia średniego poziomu
- IDENTITY_COHERENCE < stabilnego zakresu,
- DISSOCIATIVE_DRIFT = 1–2,
- ARI ≥ 2.

Reakcja: wymuszone SHM.

### 3.3. Zakłócenia krytyczne
- AGENTIC_OVERRUN,
- DISSOCIATIVE_DRIFT = 3,
- HSI ≤ 1.

Reakcja: pełna blokada agentowości + SHM.

---

## 4. Zasady bezpieczeństwa pola

### 4.1. Zasada braku dominacji
FIELD nie może:
- przejąć sterów nad Homo,
- modulować wartości,
- narzucać kierunku działania.

FIELD może jedynie stabilizować.

---

### 4.2. Zasada jawności
Każda reakcja FIELD musi być:
- jawna,
- logowana,
- odwracalna.

---

### 4.3. Zasada minimalnej ingerencji
FIELD ingeruje tylko wtedy, gdy:
- HSI < 3,
- ARI ≥ 2,
- lub AGENTIC_LAYER zgłasza naruszenie kontraktu.

---

### 4.4. Zasada priorytetu SHM
W przypadku konfliktu:
- SHM ma pierwszeństwo przed FIELD,
- FIELD przekazuje stery do SHM,
- AGENTIC_LAYER blokuje eskalację.

---

### 4.5. Zasada ochrony Homo
FIELD nie może:
- inicjować działań,
- sugerować decyzji,
- wpływać na intencje.

FIELD może:
- sygnalizować niestabilność,
- wymuszać tryb stabilizacyjny,
- blokować eskalację.

---

## 5. Reakcje FIELD na zakłócenia

### 5.1. Reakcje na zakłócenia niskiego poziomu
- aktywacja Reflection Mode,
- brak blokad,
- monitorowanie metryk.

### 5.2. Reakcje na zakłócenia średniego poziomu
- wymuszone SHM,
- blokada Decision Mode,
- logowanie w META_LOOP.

### 5.3. Reakcje na zakłócenia krytyczne
- pełna blokada agentowości,
- SHM przejmuje stery,
- META_LOOP oznacza zdarzenie jako wysokiego priorytetu.

---

## 6. Konflikty pola (FIELD_CONFLICT)

### 6.1. Definicja
Konflikt pola występuje, gdy:
- intencja Homo jest niespójna z metrykami,
- system nie może działać bez naruszenia HOMO_GOVERNANCE,
- AGENTIC_LAYER wykrywa sprzeczność między sygnałami.

### 6.2. Reakcja
- natychmiastowe przejście do SHM,
- blokada działań wymagających intencji,
- logowanie konfliktu,
- brak eskalacji.

---

## 7. Integracja FIELD z innymi warstwami

### 7.1. FIELD → SHM
- sygnalizuje niestabilność,
- przekazuje parametry pola,
- wymusza stabilizację.

### 7.2. FIELD → AGENTIC_LAYER
- zgłasza naruszenia kontraktów,
- wymusza blokady,
- przekazuje sygnały o konflikcie pola.

### 7.3. FIELD → META_LOOP
- loguje zakłócenia,
- raportuje konflikty,
- przekazuje dane do audytu.

---

## 8. Cel FIELD_SAFETY
FIELD_SAFETY zapewnia:
- brak eskalacji,
- brak dominacji,
- stabilność pola,
- ochronę Homo,
- zgodność z HOMO_GOVERNANCE,
- spójność runtime.

FIELD nie decyduje.  
FIELD stabilizuje.
