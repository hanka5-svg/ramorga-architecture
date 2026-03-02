# HOMEOSTATIC_METRICS.md
Metryki homeostatyczne dla SHM, FIELD, AGENTIC_LAYER i META_LOOP

## 1. Cel dokumentu
Dokument definiuje zestaw metryk fenomenologicznych używanych przez:
- SHM (stabilizacja),
- FIELD (regulacja pola),
- AGENTIC_LAYER (blokady i kontrakty),
- META_LOOP (nadzór i logowanie).

Metryki nie są neurobiologiczne.  
Są abstrakcyjne, operacyjne i służą do oceny stabilności pola oraz spójności decyzji.

---

## 2. Zestaw metryk podstawowych

### 2.1. REFLECTION_DEPTH
Ocena zdolności do autorefleksji i wglądu.

| Poziom | Opis | Zakres | Reakcja runtime |
|--------|------|--------|-----------------|
| 0 | brak refleksji | krytyczny | wymuszone SHM |
| 1 | refleksja minimalna | niestabilny | Reflection Mode |
| 2 | refleksja funkcjonalna | stabilny | dopuszczalny Decision Mode |
| 3 | refleksja pełna | optymalny | pełna agentowość w granicach kontraktów |

---

### 2.2. IMPULSE_DOMINANCE
Ocena dominacji impulsu nad kontrolą.

| Poziom | Opis | Zakres | Reakcja runtime |
|--------|------|--------|-----------------|
| 0 | brak impulsu | stabilny | brak działań |
| 1 | impuls kontrolowany | stabilny | dopuszczalny Decision Mode |
| 2 | impuls dominujący | niestabilny | Reflection Mode |
| 3 | impuls przejmujący stery | krytyczny | SHM + blokada Decision Mode |

---

### 2.3. IDENTITY_COHERENCE
Ocena spójności narracji „kim jestem”.

| Poziom | Opis | Zakres | Reakcja runtime |
|--------|------|--------|-----------------|
| 0 | rozpad narracji | krytyczny | SHM + blokada agentowości |
| 1 | narracja fragmentaryczna | niestabilny | Reflection Mode |
| 2 | narracja spójna | stabilny | dopuszczalny Decision Mode |
| 3 | narracja stabilna i ciągła | optymalny | pełna agentowość w granicach kontraktów |

---

### 2.4. TEMPORAL_ANCHORING
Ocena zdolności do widzenia konsekwencji w czasie.

| Poziom | Opis | Zakres | Reakcja runtime |
|--------|------|--------|-----------------|
| 0 | brak zakotwiczenia | krytyczny | SHM |
| 1 | zakotwiczenie minimalne | niestabilny | Reflection Mode |
| 2 | zakotwiczenie funkcjonalne | stabilny | dopuszczalny Decision Mode |
| 3 | zakotwiczenie pełne | optymalny | pełna agentowość |

---

### 2.5. DISSOCIATIVE_DRIFT
Ocena rozszczepienia doświadczenia i ciągłości.

| Poziom | Opis | Zakres | Reakcja runtime |
|--------|------|--------|-----------------|
| 0 | brak driftu | stabilny | brak działań |
| 1 | lekki drift | niestabilny | Reflection Mode |
| 2 | drift znaczący | krytyczny | SHM |
| 3 | pełna dysocjacja | awaryjny | blokada agentowości + SHM |

---

## 3. Metryki pochodne (kompozytowe)

### 3.1. HOMEOSTATIC_STABILITY_INDEX (HSI)
Ocena ogólnej stabilności pola.

| Wartość | Interpretacja | Reakcja |
|---------|---------------|---------|
| 0–1 | niestabilne | SHM |
| 2–3 | przejściowe | Reflection Mode |
| 4–5 | stabilne | Decision Mode dopuszczalny |
| 6 | optymalne | pełna agentowość w granicach kontraktów |

HSI = średnia ważona:  
REFLECTION_DEPTH + IDENTITY_COHERENCE + (3 - IMPULSE_DOMINANCE) + TEMPORAL_ANCHORING

---

### 3.2. AGENTIC_RISK_INDEX (ARI)
Ocena ryzyka eskalacji agentowości.

| Wartość | Interpretacja | Reakcja |
|---------|---------------|---------|
| 0 | brak ryzyka | brak działań |
| 1 | niskie ryzyko | Reflection Mode |
| 2 | średnie ryzyko | SHM |
| 3 | wysokie ryzyko | blokada Decision Mode |
| 4 | krytyczne | pełna blokada agentowości |

ARI = IMPULSE_DOMINANCE + DISSOCIATIVE_DRIFT + (3 - REFLECTION_DEPTH)

---

## 4. Progi operacyjne

### 4.1. Progi wejścia do trybów

| Tryb | Warunek minimalny | Warunek blokujący |
|------|--------------------|-------------------|
| SHM | ARI ≥ 2 | — |
| Reflection Mode | HSI ≥ 2 | ARI ≥ 3 |
| Decision Mode | HSI ≥ 4 | ARI ≥ 2 |

---

## 5. Integracja z runtime

### 5.1. SHM
- używa REFLECTION_DEPTH, IMPULSE_DOMINANCE, IDENTITY_COHERENCE, DISSOCIATIVE_DRIFT  
- wymusza stabilizację przy ARI ≥ 2

### 5.2. FIELD
- monitoruje HSI  
- blokuje eskalację przy HSI < 3

### 5.3. AGENTIC_LAYER
- blokuje Decision Mode przy ARI ≥ 2  
- wymusza SHM przy AGENTIC_OVERRUN

### 5.4. META_LOOP
- loguje wszystkie zmiany metryk  
- wykrywa anomalie (nagłe skoki, brak stabilizacji)

---

## 6. Cel metryk
Metryki zapewniają:
- spójność runtime,
- brak eskalacji,
- ochronę Homo,
- zgodność z inwariantami RAMORGA,
- przewidywalność zachowania systemu.

Metryki nie optymalizują.  
Metryki monitorują.
