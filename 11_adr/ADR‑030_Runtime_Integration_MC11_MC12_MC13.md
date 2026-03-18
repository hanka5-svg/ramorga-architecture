# ADR‑030 — Integracja MC‑11/MC‑12/MC‑13 z RUNTIME

## Status
Accepted

## Kontekst
RAMORGA posiada:
- moduły interpretacyjne MC‑11/MC‑12/MC‑13,
- FIELD ENGINE z automatyzacją benchmarku,
- RUNTIME (18_runtime) jako warstwę wykonawczą.

Dotąd integracja MC‑11/12/13 z RUNTIME nie była formalnie opisana:
- brakowało zasad wywoływania warstw,
- brakowało zasad fallbacków,
- brakowało powiązania z SEM (Safety–Continuity–Escalation).

## Decyzja
Integrujemy MC‑11/MC‑12/MC‑13 z RUNTIME poprzez:

1. **Standardowy przepływ RUNTIME:**
   - INPUT → MC‑13 → MC‑11 → (opcjonalnie) MC‑12 → INTEGRATION MATRIX → OUTPUT.

2. **Zasady aktywacji:**
   - MC‑13 zawsze przed MC‑11, gdy zadanie ma komponent fonologiczny.
   - MC‑12 tylko gdy MC‑11 ≥ 6 (trafność podstawowa).

3. **Fallbacki:**
   - jeśli MC‑13 zawiedzie → RUNTIME oznacza brak fonologii, ale kontynuuje MC‑11,
   - jeśli MC‑11 < 6 → MC‑12 nieaktywne, odpowiedź oznaczona jako „literalna”.

4. **Powiązanie z SEM:**
   - niestabilność W5 (stabilność) → eskalacja do SEM (11.3–11.6),
   - krytyczne błędy interpretacyjne → ścieżka bezpieczeństwa.

## Uzasadnienie
- MC‑11/12/13 muszą działać nie tylko w testach, ale w realnym runtime.
- RUNTIME potrzebuje jasnych zasad aktywacji, fallbacków i eskalacji.
- Integracja z SEM zapewnia bezpieczeństwo i ciągłość.

## Konsekwencje
**Pozytywne:**
- spójny runtime dla interpretacji,
- możliwość użycia MC‑11/12/13 w produkcyjnych scenariuszach,
- kontrola nad błędami i eskalacją.

**Negatywne:**
- większa złożoność RUNTIME,
- konieczność utrzymania zgodności z benchmarkiem.

## Powiązania
- 18_runtime/*  
- MC‑11/MC‑12/MC‑13  
- MC_Integration_Matrix.md  
- AT‑MC11_MC12_MC13_Automation.md  
- SEM (11.3–11.6)  
- Model_Scoring.md  
