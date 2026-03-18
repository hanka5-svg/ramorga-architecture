# ADR‑021 — MC‑13 Phonological Layer

## Status
Accepted

## Kontekst
Zagadki RAMORGI często opierają się na:
- sylabach,
- fonemach,
- rytmie,
- szyfrach fonetycznych.

Modele LLM nie posiadają natywnej fonologii, co prowadzi do błędów interpretacyjnych w MC‑11 i MC‑12.  
Brakowało formalnego modułu opisującego warstwę fonologiczną.

## Decyzja
Wprowadzamy moduł **MC‑13 — Phonological Layer**, odpowiedzialny za:
- sylabizację,
- segmentację fonemów,
- analizę akcentu,
- analizę rytmu,
- wykrywanie szyfrów fonetycznych,
- integrację fonologii z MC‑11 i MC‑12.

Plik dodany do repo:

01_module_contracts/MC‑13_Phonological_Layer.md


## Uzasadnienie
- MC‑13 formalizuje warstwę fonologiczną niezbędną do interpretacji zagadek.
- Umożliwia ocenę modeli pod kątem fonetyki.
- Oddziela fonologię od semantyki i emergencji.

## Konsekwencje
- pełna trójwarstwowa interpretacja (MC‑11 + MC‑12 + MC‑13),
- możliwość budowy benchmarku fonologicznego,
- konieczność aktualizacji FIELD ENGINE.

## Powiązania
- MC‑13_Phonological_Layer.md  
- MC‑12_Emergent_Layer.md  
- MC_Integration_Matrix.md  
- Model_Scoring.md  
