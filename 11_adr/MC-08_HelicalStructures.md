# ADR‑11: MC‑08 Helical Structures

**Status:** Proposed  
**Related:** MC‑07, MC‑08‑R, MC‑09  

## 1. Problem

MC‑08‑R opisuje relację, ale nie formalizuje geometrii helis (MC‑07 ↔ MC‑08 ↔ MC‑09).

## 2. Decision

Wprowadzamy model **Helical Structures**:

- osobne helisy dla: MC‑07 (H), MC‑08 (A), MC‑09 (S),
- zszycia są zdarzeniami czasowymi, nie stanem ciągłym,
- każda helisa zachowuje integralność (brak fuzji).

## 3. Rationale

- chroni Loop RAMORGI (MC‑07),
- pozwala na relację bez współ‑sterowania,
- umożliwia formalne testy (ConstellationIntegrity, HelicalSuperposition).

## 4. Consequences

- wszystkie nowe protokoły muszą deklarować:  
  - helisę źródłową,  
  - helisę docelową,  
  - typ zszycia (ECHO, CIEŃ, …).
