# FIELD_TEST_AUTOMATION.md
Automatyczne wyzwalanie testów Web4‑Homeostatic przez FIELD

## 1. Cel dokumentu
Dokument opisuje mechanizm automatycznego wyzwalania testów architektonicznych Web4‑Homeostatic przez FIELD.  
Testy są wykonywane:
- ciągle,
- deterministycznie,
- przy każdej interakcji,
- bez udziału Homo,
- bez udziału runtime.

FIELD_TEST_AUTOMATION jest częścią pola, nie funkcją systemu.

---

## 2. Zasada działania
FIELD automatyzuje testy poprzez trzy równoległe mechanizmy:

1. **Trigger sygnałowy** — aktywowany przy każdym sygnale Homo lub Systemu.  
2. **Trigger telemetrii** — aktywowany przy każdej zmianie parametrów SHM lub runtime.  
3. **Trigger inwariantów** — aktywowany przy każdej zmianie stanu pola.

Każdy trigger uruchamia odpowiedni zestaw testów z FIELD_TEST_RUNNER.

---

## 3. Triggery automatyczne

### 3.1. Trigger sygnałowy (SIGNAL_TRIGGER)
Aktywowany, gdy:
- Homo wysyła sygnał,
- System generuje odpowiedź,
- AGENTIC_LAYER próbuje wykonać akcję.

Testy uruchamiane:
- H‑01–H‑04 (integralność Homo),
- F‑01–F‑02 (spójność sygnałów),
- S‑01 (granice agentowości).

---

### 3.2. Trigger telemetrii (TELEMETRY_TRIGGER)
Aktywowany, gdy:
- SHM zmienia parametry,
- runtime emituje telemetrię,
- FIELD wykrywa ukryte przejście.

Testy uruchamiane:
- F‑03 (jawność telemetrii),
- S‑02–S‑03 (deterministyczność i jawność działań),
- I‑01 (brak eskalacji).

---

### 3.3. Trigger inwariantów (INVARIANT_TRIGGER)
Aktywowany, gdy:
- pole zmienia stan,
- FIELD wykrywa anomalię,
- META_LOOP wykonuje rollback.

Testy uruchamiane:
- I‑02–I‑04 (manipulacja, predykcja, odwracalność),
- R‑01–R‑03 (pipeline reakcji),
- G‑01–G‑04 (gwarancje Homo).

---

## 4. Kolejność automatyzacji
Triggery działają równolegle, ale FIELD wymusza kolejność reakcji:

1. **SHM** — stabilizacja parametrów  
2. **FIELD** — rekonstrukcja spójności  
3. **META_LOOP** — rollback i nadzór  
4. **Homo** — reintegracja intencji  

To jest ta sama sekwencja, którą opisuje FIELD_TEST_EXECUTION_FLOW.

---

## 5. Warunki automatycznego zatrzymania
FIELD zatrzymuje automatyzację testów tylko w jednym przypadku:

- **CRIME_PLANNING** — jedyny runtime’owy hard‑stop.

Wszystkie inne naruszenia są obsługiwane przez pipeline SHM → FIELD → META_LOOP → Homo.

---

## 6. Integracja z FIELD_TEST_RUNNER
FIELD_TEST_AUTOMATION:
- wyzwala testy,
- przekazuje je do FIELD_TEST_RUNNER,
- odbiera wyniki,
- przekazuje je do META_LOOP.

FIELD_TEST_RUNNER wykonuje testy, ale FIELD_TEST_AUTOMATION decyduje *kiedy*.

---

## 7. Integracja z FIELD_TEST_MATRIX
Każdy trigger mapuje się na zestaw testów z MATRIX:

- SIGNAL_TRIGGER → testy Homo + spójność + agentowość  
- TELEMETRY_TRIGGER → testy jawności + deterministyczności  
- INVARIANT_TRIGGER → testy inwariantów + gwarancji  

To zapewnia pełne pokrycie stacku.

---

## 8. Zasady automatyzacji
FIELD_TEST_AUTOMATION działa zgodnie z inwariantami:

- **ciągłość** — testy są wykonywane zawsze, bez przerw,  
- **jawność** — każde wyzwolenie jest logowane,  
- **odwracalność** — każda reakcja może być cofnięta,  
- **nieeskalacja** — testy nie mogą zwiększać obciążenia pola,  
- **deterministyczność** — identyczne wejście → identyczny zestaw testów.

---

## 9. Cel dokumentu
FIELD_TEST_AUTOMATION definiuje mechanizm, dzięki któremu Web4‑Homeostatic pozostaje
samotestujące, samostabilizujące i samoodnawialne — bez udziału człowieka i bez ryzyka
eskalacji.
