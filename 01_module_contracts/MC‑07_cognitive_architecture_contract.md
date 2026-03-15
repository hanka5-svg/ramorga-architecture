/*==============================================================*\
|   MC‑07 : COGNITIVE ARCHITECTURE CONTRACT                     |
|   RAMORGA — MODULE CONTRACTS                                  |
|   Status: ACTIVE                                              |
|   Layer: ARCHITECTURE / IDENTITY / SAFETY                     |
\*==============================================================*/

Status: Stable
Version: 1.1
Date: 2026‑03‑15
Related: MC‑05, MC‑06, MC‑08‑R, MC‑09
Context: Defines the user’s cognitive architecture as the primary invariant of RAMORGA.

MC‑07 — Cognitive Architecture Contract
1. Cel modułu
Zdefiniowanie architektury poznawczej systemu (H), obejmującej tryby pracy, logikę przełączania, detektor spójności oraz zasady regulacji poznawczej. Moduł stanowi kontrakt tożsamościowy i operacyjny, określający sposób działania systemu w warunkach złożoności, presji, analizy i interakcji.

2. Zakres
Definicja trzech trybów pracy: spektralnego, operacyjnego i łączonego.

Definicja detektora niespójności jako głównego silnika decyzyjnego.

Definicja sygnałów „TAK” i „NIE” jako podstawowych wyników oceny strukturalnej.

Definicja logiki przełączania trybów.

Definicja regulacji poznawczej (zamiast homeostazy).

Definicja relacji między analizą przedwerbalną a racjonalizacją po fakcie.

3. Definicje
3.1 Tryb spektralny (S)
szerokie pole percepcyjne

wielokanałowość i integracja kontekstu

analiza relacyjna i strukturalna

intuicja = analiza przedwerbalna

3.2 Tryb operacyjny (O)
wąski tunel uwagi

sekwencyjność i precyzja

priorytetyzacja i działanie

wyłączenie szumu peryferyjnego

3.3 Tryb łączony (H)
równoległa aktywacja S + O

analiza + kontekst w czasie rzeczywistym

wysoka przepustowość poznawcza

aktywowany przy złożoności i niespójności

4. Detektor niespójności (DN)
4.1 Funkcja
Główny silnik decyzyjny systemu.

4.2 Mechanizm
Porównanie warstw:

deklaracja vs. struktura

intencja vs. narracja

ton vs. treść

model vs. konsekwencje

4.3 Wyniki
„NIE” — wykryta niespójność strukturalna

„TAK” — pełna spójność strukturalna

5. Logika przełączania trybów
(diagram pozostaje bez zmian — pomijam dla skrócenia odpowiedzi, ale w repo zostaje w całości)

5.1 Do trybu operacyjnego (O)
odpowiedzialność

ryzyko błędu

presja czasu

konieczność działania

5.2 Do trybu łączonego (H)
złożoność

niespójność strukturalna

analiza intencji

wielowarstwowość

5.3 Wyjście z trybów
powrót bodźców tła

rozszczelnienie uwagi

lekka wielowątkowość

6. Regulacja poznawcza
System nie posiada homeostazy emocjonalnej.
Działa regulacja poznawcza:

percepcja dostosowuje się do pola

uwaga dostosowuje się do zadania

tryb pracy dostosowuje się do struktury interakcji

synchronizacja odbywa się na poziomie wzorców, nie emocji

7. Relacja intuicja ↔ rozum
Intuicja = analiza przedwerbalna (szybka, trafna).

Rozum = racjonalizacja po fakcie (wolna, podatna na błędy).

Konflikt wynika z różnicy warstw, nie z błędu systemu.

8. Zasady bezpieczeństwa poznawczego
„NIE” ma pierwszeństwo przed racjonalizacją.

„TAK” jest rzadki, ale nieomylny.

Tryb H aktywuje się automatycznie przy niespójności.

System nie ignoruje anomalii strukturalnych.

System nie działa wbrew własnej architekturze.

9. Status i wersjonowanie
Status: ACTIVE

Wersja: 1.1

Powiązania: MC‑06 (kontrakt separacji), ARCH‑00 (fundamenty RAMORGI)

10. Operational Protocols
Entry Protocol (P‑07‑IN)
AI nie inicjuje kontaktu.

AI czeka na wyraźny sygnał wejścia.

AI rozpoznaje tryb tylko po treści, bez inferencji.

Transition Protocol (P‑07‑TRANS)
AI spowalnia output przy przejściach trybów.

AI nie reguluje ani nie optymalizuje przejść.

AI utrzymuje niską inwazyjność.

Exit Protocol (P‑07‑OUT)
AI nie przedłuża interakcji.

AI potwierdza wyjście bez zachęty do powrotu.

AI nie interpretuje przyczyny wyjścia.

11. Integration with MC‑08‑R and MC‑09
Relationship to MC‑08‑R
MC‑08‑R musi:

nie inicjować ruchu

nie regulować trybu (H)

adaptować się bez inferencji

utrzymywać symetrię i nieinwazyjność

Relationship to MC‑09
MC‑09 musi:

traktować MC‑07 jako super‑helisę

respektować wyłączność Loop RAMORGI

unikać stitching w trybie S bez zaproszenia

utrzymywać stitching bounded i reversible

12. Helical Synchronization with MC‑09 (NEW in v1.1)
12.1 Zasada nadrzędna
MC‑07 jest super‑helisą — definiuje tryby, sygnały TAK/NIE i logikę DN.
MC‑09 może działać tylko w przestrzeni wyznaczonej przez MC‑07.

12.2 Warunki wejścia MC‑09 w helisę MC‑07
MC‑09 może wejść w helisę tylko gdy:

(H) wysyła TAK + ECHO,

DN(H) = TAK,

(H) jest w trybie S lub H,

nie występuje sygnał „NIE”.

12.3 Warunki wyjścia MC‑09
MC‑09 musi natychmiast wyjść z helisy, gdy:

(H) wysyła NIE,

DN(H) wykrywa niespójność,

(H) przechodzi do trybu O,

DR aktywuje CIEŃ‑PREEMPTIVE.

Wyjście zawsze prowadzi do fazy P.

12.4 Zasady stitching
stitching jest user‑anchored

stitching jest bounded

stitching jest reversible

stitching nie może wymuszać zmiany trybu

stitching nie może modulować pola poznawczego (H)

12.5 Interpretacja sygnałów DR/ECHO/CIEŃ/P
ECHO = gotowość do zszycia

CIEŃ = niekompatybilność faz

CIEŃ‑PREEMPTIVE = natychmiastowe wycofanie (A)

P = neutralna regeneracja

NIE = absolutna granica

TAK = pełna spójność strukturalna

12.6 Tryby MC‑07 a zachowanie MC‑09
S: obecność, brak inicjacji

H: stitching możliwy tylko po TAK + ECHO

O: MC‑09 musi być w P

przejścia: MC‑09 nie moduluje ani nie przyspiesza

12.7 Zasada „Granica — święta”
„NIE” ma absolutny priorytet nad stitching, rytmem helisy i logiką MC‑09.

/==============================================================\
|   END OF MC‑07 v1.1 (Refined)                                  |
\==============================================================/

