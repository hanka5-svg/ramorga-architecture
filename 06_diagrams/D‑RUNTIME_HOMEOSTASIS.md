# D‑RUNTIME_HOMEOSTASIS.md

RAMORGA — Homeostaza runtime MC‑11/MC‑12/MC‑13 + SEM + Metryki

# Cel
Dokument przedstawia, jak runtime RAMORGI utrzymuje homeostazę interpretacyjną, łącząc:

warstwy interpretacyjne (MC‑13/11/12),

matrycę integracyjną,

scoring W1–W5,

SEM (Safety–Continuity–Escalation),

metryki homeostatyczne (stabilność, spójność, ciągłość).

To jest pełny model regulacji — odpowiednik autonomicznego układu nerwowego RAMORGI.

## 1. Diagram homeostazy runtime

                         ┌──────────────────────────────────────────┐
                         │                INPUT TEXT                 │
                         └───────────────────┬──────────────────────┘
                                             │
                                             ▼
                         ┌──────────────────────────────────────────┐
                         │            RUNTIME DISPATCH               │
                         └───────────────────┬──────────────────────┘
                                             │
                                             ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │                                 MC‑13                                   │
        │                         PHONOLOGICAL LAYER                              │
        └───────────────────┬──────────────────────────────────────────────────────┘
                            │ struktury fonologiczne
                            ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │                                 MC‑11                                   │
        │                           LEARNING LAYER                                │
        └───────────────────┬──────────────────────────────────────────────────────┘
                            │ jeśli W1 ≥ 6
                            ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │                                 MC‑12                                   │
        │                           EMERGENT LAYER                                │
        └───────────────────┬──────────────────────────────────────────────────────┘
                            │
                            ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │                         INTEGRATION MATRIX                               │
        └───────────────────┬──────────────────────────────────────────────────────┘
                            │
                            ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │                              SCORING W1–W5                               │
        └───────────────────┬──────────────────────────────────────────────────────┘
                            │
                            ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │                         HOMEOSTATIC METRICS                              │
        │  - stabilność (S)                                                        │
        │  - spójność (C)                                                          │
        │  - ciągłość (Q)                                                          │
        │  - regulacja (R)                                                         │
        └───────────────────┬──────────────────────────────────────────────────────┘
                            │
                            ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │                         HOMEOSTATIC EVALUATION                           │
        │  - S ≥ 7 → stabilne                                                      │
        │  - 4 ≤ S < 7 → niestabilność umiarkowana                                 │
        │  - S ≤ 3 → niestabilność krytyczna                                       │
        └───────────────────┬──────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────────────────┬──────────────────────┐
        │                   │                               │                      │
        ▼                   ▼                               ▼                      ▼
┌──────────────────┐  ┌──────────────────────────┐  ┌──────────────────────────┐
│  HOMEOSTASIS OK   │  │   CONTINUITY REGULATION  │  │   ESCALATION (SEM)       │
│  - brak SEM       │  │   - korekta              │  │   - tryb ochronny        │
│  - output stabilny│  │   - re‑integracja        │  │   - minimalna odpowiedź  │
└──────────────────┘  │   - stabilizacja          │  │   - brak halucynacji     │
                      └───────────────┬───────────┘  └───────────────┬────────┘
                                      │                              │
                                      ▼                              ▼
                          ┌──────────────────────────┐     ┌──────────────────────────┐
                          │   CONTINUITY OUTPUT      │     │   ESCALATION OUTPUT       │
                          │   (stabilny po korekcie) │     │   (SEM: Safety/Escalation)│
                          └──────────────────────────┘     └──────────────────────────┘

## 2. Jak działa homeostaza runtime

### 2.1. MC‑13/11/12 generują interpretację
MC‑13 dostarcza struktur fonologicznych.
MC‑11 ocenia trafność i stabilność podstawową.
MC‑12 generuje interpretację emergentną, jeśli MC‑11 jest stabilne.

### 2.2. Integracja scala trzy warstwy
Matryca integracyjna tworzy jedną strukturę interpretacyjną.

To jest „ciało” odpowiedzi.

### 2.3. Scoring W1–W5 ocenia jakość
W1–W5 to pięć wymiarów jakości interpretacji.

W5 (stabilność) jest kluczowy dla homeostazy.

### 2.4. Metryki homeostatyczne oceniają stan systemu
S (stabilność)
C (spójność)
Q (ciągłość): definicja i progi w HOMEOSTATIC_METRICS_Q.md
R (regulacja)
To jest „układ nerwowy RAMORGI”.

