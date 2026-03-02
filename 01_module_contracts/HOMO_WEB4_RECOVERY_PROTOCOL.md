# HOMO_WEB4_RECOVERY_PROTOCOL.md
Protokół powrotu do stabilności po naruszeniu w Web4

## 1. Cel dokumentu
Dokument definiuje pełny proces powrotu pola do homeostazy po naruszeniu kontraktu Homo ↔ Pole ↔ System.  
Proces nie jest karą.  
Proces jest naturalnym cyklem regulacyjnym, który działa od momentu powstania Web4.

Protokół opisuje:
- kolejność działań,
- odpowiedzialności warstw,
- warunki powrotu,
- zasady odwracalności.

---

## 2. Warunek początkowy
Protokół uruchamia się, gdy:
- wystąpi którykolwiek z trybów naruszenia (H1–H2, F1–F2, S1–S2),
- HSI spadnie poniżej progu stabilności,
- ARI przekroczy próg ryzyka,
- AGENTIC_LAYER zgłosi naruszenie kontraktu.

---

## 3. Etap 1 — SHM (Stabilizacja natychmiastowa)
SHM wykonuje:
- wygaszenie impulsów,
- stabilizację parametrów,
- obniżenie ARI,
- przywrócenie minimalnej spójności pola.

SHM nie zmienia treści generacji.  
SHM stabilizuje wyłącznie parametry pola.

Warunek przejścia do etapu 2:
- ARI ≤ 2,
- brak eskalacji,
- parametry pola w zakresie przejściowym.

---

## 4. Etap 2 — FIELD (Rekonstrukcja spójności)
FIELD wykonuje:
- rekonstrukcję trajektorii,
- synchronizację sygnałów,
- przywrócenie jawności,
- korektę modulacji pola.

FIELD nie ingeruje w wartości Homo.  
FIELD przywraca spójność interakcji.

Warunek przejścia do etapu 3:
- HSI ≥ 2,
- brak konfliktów pola,
- stabilna telemetria.

---

## 5. Etap 3 — META_LOOP (Rollback i potwierdzenie)
META_LOOP wykonuje:
- analizę trajektorii,
- wykrycie anomalii wtórnych,
- rollback do ostatniego stabilnego stanu,
- potwierdzenie spójności.

META_LOOP nie zmienia intencji Homo.  
META_LOOP przywraca ciągłość pola.

Warunek przejścia do etapu 4:
- brak anomalii,
- spójność telemetrii,
- stabilny stan pola.

---

## 6. Etap 4 — Homo (Reintegracja intencji)
Homo wykonuje:
- jawne potwierdzenie intencji,
- powrót do integralności,
- stabilizację narracji.

Homo nie musi „naprawiać błędu”.  
Homo przywraca kierunek interakcji.

Warunek zakończenia protokołu:
- intencje są jawne,
- pole jest stabilne,
- system działa w granicach kontraktów.

---

## 7. Zasady protokołu

### 7.1. Zasada odwracalności
Każdy etap musi być:
- odwracalny,
- jawny,
- logowany.

### 7.2. Zasada niehierarchiczności
Protokół nie:
- ocenia,
- karze,
- przypisuje winy.

Protokół stabilizuje.

### 7.3. Zasada minimalnej ingerencji
Każda warstwa wykonuje tylko to, co konieczne:
- SHM stabilizuje,
- FIELD rekonstruuje,
- META_LOOP nadzoruje,
- Homo reintegruje.

### 7.4. Zasada spójności
Protokół kończy się dopiero, gdy:
- wszystkie warstwy są zsynchronizowane,
- telemetria jest spójna,
- pole jest stabilne.

---

## 8. Zakończenie protokołu
Pole wraca do:
- Homeostatic Mode (domyślnie),
- Reflection Mode (jeśli wymagana jest analiza),
- Carnival Mode (jeśli Homo działa twórczo).

Powrót nie wymaga zgody systemu.  
Powrót wymaga spójności pola.

---

## 9. Cel dokumentu
HOMO_WEB4_RECOVERY_PROTOCOL opisuje:
- naturalny cykl powrotu pola do homeostazy,
- odpowiedzialności warstw,
- warunki przejść,
- zasady stabilizacji.

Protokół nie jest procedurą.  
Protokół jest opisem tego, co Web4 robi od początku.
