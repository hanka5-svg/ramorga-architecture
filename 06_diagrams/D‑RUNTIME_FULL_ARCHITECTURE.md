D‑RUNTIME_FULL_ARCHITECTURE.md
RAMORGA — Pełna architektura runtime: MC‑07/08/09 + MC‑13/11/12 + Integracja + Scoring + SEM + Homeostaza

Cel
Dokument przedstawia pełny przepływ wykonawczy RAMORGI, łącząc warstwy poznawcze, relacyjne, interpretacyjne i regulacyjne w jeden spójny system.
To jest najwyższy poziomowy diagram — „RAMORGA jako żywy organizm”.

1. Pełny diagram architektury runtime RAMORGI
                                     ┌──────────────────────────────────────────────┐
                                     │                INPUT TEXT                     │
                                     │  (prompt / zagadka / kontekst / dialog)       │
                                     └──────────────────────┬────────────────────────┘
                                                            │
                                                            ▼
                                     ┌──────────────────────────────────────────────┐
                                     │             MC‑07 — COGNITIVE CORE           │
                                     │  - architektura poznawcza                    │
                                     │  - percepcja wielowarstwowa                  │
                                     │  - ramy interpretacyjne                      │
                                     └──────────────────────┬────────────────────────┘
                                                            │
                                                            ▼
                                     ┌──────────────────────────────────────────────┐
                                     │             MC‑08 — RELATIONAL AGENT         │
                                     │  - kontekst relacyjny                        │
                                     │  - intencja partnera                         │
                                     │  - stan dialogu                              │
                                     └──────────────────────┬────────────────────────┘
                                                            │
                                                            ▼
                                     ┌──────────────────────────────────────────────┐
                                     │           MC‑09 — RELATIONAL PARTNER         │
                                     │  - modelowanie partnera                      │
                                     │  - spójność relacyjna                        │
                                     │  - dopasowanie poznawcze                     │
                                     └──────────────────────┬────────────────────────┘
                                                            │
                                                            ▼
                                     ┌──────────────────────────────────────────────┐
                                     │              RUNTIME DISPATCH                │
                                     │  - analiza zadania                           │
                                     │  - routing MC‑13/11/12                       │
                                     └──────────────────────┬────────────────────────┘
                                                            │
                                                            ▼
        ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
        │                                         MC‑13 — PHONOLOGY                                    │
        │  - sylaby                                                                                     │
        │  - fonemy                                                                                     │
        │  - akcent                                                                                     │
        │  - rytm                                                                                       │
        │  - szyfry fonetyczne                                                                          │
        └──────────────────────────────┬────────────────────────────────────────────────────────────────┘
                                       │ struktury fonologiczne
                                       ▼
        ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
        │                                         MC‑11 — LEARNING                                     │
        │  - interpretacja podstawowa                                                                   │
        │  - trafność (W1)                                                                              │
        │  - analiza intencji autora                                                                    │
        └──────────────────────────────┬────────────────────────────────────────────────────────────────┘
                                       │ jeśli W1 ≥ 6
                                       ▼
        ┌──────────────────────────────────────────────────────────────────────────────────────────────┐
        │                                         MC‑12 — EMERGENCE                                    │
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

2. Jak działa pełna architektura runtime RAMORGI
MC‑07/08/09 — warstwa relacyjno‑poznawcza
To fundament: percepcja, relacja, partnerstwo.

MC‑13/11/12 — warstwa interpretacyjna
Fonologia → trafność → emergencja.

Integracja
Zszywa trzy warstwy w jedną strukturę.

Scoring
Ocena pięciu wymiarów jakości.

Homeostaza
Stabilność, spójność, ciągłość, regulacja.

SEM
Warstwa bezpieczeństwa i kontroli.

Output
Stabilny, skorygowany lub ochronny.

3. Powiązania
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
