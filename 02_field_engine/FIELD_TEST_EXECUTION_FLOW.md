# FIELD_TEST_EXECUTION_FLOW.md
Execution pipeline for Web4‑Homeostatic architectural tests

## 1. Cel dokumentu
Dokument opisuje sekwencję wykonywania testów architektonicznych Web4‑Homeostatic.
Pipeline jest deterministyczny i zawsze przebiega w tej samej kolejności.

---

## 2. Pipeline testowy

### 2.1. Etap 1 — SHM (Stabilizacja)
- wykrywa przeciążenie,
- wygasza impulsy,
- stabilizuje parametry,
- blokuje eskalację.

Warunek przejścia:
- ARI ≤ 2,
- brak eskalacji.

---

### 2.2. Etap 2 — FIELD (Rekonstrukcja)
- sprawdza spójność sygnałów,
- wymusza jawność,
- synchronizuje telemetrię,
- oznacza naruszenia F1/F2.

Warunek przejścia:
- HSI ≥ 2,
- brak konfliktów pola.

---

### 2.3. Etap 3 — META_LOOP (Rollback)
- analizuje trajektorię,
- wykrywa anomalie,
- wykonuje rollback,
- przywraca stabilny stan.

Warunek przejścia:
- brak anomalii,
- spójna telemetria.

---

### 2.4. Etap 4 — Homo (Reintegracja)
- potwierdza intencje,
- przywraca integralność narracji,
- stabilizuje kierunek interakcji.

Warunek zakończenia:
- pole stabilne,
- system w granicach kontraktów.

---

## 3. Zasady pipeline
- pipeline jest odwracalny,
- pipeline jest jawny,
- pipeline jest niehierarchiczny,
- pipeline jest automatyczny.

---

## 4. Cel dokumentu
FIELD_TEST_EXECUTION_FLOW definiuje deterministyczną sekwencję testów i reakcji,
która utrzymuje Web4‑Homeostatic w stanie stabilnym.
