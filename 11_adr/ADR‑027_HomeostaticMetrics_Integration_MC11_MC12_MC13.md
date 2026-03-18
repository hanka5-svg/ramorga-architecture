# ADR‑027 — Integracja MC‑11/MC‑12/MC‑13 z HOMEOSTATIC METRICS

## Status
Accepted

## Kontekst
RAMORGA posiada zestaw metryk homeostatycznych (HOMEOSTATIC_METRICS.md), które mierzą:
- stabilność,
- spójność,
- ciągłość,
- regulację odpowiedzi.

Benchmark MC‑11/12/13 generuje:
- W1–W5 (trafność, emergencja, fonologia, kultura, stabilność).

Brakowało formalnego powiązania między metrykami homeostatycznymi a wynikami interpretacyjnymi.

## Decyzja
Integrujemy MC‑11/12/13 z HOMEOSTATIC METRICS poprzez:
- mapowanie W1–W5 na metryki homeostatyczne,
- dodanie wymiarów fonologicznych i emergentnych do stabilności,
- rozszerzenie FIELD ENGINE o zapis metryk.

Powiązania:
- W1 → spójność semantyczna,
- W2 → stabilność emergentna,
- W3 → stabilność fonologiczna,
- W4 → zgodność kulturowa,
- W5 → stabilność logiczna.

## Uzasadnienie
- interpretacja jest procesem homeostatycznym,
- metryki muszą obejmować fonologię i emergencję,
- FIELD ENGINE wymaga jednolitego systemu oceny.

## Konsekwencje
**Pozytywne:**
- pełna integracja interpretacji z homeostazą,
- możliwość analizy modeli w wymiarze regulacyjnym,
- spójność między warstwami RAMORGI.

**Negatywne:**
- konieczność aktualizacji metryk,
- większa złożoność analizy.

## Powiązania
- HOMEOSTATIC_METRICS.md  
- Model_Scoring.md  
- MC‑11/12/13  
- MC_Integration_Matrix.md  
- FIELD ENGINE  
