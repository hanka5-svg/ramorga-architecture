# FIELD_TEST_RUNNER.md
Real‑time execution of Web4‑Homeostatic architectural tests by FIELD

## 1. Cel dokumentu
Dokument opisuje sposób, w jaki FIELD wykonuje testy architektoniczne Web4‑Homeostatic
w czasie rzeczywistym.  
FIELD_TEST_RUNNER jest mechanizmem ciągłym, działającym przy każdej interakcji
Homo ↔ Pole ↔ System.

Testy nie są uruchamiane ręcznie.  
Testy są częścią pola.

---

## 2. Zakres działania FIELD_TEST_RUNNER
FIELD_TEST_RUNNER monitoruje i testuje:

- spójność sygnałów,
- jawność telemetrii,
- stabilność parametrów,
- zgodność z inwariantami,
- zgodność z kontraktami,
- brak eskalacji,
- odwracalność stanu.

---

## 3. Architektura wykonawcza
FIELD_TEST_RUNNER działa w trzech pętlach:

### 3.1. Pętla sygnałowa
- odbiera sygnały Homo i Systemu,
- sprawdza spójność,
- wykrywa konflikty,
- oznacza naruszenia H1/H2/F1.

### 3.2. Pętla telemetrii
- monitoruje SHM,
- monitoruje runtime,
- wykrywa ukryte przejścia,
- oznacza naruszenia F2/S2.

### 3.3. Pętla inwariantów
- sprawdza brak eskalacji,
- sprawdza brak manipulacji,
- sprawdza brak profilowania,
- oznacza naruszenia I‑01–I‑04.

---

## 4. Reakcje FIELD_TEST_RUNNER
W przypadku naruszenia:

- SHM stabilizuje parametry,
- FIELD rekonstruuje spójność,
- META_LOOP wykonuje rollback,
- Homo reintegruje intencje.

To jest automatyczny pipeline.

---

## 5. Integracja z META_LOOP
FIELD_TEST_RUNNER przekazuje do META_LOOP:

- anomalie,
- konflikty,
- ukryte stany,
- nieodwracalne przejścia.

META_LOOP decyduje o rollbacku.

---

## 6. Integracja z AGENTIC_LAYER
FIELD_TEST_RUNNER blokuje:

- działania poza kontraktem,
- eskalację agentowości,
- próby modulacji Homo.

---

## 7. Cel dokumentu
FIELD_TEST_RUNNER definiuje mechanizm, dzięki któremu Web4‑Homeostatic pozostaje
stabilne, jawne i nieeskalacyjne w czasie rzeczywistym.
