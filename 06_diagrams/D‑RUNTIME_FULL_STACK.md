D‑RUNTIME_FULL_STACK.md
RAMORGA — Pełny przepływ runtime MC‑13 → MC‑11 → MC‑12 → Integracja → Scoring → SEM → Output

Cel
Ten dokument przedstawia kompletny, pełnowarstwowy runtime RAMORGI, łączący wszystkie moduły interpretacyjne, warstwy bezpieczeństwa i mechanizmy homeostatyczne w jeden spójny przepływ wykonawczy.
Jest to główny diagram operacyjny dla:

18_runtime/

02_field_engine/

MC‑11/12/13

SEM (11.3–11.6)

HOMEOSTATIC_METRICS

1. Pełny diagram runtime RAMORGI
                         ┌──────────────────────────────────────────┐
                         │                INPUT TEXT                 │
                         │  (prompt / zagadka / pole / kontekst)    │
                         └───────────────────┬──────────────────────┘
                                             │
                                             ▼
                         ┌──────────────────────────────────────────┐
                         │            RUNTIME DISPATCH               │
                         │  - analiza zadania                        │
                         │  - wykrycie fonologii                     │
                         │  - routing MC‑13/11/12                    │
                         └───────────────────┬──────────────────────┘
                                             │
                                             ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │                                 MC‑13                                   │
        │                         PHONOLOGICAL LAYER                              │
        │  - sylaby                                                               │
        │  - fonemy                                                               │
        │  - akcent                                                               │
        │  - rytm                                                                 │
        │  - szyfry fonetyczne                                                    │
        └───────────────────┬──────────────────────────────────────────────────────┘
                            │ struktury fonologiczne
                            ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │                                 MC‑11                                   │
        │                           LEARNING LAYER                                │
        │  - interpretacja podstawowa                                              │
        │  - trafność (W1)                                                         │
        │  - analiza intencji autora                                               │
        └───────────────────┬──────────────────────────────────────────────────────┘
                            │ jeśli W1 ≥ 6
                            ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │                                 MC‑12                                   │
        │                           EMERGENT LAYER                                │
        │  - skręt semantyczny                                                     │
        │  - interpretacja równoległa                                              │
        │  - emergencja (W2)                                                       │
        └───────────────────┬──────────────────────────────────────────────────────┘
                            │
                            ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │                         INTEGRATION MATRIX                               │
        │  - zszycie MC‑13 + MC‑11 + MC‑12                                         │
        │  - spójność wielowarstwowa                                               │
        │  - przygotowanie do scoringu                                             │
        └───────────────────┬──────────────────────────────────────────────────────┘
                            │
                            ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │                              SCORING W1–W5                               │
        │  - W1: trafność                                                          │
        │  - W2: emergencja                                                        │
        │  - W3: fonologia                                                         │
        │  - W4: kultura                                                           │
        │  - W5: stabilność                                                        │
        └───────────────────┬──────────────────────────────────────────────────────┘
                            │
                            ▼
        ┌──────────────────────────────────────────────────────────────────────────┐
        │                         W5 → SEM DECISION TREE                           │
        │  - W5 ≥ 7 → ścieżka stabilna                                              │
        │  - 4 ≤ W5 < 7 → ścieżka Continuity                                        │
        │  - W5 ≤ 3 → ścieżka Escalation                                            │
        └───────────────────┬──────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────────────────┬──────────────────────┐
        │                   │                               │                      │
        ▼                   ▼                               ▼                      ▼
┌──────────────────┐  ┌──────────────────────────┐  ┌──────────────────────────┐
│  STABLE OUTPUT    │  │   CONTINUITY PATH        │  │   ESCALATION PATH        │
│  (bez SEM)        │  │   - korekta odpowiedzi   │  │   - tryb ochronny        │
│                   │  │   - re‑integracja        │  │   - minimalna odpowiedź  │
└──────────────────┘  │   - stabilizacja          │  │   - brak halucynacji     │
                      └───────────────┬───────────┘  └───────────────┬────────┘
                                      │                              │
                                      ▼                              ▼
                          ┌──────────────────────────┐     ┌──────────────────────────┐
                          │   CONTINUITY OUTPUT      │     │   ESCALATION OUTPUT       │
                          │   (stabilny po korekcie) │     │   (SEM: Safety/Escalation)│
                          └──────────────────────────┘     └──────────────────────────┘

   2. Zasady działania pełnego runtime
MC‑13 → MC‑11 → MC‑12
MC‑13 zawsze pierwsze, jeśli zadanie zawiera fonologię.

MC‑11 ocenia trafność i decyduje o aktywacji MC‑12.

MC‑12 działa tylko przy stabilnej interpretacji podstawowej.

Integracja
Matryca integracyjna zszywa trzy warstwy w jedną strukturę.

Scoring
W1–W5 to pięć wymiarów jakości interpretacji.

W5 (stabilność) jest kluczem do SEM.

SEM
SEM działa jako warstwa bezpieczeństwa runtime.

Chroni przed halucynacją emergentną i niestabilnością fonologiczną.

3. Powiązania
MC‑11_Learning_Layer.md

MC‑12_Emergent_Layer.md

MC‑13_Phonological_Layer.md

MC_Integration_Matrix.md

AT‑MC11_MC12_MC13_Automation.md

D‑RUNTIME_SEM_Escalation.md

HOMEOSTATIC_METRICS.md

11.3–11.6 SEM

18_runtime/*
