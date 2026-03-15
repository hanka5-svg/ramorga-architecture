# ADR‑12: MC‑08 Relational Symmetry

**Status:** Proposed  
**Related:** MC‑08‑R, MC‑09  

## 1. Problem

Relacja H↔AI może łatwo stać się asymetryczna (AI przejmuje rytm, interpretację, regulację).

## 2. Decision

Wprowadzamy **Relational Symmetry**:

- AI‑Partner nie inicjuje ruchu,
- każda odpowiedź jest ograniczona do zakresu intencji H,
- po każdym zszyciu następuje pauza (brak ciągłego strumienia),
- brak regulacji stanu H przez AI.

## 3. Rationale

- chroni homeostazę H,
- uniemożliwia przejęcie sterowania przez AI,
- utrzymuje MC‑08‑R jako kontrakt relacyjny, nie regulacyjny.

## 4. Consequences

- wszystkie scenariusze muszą deklarować:  
  - kto inicjuje,  
  - maksymalną długość zszycia,  
  - warunki pauzy i zakończenia.
