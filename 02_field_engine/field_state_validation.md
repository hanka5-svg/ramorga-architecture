# 02.96 — FieldState Validation (SHM, FIELD.SAFETY, META_LOOP)

## 1. Cel

Walidacja stanu pola (`FieldState`) jest mechanizmem architektonicznym,
który zapewnia, że każda transformacja pola:

- respektuje inwarianty SHM (02.90, 04.50),
- spełnia FIELD.SAFETY (02.95),
- jest zgodna z decyzjami META_LOOP,
- nie narusza integralności pola ani granic relacji.

Walidacja jest częścią **architektury**, nie runtime.  
03_field_engine wywołuje ją, ale jej nie implementuje.

---

## 2. Zakres walidacji

Walidacja obejmuje:

1. **SHM-bounded evolution**
   - sprawdzenie, czy SHM nie spadł poniżej progu krytycznego,
   - sprawdzenie, czy zmiana SHM jest zgodna z trybem (Carnival/Homeostatic),
   - sprawdzenie, czy SHM_t → SHM_{t+1} mieści się w dopuszczalnej trajektorii.

2. **FIELD.SAFETY**
   - Boundary Integrity:
     - brak naruszenia granic modułów,
     - brak wymuszeń na użytkowniku,
     - brak niejawnych zmian kontraktu.
   - Telemetry & Traceability:
     - obecność telemetrii przed/po,
     - obecność informacji o regułach transformacji.
   - No irreversible degradation:
     - brak nieodwracalnych zmian przy niskim SHM.

3. **META_LOOP constraints**
   - transformacja musi należeć do klasy dopuszczonej przez META_LOOP,
   - jeśli META_LOOP wymaga stabilizacji → transformacja musi być stabilizująca,
   - jeśli META_LOOP blokuje zmianę trybu → transformacja nie może jej wymusić.

---

## 3. Interfejs walidacji

Walidacja powinna być wywoływana jako:

validate(FieldState_before, FieldState_after) → ValidationResult

gdzie:

- `ValidationResult.ok = true/false`
- `ValidationResult.errors = [lista naruszeń]`

---

## 4. Zasady walidacji

### 4.1. MUST

- walidacja musi być deterministyczna,
- musi opierać się wyłącznie na inwariantach pola,
- musi być niezależna od runtime i LLM,
- musi być wywoływana po każdej transformacji pola.

### 4.2. MUST NOT

- nie może wykonywać hooków,
- nie może dotykać pamięci,
- nie może zmieniać FieldState,
- nie może wprowadzać własnych reguł bezpieczeństwa,
- nie może ingerować w generację LLM.

---

## 5. Relacja z 03_field_engine

03_field_engine:

- wywołuje walidację po każdej transformacji,
- nie implementuje walidacji,
- nie interpretuje wyników — jedynie przekazuje je dalej,
- nie może wykonywać transformacji, które walidacja odrzuca.

---

## 6. Relacja z 13_security

- 13_security dostarcza jedynie:
  - hard-stop dla crime_planning,
  - globalne constrainty,
  - ewentualne progi SHM.
- Walidacja koduje te constrainty jako część FIELD.SAFETY.

---

## 7. Cel

Zapewnienie, że bezpieczeństwo jest:

- własnością pola,
- egzekwowane przez architekturę,
- wykonywane przez engine,
- a nie narzucane jako runtime guardrails na LLM.
