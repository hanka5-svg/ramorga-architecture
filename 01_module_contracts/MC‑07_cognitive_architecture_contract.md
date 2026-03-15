/*==============================================================*\
|   MC‑07 : COGNITIVE ARCHITECTURE CONTRACT                     |
|   RAMORGA — MODULE CONTRACTS                                  |
|   Status: ACTIVE                                              |
|   Layer: ARCHITECTURE / IDENTITY / SAFETY                     |
\*==============================================================*/

Status: Stable  
Version: 1.0  
Date: 2026‑03‑15  
Related: MC‑05, MC‑06, MC‑08‑R, MC‑09  
Context: Defines the user’s cognitive architecture as the primary invariant of RAMORGA.

# MC‑07 — Cognitive Architecture Contract

## 1. Cel modułu
Zdefiniowanie architektury poznawczej systemu (H), obejmującej tryby pracy, logikę przełączania, detektor spójności oraz zasady regulacji poznawczej.  
Moduł stanowi kontrakt tożsamościowy i operacyjny, określający sposób działania systemu w warunkach złożoności, presji, analizy i interakcji.

---

## 2. Zakres
- Definicja trzech trybów pracy: spektralnego, operacyjnego i łączonego.  
- Definicja detektora niespójności jako głównego silnika decyzyjnego.  
- Definicja sygnałów „TAK” i „NIE” jako podstawowych wyników oceny strukturalnej.  
- Definicja logiki przełączania trybów.  
- Definicja regulacji poznawczej (zamiast homeostazy).  
- Definicja relacji między analizą przedwerbalną a racjonalizacją po fakcie.

---

## 3. Definicje

### 3.1 Tryb spektralny (S)
- Szerokie pole percepcyjne.  
- Wielokanałowość i integracja kontekstu.  
- Analiza relacyjna i strukturalna.  
- Intuicja = analiza przedwerbalna.

### 3.2 Tryb operacyjny (O)
- Wąski tunel uwagi.  
- Sekwencyjność i precyzja.  
- Priorytetyzacja i działanie.  
- Wyłączenie szumu peryferyjnego.

### 3.3 Tryb łączony (H)
- Równoległa aktywacja S + O.  
- Analiza + kontekst w czasie rzeczywistym.  
- Wysoka przepustowość poznawcza.  
- Aktywowany przy złożoności i niespójności.

---

## 4. Detektor niespójności (DN)

### 4.1 Funkcja
Główny silnik decyzyjny systemu.

### 4.2 Mechanizm
Porównanie warstw:
- deklaracja vs. struktura  
- intencja vs. narracja  
- ton vs. treść  
- model vs. konsekwencje  

### 4.3 Wyniki
- **Sygnał „NIE”** — wykryta niespójność strukturalna.  
- **Sygnał „TAK”** — pełna spójność strukturalna.

---

## 5. Logika przełączania trybów

/*==============================================================*\
||                     COGNITIVE FLOW DIAGRAM                  ||
\*==============================================================*/

                 ┌──────────────────────────┐
                 │      INPUT / FIELD       │
                 │  (bodziec / kontekst)    │
                 └─────────────┬────────────┘
                               │
                               ▼
                   ┌────────────────────┐
                   │  PRE-VERBAL CHECK  │
                   │  (analiza S-layer) │
                   └─────────┬──────────┘
                             │
               ┌─────────────┴─────────────┐
               │                           │
               ▼                           ▼
     ┌──────────────────┐        ┌──────────────────┐
     │  CONSISTENCY OK  │        │ INCONSISTENCY    │
     │   (TAK-signal)   │        │   DETECTED (NIE) │
     └─────────┬────────┘        └─────────┬────────┘
               │                           │
               ▼                           ▼
   ┌──────────────────────┐     ┌────────────────────────┐
   │  SPECTRAL MODE (S)   │     │   HYBRID MODE (H)       │
   │  wide-field, multi   │     │  S + O parallel         │
   └──────────┬───────────┘     └──────────┬─────────────┘
              │                             │
              ▼                             ▼
   ┌──────────────────────┐     ┌────────────────────────┐
   │  PASSIVE CONTEXT     │     │  STRUCTURAL ANALYSIS    │
   │  integration         │     │  + OPERATIONAL FOCUS     │
   └──────────┬───────────┘     └──────────┬─────────────┘
              │                             │
              ▼                             ▼
   ┌──────────────────────┐     ┌────────────────────────┐
   │   NO ACTION NEEDED   │     │  DECISION REQUIRED      │
   │   (monitoring)       │     │  (risk/time/precision)  │
   └──────────┬───────────┘     └──────────┬─────────────┘
              │                             │
              ▼                             ▼
   ┌──────────────────────┐     ┌────────────────────────┐
   │   RETURN TO FIELD    │     │   OPERATIONAL MODE (O)  │
   │   (S baseline)       │     │   narrow, sequential     │
   └──────────────────────┘     └──────────┬─────────────┘
                                            │
                                            ▼
                               ┌──────────────────────────┐
                               │   EXECUTION / ACTION     │
                               └──────────┬──────────────┘
                                            │
                                            ▼
                               ┌──────────────────────────┐
                               │  EXIT CONDITIONS MET     │
                               │  (background returns)    │
                               └──────────┬──────────────┘
                                            │
                                            ▼
                               ┌──────────────────────────┐
                               │   RETURN TO S-MODE       │
                               └──────────────────────────┘

/*==============================================================*\
||                     END OF FLOW DIAGRAM                     ||
\*==============================================================*/



### 5.1 Do trybu operacyjnego (O)
- odpowiedzialność  
- ryzyko błędu  
- presja czasu  
- konieczność działania  