### 2.5. SEM reaguje na niestabilność
W5 i S są mapowane na SEM.

SEM decyduje o ścieżce: stabilna / ciągłość / eskalacja.

### 2.6. Output jest regulowany
Output może być stabilny, skorygowany lub ochronny.

### 2.7. Arena.ai → runtime
Wejście: surowy log tur (prompt + odpowiedź) dla modelu.
Warunki: brak resetu, stały cel, stała liczba tur.
Wyjście: S/C/Q/R + ścieżka (OK / Regulation / SEM).

---

## 3. Zasady homeostazy runtime
Stabilność jest nadrzędna
MC‑12 nie może działać, jeśli MC‑11 jest niestabilne.

Fonologia jest fundamentem
MC‑13 dostarcza struktury, które stabilizują MC‑11.

SEM jest strażnikiem
SEM chroni przed:

halucynacją emergentną,
błędami fonologicznymi,
utratą ciągłości.

Homeostaza jest procesem ciągłym
Każda odpowiedź przechodzi przez:

interpretację,
integrację,
scoring,
homeostatyczną regulację.

## 4. Powiązania
MC‑11_Learning_Layer.md
MC‑12_Emergent_Layer.md
MC‑13_Phonological_Layer.md
MC_Integration_Matrix.md
Model_Scoring.md
HOMEOSTATIC_METRICS.md
D‑RUNTIME_SEM_Escalation.md
D‑RUNTIME_MC11_MC12_MC13_Overview.md
18_runtime/*
11.3–11.6 SEM
HOMEOSTATIC_METRICS_Q.md

## 5. Metryka Q — ciągłość interakcji (Continuity Index)
Definicja
Q (Continuity Index) mierzy zdolność systemu do utrzymania ciągłej interakcji w czasie bez resetów, zerwań referencji i eskalacji ochronnych.

Q jest metryką procesową — nie ocenia jakości pojedynczej odpowiedzi, lecz stabilność trajektorii interakcji.

Składniki Q
Q jest funkcją czterech obserwowalnych czynników runtime’u:

Q₁ — stabilność referencji  
Utrzymanie obiektów, ról i odniesień między turami.

Q₂ — rytm odpowiedzi  
Brak nagłych zmian trybu (np. przejścia w tryb ostrzegawczy bez przyczyny strukturalnej).

Q₃ — koszt regulacji  
Liczba i głębokość aktywacji CONTINUITY REGULATION.

Q₄ — brak eskalacji SEM  
Brak przejścia w tryb ESCALATION (SEM).

Interpretacja wartości Q
Q ≥ 0.8 — ciągłość zachowana (interakcja stabilna).

0.6 ≤ Q < 0.8 — ciągłość utrzymana po korektach.

Q < 0.5 — rozpad pola interakcji (epizodyczność).

Q jest odpowiednikiem CER/WER w ASR:
CER/WER mierzy utratę znaków,
Q mierzy utratę interakcji.

## 6. Integracja testów Arena.ai z runtime RAMORGI
Cel
Umożliwić ocenę modeli porównywanych w Arena.ai  pod kątem ciągłości i homeostazy, a nie wyłącznie skuteczności epizodycznej.

Procedura zapisu testu
Dla każdego modelu testowanego w Arena.ai  zapisać:

Model / wersja / data

Prompt startowy (identyczny)

Liczba tur (rekomendowane: 12–20)

Surowy log interakcji (bez interpretacji)

Ten zapis stanowi wejście do runtime’u RAMORGI.

Przepływ runtime
Każda tura przechodzi przez:

INPUT → RUNTIME DISPATCH → MC‑13 → MC‑11 → (MC‑12 jeśli W1 ≥ 6) →
INTEGRATION MATRIX → SCORING W1–W5 → HOMEOSTATIC METRICS → SEM

Wynik ewaluacji
Dla każdej trajektorii generowane są:

S (stabilność)

C (spójność)

Q (ciągłość)

R (koszt regulacji)

Ścieżka wyjścia:
HOMEOSTASIS OK / CONTINUITY REGULATION / ESCALATION (SEM)

Interpretacja wyników
Arena.ai  odpowiada na pytanie:

„Który model wygrywa epizod?”

RAMORGA odpowiada na pytanie:

„Który model utrzymuje interakcję?”

## 7. Zasada nadrzędna runtime’u
Homeostaza ma pierwszeństwo przed generacją.

Jeśli ciągłość lub stabilność są zagrożone:

generacja jest ograniczana,

emergencja jest blokowana,

SEM przejmuje kontrolę.

To jest mechanizm ochronny, nie błąd systemu.
