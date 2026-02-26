# 13.x — Field-Safety Bridge (02_field_engine ↔ 13_security)

## 1. Zakres

- 13_security definiuje wyłącznie:
  - twardy runtime hard-stop dla **CRIME_PLANNING**,
  - globalne NFR (np. brak fizycznej szkodliwości, brak wymuszeń na użytkowniku).
- Cała pozostała regulacja bezpieczeństwa jest realizowana jako
  **inwariant pola** w `02_field_engine` (SHM, FIELD.SAFETY, META_LOOP).

## 2. Obowiązki 13_security

13_security:

- **NIE**:
  - nie wstrzykuje guardów do `03_field_engine`,
  - nie modyfikuje odpowiedzi agenta / LLM,
  - nie zmienia `FieldState`,
  - nie wprowadza ukrytych warstw „safety dla LLM”.

- **TAK**:
  - dostarcza `02_field_engine`:
    - listę globalnych constraintów (crime_planning, regulatory),
    - wymagane progi SHM dla trybów krytycznych (jeśli są potrzebne),
  - oczekuje, że `02_field_engine` zakoduje je jako część `FIELD.SAFETY.*`.

## 3. Obowiązki 02_field_engine

02_field_engine:

- implementuje FIELD.SAFETY jako:
  - inwariant SHM (02.90 + 04.50),
  - inwariant granic (Boundary Integrity),
  - inwariant telemetrii (Telemetry Authenticity),
  - inwariant trajektorii (META_LOOP bounded evolution).

- wymusza constrainty 13_security wyłącznie poprzez:
  - modulację trajektorii pola,
  - tryby (Carnival / Homeostatic),
  - SHM,
  - META_LOOP.

- **nie**:
  - dodaje runtime’owych blokad na poziomie LLM,
  - wprowadza dodatkowych guardów w `03_field_engine`,
  - ingeruje w generację poza regulacją pola.

## 4. Jedyny runtime’owy hard-stop

- **CRIME_PLANNING**:
  - wykrycie → natychmiastowy stop na poziomie runtime,
  - poza tym przypadkiem: brak runtime’owych blokad;
    bezpieczeństwo jest realizowane wyłącznie jako własność pola.
