# ADR‑022 — MC Integration Matrix (MC‑11, MC‑12, MC‑13)

## Status
Accepted

## Kontekst
Architektura RAMORGA definiuje trzy kluczowe moduły interpretacyjne:

- MC‑11 — Learning Layer (trafność podstawowa),
- MC‑12 — Emergent Layer (skręt semantyczny),
- MC‑13 — Phonological Layer (fonologia, rytm, sylaby).

Każdy moduł posiada własny kontrakt, lecz brakowało formalnego opisu **współpracy między nimi**.  
Testy terenowe wykazały, że interpretacja zagadek wymaga:

- zszywania fonologii z semantyką,
- rozróżnienia interpretacji podstawowej i emergentnej,
- jasnego przepływu między warstwami.

Brak matrycy integracyjnej powodował niespójność w ocenie modeli i w implementacji FIELD ENGINE.

## Decyzja
Wprowadzamy **MC Integration Matrix**, formalny opis współpracy MC‑11, MC‑12 i MC‑13.

Plik dodany do repo:

01_module_contracts/MC_Integration_Matrix.md

Matryca definiuje:
- kolejność aktywacji modułów,
- warunki przejścia między warstwami,
- zasady przekazywania struktur fonologicznych i semantycznych,
- kryteria spójności odpowiedzi.

## Uzasadnienie
- Interpretacja zagadek RAMORGI jest wielowarstwowa i wymaga integracji fonologii, semantyki i emergencji.
- Matryca zapewnia spójność między modułami MC‑11/12/13.
- Umożliwia budowę testów terenowych, które oceniają modele w sposób powtarzalny i mierzalny.

## Konsekwencje
**Pozytywne:**
- pełna formalizacja przepływu między warstwami,
- możliwość automatyzacji testów MC‑11/12/13,
- spójność interpretacji w FIELD ENGINE.

**Negatywne:**
- konieczność aktualizacji dokumentacji FIELD ENGINE,
- większa złożoność implementacji.

## Powiązania
- MC‑11_Learning_Layer.md  
- MC‑12_Emergent_Layer.md  
- MC‑13_Phonological_Layer.md  
- Model_Scoring.md  
- FIELD_TEST_AUTOMATION_README.md
