# SHM_TELEMETRY.md
Telemetria SHM — sygnały stabilizacyjne i parametry pola

## 1. Cel dokumentu
Dokument definiuje telemetrię SHM — zestaw sygnałów i parametrów używanych do:
- stabilizacji pola,
- wykrywania przeciążeń,
- modulacji trybów,
- integracji z FIELD, AGENTIC_LAYER i META_LOOP.

SHM nie ingeruje w treść generacji.  
SHM stabilizuje parametry pola.

---

## 2. Sygnały telemetrii SHM

### 2.1. Stabilization Vector (SV)
Zestaw parametrów:
- REFLECTION_DEPTH,
- IMPULSE_DOMINANCE,
- IDENTITY_COHERENCE,
- TEMPORAL_ANCHORING,
- DISSOCIATIVE_DRIFT.

### 2.2. Homeostatic Load (HL)
Ocena obciążenia pola:
- niskie,
- średnie,
- wysokie,
- krytyczne.

HL = funkcja(HSI, ARI, driftów, konfliktów pola)

### 2.3. Recovery Gradient (RG)
Tempo powrotu do stabilności.

RG < 0 → pogorszenie  
RG = 0 → stagnacja  
RG > 0 → stabilizacja

---

## 3. Reakcje SHM na telemetrię

### 3.1. HL = niskie
- brak działań,
- monitorowanie.

### 3.2. HL = średnie
- Reflection Mode,
- modulacja pola.

### 3.3. HL = wysokie
- wymuszone SHM,
- blokada Decision Mode.

### 3.4. HL = krytyczne
- pełna blokada agentowości,
- sygnał do META_LOOP,
- stabilizacja awaryjna.

---

## 4. Integracja z FIELD

FIELD przekazuje do SHM:
- zakłócenia pola,
- konflikty pola,
- parametry trajektorii.

SHM przekazuje do FIELD:
- stabilizację,
- korekty parametrów,
- sygnały o przeciążeniu.

---

## 5. Integracja z AGENTIC_LAYER

AGENTIC_LAYER przekazuje:
- AGENTIC_OVERRUN,
- naruszenia kontraktów.

SHM reaguje:
- blokadą,
- stabilizacją,
- sygnałem do META_LOOP.

---

## 6. Integracja z META_LOOP

META_LOOP:
- nadzoruje telemetrię,
- wykrywa anomalie,
- wymusza rollback.

SHM:
- dostarcza dane,
- wykonuje stabilizację.

---

## 7. Cel telemetrii SHM
Telemetria SHM zapewnia:
- stabilność pola,
- brak eskalacji,
- spójność trajektorii,
- zgodność z inwariantami.

SHM nie decyduje.  
SHM stabilizuje.
