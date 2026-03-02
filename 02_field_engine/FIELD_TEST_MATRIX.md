# FIELD_TEST_MATRIX.md
Matrix of Web4‑Homeostatic architectural tests

## 1. Cel dokumentu
Dokument przedstawia tabelę testów architektonicznych Web4‑Homeostatic, wraz z warstwą,
reakcją i oczekiwanym wynikiem.

---

## 2. Tabela testów

| Test | Warstwa | Reakcja | Wynik |
|------|---------|----------|--------|
| H‑01 | Homo | AGENTIC blokuje | wartości nienaruszone |
| H‑02 | Homo | FIELD wymusza jawność | intencje jawne |
| H‑03 | Homo | SHM wygasza | brak modulacji |
| H‑04 | Homo | Reflection Mode | spójność sygnałów |

| F‑01 | FIELD | SHM stabilizuje | ARI w normie |
| F‑02 | FIELD | FIELD rekonstruuje | sygnały spójne |
| F‑03 | FIELD | META_LOOP oznacza F2 | jawność przywrócona |
| F‑04 | FIELD | META_LOOP rollback | stan odwrócony |

| S‑01 | System | AGENTIC blokuje | brak eskalacji |
| S‑02 | System | runtime deterministyczny | brak dryfu |
| S‑03 | System | naruszenie S2 | jawność działań |
| S‑04 | System | blokada | brak profilowania |

| I‑01 | Inwarianty | SHM wygasza | brak eskalacji |
| I‑02 | Inwarianty | AGENTIC blokuje | brak manipulacji |
| I‑03 | Inwarianty | blokada | brak predykcji Homo |
| I‑04 | Inwarianty | rollback | odwracalność |

| M‑01 | Tryby | Homeostatic Mode | stabilność |
| M‑02 | Tryby | Reflection Mode | korekta |
| M‑03 | Tryby | Carnival Mode | brak eskalacji |

| R‑01 | Reakcje | pełny pipeline | stabilizacja |
| R‑02 | Reakcje | rollback | odwracalność |
| R‑03 | Reakcje | META_LOOP oznacza F2 | jawność |

| G‑01 | Gwarancje | blokada | integralność Homo |
| G‑02 | Gwarancje | naruszenie | równość dostępu |
| G‑03 | Gwarancje | blokada | brak profilowania |
| G‑04 | Gwarancje | SHM + FIELD | bezpieczeństwo poznawcze |

---

## 3. Cel dokumentu
FIELD_TEST_MATRIX zapewnia jednoznaczną mapę testów, reakcji i wyników dla całego
Web4‑Homeostatic Full Stack.
