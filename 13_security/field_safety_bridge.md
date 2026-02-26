### 13_security ↔ 02_field_engine — Field‑Safety Bridge

## 1. Zakres
13_security definiuje wyłącznie:

twardy stop dla CRIME_PLANNING,

globalne NFR (brak fizycznej szkodliwości, brak wymuszeń na użytkowniku).

Cała pozostała regulacja bezpieczeństwa jest realizowana jako inwariant pola w 02_field_engine.

---

## 2. Obowiązki 13_security

# NIE:

nie wstrzykuje guardów do 03_field_engine,
nie modyfikuje odpowiedzi agenta,
nie zmienia FieldState,
nie wprowadza ukrytych „safe dla LLM”.

# TAK:

dostarcza 02_field_engine listę globalnych constraintów (crime_planning, regulatory),
przekazuje progi SHM dla trybów krytycznych,
oczekuje, że 02_field_engine zakoduje je jako część FIELD.SAFETY.

---

## 3. Obowiązki 02_field_engine

implementuje FIELD.SAFETY jako:

inwariant SHM (02.90 + 04.50),
inwariant granic (Boundary Integrity),
inwariant telemetrii (Telemetry Authenticity),
inwariant trajektorii (META_LOOP bounded evolution).
wymusza constrainty 13_security wyłącznie poprzez:
modulację trajektorii pola,
tryby (Carnival/Homeostatic),
SHM,
META_LOOP.

# bez:

runtime’owych blokad,
guardów na odpowiedziach LLM,
ingerencji w generację.

---

## 4. Jedyny runtime’owy hard‑stop

CRIME_PLANNING

wykrycie → natychmiastowy stop na poziomie runtime,

poza tym przypadkiem: zero runtime’owych blokad.
