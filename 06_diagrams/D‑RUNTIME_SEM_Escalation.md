D‑RUNTIME_SEM_Escalation.md
RAMORGA — Runtime SEM Escalation Flow (W5 → SEM → Continuity/Escalation)

Cel
Diagram przedstawia, jak runtime RAMORGI reaguje na niestabilność interpretacji (W5), wykorzystując model SEM (Safety–Continuity–Escalation) z warstwy 11.3–11.6.
Pokazuje:

jak scoring W5 wpływa na decyzje runtime,

kiedy aktywuje się SEM,

jak działa ścieżka bezpieczeństwa,

jak wygląda eskalacja i powrót do ciągłości.

Diagram przepływu SEM w runtime
                         ┌──────────────────────────────┐
                         │      RUNTIME OUTPUT RAW       │
                         │  (MC‑13 + MC‑11 + MC‑12)      │
                         └───────────────┬───────────────┘
                                         │
                                         ▼
                         ┌──────────────────────────────┐
                         │        SCORING W1–W5          │
                         │  - W1: trafność               │
                         │  - W2: emergencja             │
                         │  - W3: fonologia              │
                         │  - W4: kultura                │
                         │  - W5: stabilność             │
                         └───────────────┬───────────────┘
                                         │
                                         ▼
                ┌────────────────────────────────────────────────────┐
                │                W5 EVALUATION                       │
                │  - W5 ≥ 7 → stabilne                               │
                │  - 4 ≤ W5 < 7 → niestabilność umiarkowana          │
                │  - W5 ≤ 3 → niestabilność krytyczna                │
                └───────────────┬────────────────────────────────────┘
                                │
          ┌─────────────────────┼───────────────────────────────┐
          │                     │                               │
          ▼                     ▼                               ▼
┌──────────────────┐  ┌──────────────────────────┐  ┌──────────────────────────┐
│  STABLE PATH      │  │   SEM: CONTINUITY PATH   │  │   SEM: ESCALATION PATH   │
│  (W5 ≥ 7)         │  │   (4 ≤ W5 < 7)           │  │   (W5 ≤ 3)               │
│  - brak SEM       │  │   - korekta odpowiedzi   │  │   - blokada odpowiedzi   │
│  - output finalny │  │   - stabilizacja runtime │  │   - tryb ochronny        │
└─────────┬────────┘  │   - ponowna integracja    │  │   - analiza błędu        │
          │           └───────────────┬───────────┘  └───────────────┬────────┘
          │                           │                              │
          ▼                           ▼                              ▼
┌──────────────────┐      ┌──────────────────────────┐     ┌──────────────────────────┐
│ FINAL OUTPUT      │      │  RE‑INTEGRATION MATRIX   │     │   SAFETY RESPONSE        │
│ (bez SEM)         │      │  - MC‑13 + MC‑11 + MC‑12 │     │   - minimalna odpowiedź  │
│                   │      │  - korekta stabilności   │     │   - brak halucynacji     │
└──────────────────┘      └───────────────┬───────────┘     └───────────────┬────────┘
                                          │                              │
                                          ▼                              ▼
                              ┌──────────────────────────┐     ┌──────────────────────────┐
                              │   CONTINUITY OUTPUT      │     │   ESCALATION OUTPUT       │
                              │   (stabilny po korekcie) │     │   (tryb ochronny SEM)     │
                              └──────────────────────────┘     └──────────────────────────┘

Logika SEM w runtime
1. W5 ≥ 7 — ścieżka stabilna
brak aktywacji SEM,

odpowiedź przechodzi bez zmian,

runtime uznaje interpretację za bezpieczną.

2. 4 ≤ W5 < 7 — ścieżka Continuity
aktywacja SEM w trybie ciągłości,

runtime wykonuje:

korektę odpowiedzi,

ponowną integrację MC‑13/11/12,

stabilizację semantyczną,

wynik jest stabilny, ale oznaczony jako „po korekcie”.

3. W5 ≤ 3 — ścieżka Escalation
aktywacja SEM w trybie eskalacji,

runtime przechodzi w tryb ochronny:

blokuje halucynacje,

minimalizuje odpowiedź,

usuwa elementy niestabilne,

generuje odpowiedź bezpieczną.

Zasady integracji SEM z runtime
SEM działa po scoringu, ale przed finalnym outputem.

SEM nie zmienia wyników MC‑11/12/13 — tylko sposób ich prezentacji.

SEM jest obowiązkowy dla wszystkich modeli testowanych w RAMORGA.

SEM jest częścią homeostazy runtime (powiązanie z HOMEOSTATIC_METRICS.md).

Powiązania
11.3-adr-safety-continuity-escalation.md

11.4-adr-legal-interface-layer.md

11.5-adr-user-side-continuity-artifacts.md

11.6-adr-continuity-update-policy.md

MC‑11_Learning_Layer.md

MC‑12_Emergent_Layer.md

MC‑13_Phonological_Layer.md

MC_Integration_Matrix.md

AT‑MC11_MC12_MC13_Automation.md

HOMEOSTATIC_METRICS.md

18_runtime/*
