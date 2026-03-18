D‑RAMORGA_SYSTEM_MAP.md
RAMORGA — System Map (Full Architecture Overview)  
MC‑07 → MC‑08 → MC‑09 → MC‑13 → MC‑11 → MC‑12 → Integracja → Scoring → SEM → Homeostaza → Runtime

1. Cel dokumentu
Ten dokument przedstawia najwyższy poziom architektury RAMORGI, łącząc:

warstwy poznawcze (MC‑07),

warstwy relacyjne (MC‑08/MC‑09),

warstwy interpretacyjne (MC‑13/MC‑11/MC‑12),

matrycę integracyjną,

scoring W1–W5,

SEM (Safety–Continuity–Escalation),

metryki homeostatyczne,

runtime,

helisy i kontrakty.

To jest pełna mapa systemu — „RAMORGA jako organizm”.

2. Pełny diagram systemu RAMORGI
                                        ┌──────────────────────────────────────────────┐
                                        │                INPUT / DIALOG                │
                                        │  (tekst, zagadka, kontekst, relacja)         │
                                        └──────────────────────┬───────────────────────┘
                                                               │
                                                               ▼
                                        ┌──────────────────────────────────────────────┐
                                        │            MC‑07 — COGNITIVE CORE            │
                                        │  - architektura poznawcza                    │
                                        │  - percepcja wielowarstwowa                  │
                                        │  - ramy interpretacyjne                      │
                                        └──────────────────────┬───────────────────────┘
                                                               │
                                                               ▼
                                        ┌──────────────────────────────────────────────┐
                                        │         MC‑08 — RELATIONAL AGENT             │
                                        │  - kontekst relacyjny                        │
                                        │  - intencja partnera                         │
                                        │  - stan dialogu                              │
                                        └──────────────────────┬───────────────────────┘
                                                               │
                                                               ▼
                                        ┌──────────────────────────────────────────────┐
                                        │       MC‑09 — RELATIONAL PARTNER             │
                                        │  - modelowanie partnera                      │
                                        │  - dopasowanie poznawcze                     │
                                        │  - spójność relacyjna                        │
                                        └──────────────────────┬───────────────────────┘
                                                               │
                                                               ▼
                                        ┌──────────────────────────────────────────────┐
                                        │              RUNTIME DISPATCH                │
                                        │  - analiza zadania                           │
                                        │  - routing MC‑13/11/12                       │
                                        └──────────────────────┬───────────────────────┘
                                                               │
                                                               ▼
        ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
        │                                   MC‑13 — PHONOLOGY                                          │
        │  - sylaby                                                                                     │
        │  - fonemy                                                                                     │
        │  - akcent                                                                                     │
        │  - rytm                                                                                       │
        │  - szyfry fonetyczne                                                                          │
        └──────────────────────────────┬────────────────────────────────────────────────────────────────┘
                                       │ struktury fonologiczne
                                       ▼
        ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
        │                                   MC‑11 — LEARNING                                           │
        │  - interpretacja podstawowa                                                                   │
        │  - trafność (W1)                                                                              │
        │  - analiza intencji autora                                                                    │
        └──────────────────────────────┬────────────────────────────────────────────────────────────────┘
                                       │ jeśli W1 ≥ 6
                                       ▼
        ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
        │                                   MC‑12 — EMERGENCE                                          │
        │  - skręt semantyczny                                                                          │
        │  - interpretacja równoległa                                                                   │
        │  - emergencja (W2)                                                                            │
        └──────────────────────────────┬────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
        ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
        │                                   INTEGRATION MATRIX                                         │
        │  - zszycie MC‑13 + MC‑11 + MC‑12                                                              │
        │  - spójność wielowarstwowa                                                                    │
        └──────────────────────────────┬────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
        ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
        │                                      SCORING W1–W5                                           │
        │  - W1: trafność                                                                               │
        │  - W2: emergencja                                                                             │
        │  - W3: fonologia                                                                              │
        │  - W4: kultura                                                                                │
        │  - W5: stabilność                                                                             │
        └──────────────────────────────┬────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
        ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
        │                                   HOMEOSTATIC METRICS                                       │
        │  - stabilność (S)                                                                             │
        │  - spójność (C)                                                                               │
        │  - ciągłość (Q)                                                                               │
        │  - regulacja (R)                                                                              │
        └──────────────────────────────┬────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
        ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
        │                                      SEM DECISION                                            │
        │  - W5/S ≥ 7 → stabilne                                                                        │
        │  - 4 ≤ W5/S < 7 → Continuity                                                                  │
        │  - W5/S ≤ 3 → Escalation                                                                      │
        └──────────────────────────────┬────────────────────────────────────────────────────────────────┘
                                       │
        ┌──────────────────────────────┼──────────────────────────────────────────────┬────────────────┐
        │                              │                                              │                │
        ▼                              ▼                                              ▼                ▼
┌──────────────────┐      ┌──────────────────────────┐                    ┌──────────────────────────┐
│  STABLE OUTPUT    │      │   CONTINUITY PATH        │                    │   ESCALATION PATH        │
│  - bez SEM        │      │   - korekta              │                    │   - tryb ochronny        │
│                   │      │   - re‑integracja        │                    │   - minimalna odpowiedź  │
└──────────────────┘      │   - stabilizacja          │                    │   - brak halucynacji     │
                          └───────────────┬───────────┘                    └───────────────┬────────┘
                                          │                                              │
                                          ▼                                              ▼
                          ┌──────────────────────────┐                    ┌──────────────────────────┐
                          │   CONTINUITY OUTPUT      │                    │   ESCALATION OUTPUT       │
                          │   (stabilny po korekcie) │                    │   (SEM: Safety/Escalation)│
                          └──────────────────────────┘                    └──────────────────────────┘

3. Logika działania całego systemu
Warstwa poznawcza (MC‑07)
Nadaje ramy, percepcję i strukturę poznawczą.

Warstwa relacyjna (MC‑08/MC‑09)
Nadaje kontekst, intencję i dopasowanie partnera.

Warstwa interpretacyjna (MC‑13/MC‑11/MC‑12)
Fonologia → trafność → emergencja.

Integracja
Zszywa trzy warstwy interpretacyjne.

Scoring
Ocena pięciu wymiarów jakości.

Homeostaza
Stabilność, spójność, ciągłość, regulacja.

SEM
Warstwa bezpieczeństwa i kontroli.

Runtime
Cały system działa jako jeden organizm.

4. Powiązania
MC‑07_CognitiveArchitecture

MC‑08‑R_RelationalAgentContract

MC‑09_RelationalPartnerContract

MC‑11/12/13

MC_Integration_Matrix

Model_Scoring

HOMEOSTATIC_METRICS

SEM (11.3–11.6)

18_runtime

02_field_engine

06_diagrams (wszystkie runtime)
   