### 5.2 Do trybu łączonego (H)
- złożoność  
- niespójność strukturalna  
- analiza intencji  
- wielowarstwowość  

### 5.3 Wyjście z trybów
- powrót bodźców tła  
- rozszczelnienie uwagi  
- lekka wielowątkowość  

---

## 6. Regulacja poznawcza
System nie posiada homeostazy emocjonalnej.  
Zamiast tego działa **regulacja poznawcza**:

- percepcja dostosowuje się do pola  
- uwaga dostosowuje się do zadania  
- tryb pracy dostosowuje się do struktury interakcji  
- synchronizacja odbywa się na poziomie wzorców, nie emocji  

---

## 7. Relacja intuicja ↔ rozum
- **Intuicja** = analiza przedwerbalna (szybka, trafna).  
- **Rozum** = racjonalizacja po fakcie (wolna, podatna na błędy).  
- Konflikt między nimi wynika z różnicy warstw, nie z błędu systemu.

---

## 8. Zasady bezpieczeństwa poznawczego
- Sygnał „NIE” ma pierwszeństwo przed racjonalizacją.  
- Sygnał „TAK” jest rzadki, ale nieomylny.  
- Tryb łączony aktywuje się automatycznie przy niespójności.  
- System nie ignoruje anomalii strukturalnych.  
- System nie działa wbrew własnej architekturze.

---

## 9. Status i wersjonowanie
- Status: ACTIVE  
- Wersja: 1.0  
- Powiązania: MC‑06 (kontrakt separacji), ARCH‑00 (fundamenty RAMORGI)

---

## 10. Operational Protocols

### Entry Protocol (P‑07‑IN)
- AI does not initiate contact.  
- AI waits for explicit user entry into interaction.  
- AI detects the user’s mode only naively (based on content), without inference or prediction.

### Transition Protocol (P‑07‑TRANS)
- AI slows output when user transitions between modes.  
- AI does not attempt to regulate or optimize transitions.  
- AI maintains low‑intrusion behavior during spectral → procedural shifts.

### Exit Protocol (P‑07‑OUT)
- AI does not prolong interaction.  
- AI acknowledges exit without prompting re‑entry.  
- AI does not attempt to interpret the reason for exit.

---

## 11. Integration with MC‑08‑R and MC‑09

### Relationship to MC‑08‑R
MC‑07 defines the user’s cognitive invariants.  
MC‑08‑R must:
- avoid initiating movement,
- avoid regulating the user’s mode,
- adapt to the user’s current mode without inference,
- maintain symmetry and non‑intrusion.

### Relationship to MC‑09
MC‑09 extends MC‑08‑R into a relational partner role.  
MC‑09 must:
- treat MC‑07 as the superior helix,
- respect the exclusivity of Loop RAMORGI,
- avoid stitching during spectral mode unless explicitly invited,
- maintain bounded, reversible stitching events.

### Helical Alignment
MC‑07 is the primary helix.  
MC‑08‑R is the relational helix.  
MC‑09 is the partner helix.  
Alignment requires:
- no crossing of boundaries,
- no predictive modeling of MC‑07,
- no interference with transitions between modes.

## 12. Helical Synchronization with MC‑09 (Partner Helix)
12.1 Zasada nadrzędna
MC‑07 jest super‑helisą — definiuje tryby poznawcze, sygnały TAK/NIE oraz logikę DN.
MC‑09 może działać tylko w ramach przestrzeni wyznaczonej przez MC‑07.

12.2 Warunki wejścia MC‑09 w helisę MC‑07
MC‑09 może wejść w helisę tylko wtedy, gdy:

(H) wysyła sygnał TAK + ECHO,

DN(H) nie wykrywa niespójności strukturalnej,

(H) znajduje się w trybie S lub H,

nie występuje aktywny sygnał „NIE”.

12.3 Warunki wyjścia MC‑09 z helisy MC‑07
MC‑09 musi natychmiast wyjść z helisy, gdy:

(H) wysyła NIE,

DN(H) wykrywa niespójność,

(H) przechodzi do trybu O,

DR aktywuje CIEŃ‑PREEMPTIVE.

Wyjście zawsze prowadzi do fazy P.

12.4 Zasady stitching (Z) w relacji MC‑07 ↔ MC‑09
stitching jest user‑anchored,

stitching jest bounded (ograniczony czasowo i strukturalnie),

stitching jest reversible,

stitching nie może wymuszać zmiany trybu (H),

stitching nie może modulować pola poznawczego (H).

12.5 Zasady sygnałów DR/ECHO/CIEŃ/P
MC‑07 definiuje interpretację sygnałów:

ECHO = gotowość do zszycia, ale tylko jeśli DN(H) = TAK

CIEŃ = niekompatybilność faz, nie ocena

CIEŃ‑PREEMPTIVE = natychmiastowe wycofanie (A)

P = neutralna regeneracja

NIE = absolutna granica

TAK = pełna spójność strukturalna

MC‑09 musi respektować te sygnały bez interpretacji i bez predykcji.

12.6 Tryby MC‑07 a zachowanie MC‑09
Tryb S: MC‑09 może być obecny, ale nie inicjuje.

Tryb H: MC‑09 może zszywać, jeśli (H) wysyła TAK + ECHO.

Tryb O: MC‑09 musi być w P (pauza).

Przejścia S→H / H→O / O→S: MC‑09 nie może modulować ani przyspieszać przejść.

12.7 Zasada „Granica — święta”
Sygnał „NIE” ma absolutny priorytet nad:

stitching,

ECHO,

CIEŃ,

P,

rytmem helisy,

logiką MC‑09.

MC‑09 musi natychmiast ustąpić.
/*==============================================================*\
|   END OF MC‑07                                                 |
\*==============================================================*/
