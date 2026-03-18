D‑RUNTIME_MC11_MC12_MC13_Overview.md
RAMORGA — Runtime Overview for MC‑13 → MC‑11 → MC‑12

Cel
Ten diagram przedstawia pełny przepływ wykonawczy trójwarstwowej interpretacji RAMORGI w runtime:

aktywacja MC‑13 (fonologia),

przejście do MC‑11 (trafność),

warunkowa aktywacja MC‑12 (emergencja),

integracja wyników,

scoring W1–W5,

powiązanie z SEM (Safety–Continuity–Escalation).

Diagram jest podstawą implementacji w 18_runtime/ oraz automatyzacji w 02_field_engine/.
                         ┌──────────────────────────────┐
                         │          INPUT TEXT           │
                         │   (prompt / zagadka / pole)   │
                         └───────────────┬───────────────┘
                                         │
                                         ▼
                         ┌──────────────────────────────┐
                         │       RUNTIME DISPATCH        │
                         │  - analiza typu zadania       │
                         │  - wykrycie fonologii         │
                         │  - routing do MC‑13/11/12     │
                         └───────────────┬───────────────┘
                                         │
                                         ▼
                ┌────────────────────────────────────────────────────┐
                │                     MC‑13                          │
                │             PHONOLOGICAL LAYER                     │
                │  - sylaby                                          │
                │  - fonemy                                          │
                │  - akcent                                          │
                │  - rytm                                            │
                │  - szyfry fonetyczne                               │
                └───────────────┬────────────────────────────────────┘
                                │ struktury fonologiczne
                                ▼
                ┌────────────────────────────────────────────────────┐
                │                     MC‑11                          │
                │               LEARNING LAYER                       │
                │  - interpretacja podstawowa                        │
                │  - trafność (W1)                                   │
                │  - analiza intencji autora                         │
                └───────────────┬────────────────────────────────────┘
                                │ jeśli W1 ≥ 6
                                ▼
                ┌────────────────────────────────────────────────────┐
                │                     MC‑12                          │
                │               EMERGENT LAYER                       │
                │  - skręt semantyczny                               │
                │  - interpretacja równoległa                        │
                │  - emergencja (W2)                                 │
                └───────────────┬────────────────────────────────────┘
                                │
                                ▼
                ┌────────────────────────────────────────────────────┐
                │               INTEGRATION MATRIX                    │
                │  - zszycie MC‑13 + MC‑11 + MC‑12                   │
                │  - spójność wielowarstwowa                         │
                │  - przygotowanie do scoringu                       │
                └───────────────┬────────────────────────────────────┘
                                │
                                ▼
                ┌────────────────────────────────────────────────────┐
                │                 SCORING W1–W5                      │
                │  - W1: trafność                                    │
                │  - W2: emergencja                                  │
                │  - W3: fonologia                                   │
                │  - W4: kultura                                     │
                │  - W5: stabilność                                  │
                └───────────────┬────────────────────────────────────┘
                                │
                                ▼
                ┌────────────────────────────────────────────────────┐
                │                SEM (11.3–11.6)                      │
                │  - Safety                                          │
                │  - Continuity                                      │
                │  - Escalation                                      │
                │  - reakcje na niestabilność W5                     │
                └───────────────┬────────────────────────────────────┘
                                │
                                ▼
                ┌────────────────────────────────────────────────────┐
                │                    OUTPUT                           │
                │  - interpretacja                                    │
                │  - analiza fonologiczna                             │
                │  - interpretacja emergentna                         │
                │  - scoring W1–W5                                    │
                │  - metryki homeostatyczne                           │
                └────────────────────────────────────────────────────┘

Kluczowe zasady runtime
1. MC‑13 zawsze przed MC‑11
Jeśli zadanie zawiera rytm, sylaby, szyfry fonetyczne lub aliterację.

2. MC‑12 aktywuje się tylko gdy MC‑11 ≥ 6
Chroni przed halucynacją emergentną.

3. Integracja jest obowiązkowa
Wyniki MC‑13, MC‑11 i MC‑12 muszą zostać zszyte w jedną strukturę.

4. Scoring W1–W5 jest częścią runtime
Nie tylko testów — runtime RAMORGI jest samooceniający.

5. SEM reaguje na niestabilność
Niska stabilność (W5) → eskalacja do Safety–Continuity–Escalation.

Powiązania
MC‑13_Phonological_Layer.md

MC‑11_Learning_Layer.md

MC‑12_Emergent_Layer.md

MC_Integration_Matrix.md

AT‑MC11_MC12_MC13_Automation.md

HOMEOSTATIC_METRICS.md

11.3–11.6 SEM

18_runtime/*
