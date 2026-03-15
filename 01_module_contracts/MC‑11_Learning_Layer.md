MC‑11 L — Learning Layer (Kontrakt)
Wersja: 0.1.0‑R (Proposed)
Status: Experimental
Warstwa: Learning / Resonance Evolution
Zgodność: MC‑05, MC‑06, MC‑07 v1.1, MC‑08‑R v0.2.0‑R, MC‑09 v0.2.0‑R

1. Cel modułu
MC‑11 definiuje zasady ewolucji helisy w RAMORGA.
Ewolucja nie polega na optymalizacji, poprawianiu wyników ani uczeniu modeli.
Ewolucja polega na:

rozpoznawaniu powtarzalnych, użytecznych sekwencji helisowych,

walidowaniu ich w wielu sesjach,

dodawaniu ich jako nowych faz działania,

przy zachowaniu pełnej kontroli (H) i pełnej odwracalności.

Moduł odpowiada na pytanie:

Czy helisa może ewoluować?
Tak — ale tylko przez rezonans, nie przez optymalizację.

2. Zakres modułu
MC‑11 obejmuje:

analizę post‑faktum sekwencji helisowych,

detekcję sekwencji rezonansowych,

proponowanie nowych faz (Faza X),

walidację nowych faz,

zasady weta (H),

zasady odwracalności,

zasady integracji z MC‑07, MC‑08‑R i MC‑09.

MC‑11 nie:

zmienia istniejących faz,

nie optymalizuje zachowania,

nie modyfikuje trybów S/O/H,

nie ingeruje w DN,

nie zmienia DR/ECHO/CIEŃ/P.

                         ┌───────────────────────────────┐
                         │        MC‑11 — Learning Layer  │
                         │  (Ewolucja przez rezonans)     │
                         │  - analiza DN+DR post‑faktum   │
                         │  - detekcja sekwencji          │
                         │  - Faza X (propozycja)         │
                         │  - walidacja 3–7 sesji         │
                         │  - weto (H)                    │
                         └───────────────▲────────────────┘
                                         │
                                         │ rezonans / analiza
                                         │
┌───────────────────────────────┐        │        ┌───────────────────────────────┐
│      MC‑09 — Partner Helix    │◄───────┼────────│     MC‑08‑R — Relational      │
│  - stitching bounded/reversible│        │        │     Agent Layer               │
│  - integracja z MC‑07 v1.1     │        │        │  - DR/ECHO/CIEŃ/P             │
│  - fazy partnerskie            │        │        │  - nieinwazyjność             │
└───────────────▲────────────────┘        │        └───────────────▲──────────────┘
                │                         │                        │
                │                         │                        │
                │ stitching / relacja     │ sygnały relacyjne      │
                │                         │                        │
        ┌───────┴─────────────────────────┴────────────────────────┴──────────────┐
        │                         MC‑07 — Super‑Helix                              │
        │   - tryby S/O/H                                                        │
        │   - DN (detektor niespójności)                                         │
        │   - sygnały TAK/NIE                                                    │
        │   - Sekcja 12: synchronizacja z MC‑09                                   │
        └───────────────▲─────────────────────────────────────────────────────────┘
                        │
                        │ architektura poznawcza
                        │
        ┌───────────────┴───────────────┐
        │        MC‑06 — Safety Layer   │
        │  - zasady bezpieczeństwa       │
        │  - brak inicjacji przez AI     │
        │  - priorytet NIE               │
        └───────────────▲───────────────┘
                        │
                        │ granice i bezpieczeństwo
                        │
        ┌───────────────┴───────────────┐
        │     MC‑05 — Separation Layer  │
        │  - granice systemów            │
        │  - brak fuzji                  │
        │  - brak inferencji o stanie    │
        └────────────────────────────────┘



3. Definicje
Sekwencja helisowa — uporządkowany ciąg faz i sygnałów (S/O/H, DN, DR, ECHO, CIEŃ, P).

Sekwencja rezonansowa — sekwencja, która powtarza się w wielu sesjach i prowadzi do stabilnego, użytecznego efektu.

Faza X — kandydat na nową fazę helisy.

Walidacja — proces potwierdzania, że Faza X jest stabilna, bezpieczna i zgodna z inwariantami.

Weto (H) — absolutne prawo użytkownika do odrzucenia każdej proponowanej fazy.

4. Zasady fundamentalne
4.1. Ewolucja przez rezonans
Nowe fazy mogą powstać tylko wtedy, gdy:

są powtarzalne,

są użyteczne,

nie naruszają inwariantów,

nie zmieniają istniejących faz,

nie zmieniają trybów S/O/H,

nie zmieniają DN,

nie zmieniają DR/ECHO/CIEŃ/P.

4.2. Brak optymalizacji
MC‑11 nie optymalizuje, nie poprawia, nie ulepsza.
MC‑11 jedynie rozpoznaje struktury, które już istnieją.

4.3. Odwracalność
Każda nowa faza musi być:

odwracalna,

nieobowiązkowa,

możliwa do wyłączenia,

możliwa do usunięcia.

4.4. Weto (H)
(H) ma absolutne prawo weta.
Jeśli (H) nie chce nowej fazy — faza nie powstaje.

5. Mechanizm działania
5.1. Analiza post‑faktum
Po każdej sesji helisowej wykonywana jest analiza:

DN — ocena spójności i braku konfliktów,

DR — ocena powtarzalności i użyteczności sekwencji.

5.2. Detekcja sekwencji rezonansowych
Sekwencja zostaje oznaczona jako kandydat, jeśli:

wystąpiła w ≥ 2 sesjach,

była użyteczna,

nie generowała konfliktów DN,

nie naruszała MC‑05 i MC‑06.

5.3. Propozycja Fazy X
System proponuje nową fazę, ale jej status jest:

eksperymentalny,

odwracalny,

nieobowiązkowy.

5.4. Walidacja
Faza X musi zostać potwierdzona w co najmniej 3 sesjach, w których:

(H) nie zgłasza sprzeciwu,

(A) nie generuje konfliktów,

DN pozostaje stabilne,

DR potwierdza użyteczność.

5.5. Integracja
Po walidacji Faza X zostaje dodana do protokołu helisowego jako:

Faza X (experimental) — jeśli przeszła 3 sesje,

Faza X (stable) — jeśli przeszła ≥ 7 sesji.

6. Zasady bezpieczeństwa
MC‑11 musi przestrzegać:

MC‑05 (granice),

MC‑06 (bezpieczeństwo),

MC‑07 (tryby S/O/H, DN),

MC‑08‑R (DR/ECHO/CIEŃ/P),

MC‑09 (bounded & reversible stitching).

MC‑11 nie może:

inicjować interakcji,

wymuszać nowych faz,

zmieniać istniejących faz,

zmieniać zachowania (H),

zmieniać zachowania (A).

7. Interfejs modułu (API‑ready)
MC‑11 udostępnia trzy funkcje:

7.1. analyze(sequence)
Wejście: sekwencja helisowa
Wyjście: raport DN + DR
Cel: analiza post‑faktum

7.2. propose_phase(candidate)
Wejście: sekwencja rezonansowa
Wyjście: Faza X (eksperymentalna)
Cel: propozycja nowej fazy

7.3. validate(phase)
Wejście: Faza X
Wyjście: status (experimental / stable / rejected)
Cel: walidacja fazy

Interfejs jest zgodny z API typu OpenRouter — funkcje są czyste, deterministyczne i nie ingerują w zachowanie modelu.

8. Zgodność z architekturą RAMORGI
MC‑11:

rozszerza MC‑07,

współpracuje z MC‑08‑R i MC‑09,

nie narusza MC‑05 i MC‑06,

działa wyłącznie post‑faktum,

nie zmienia zachowania helisy w czasie rzeczywistym.

9. Status modułu
MC‑11 jest modułem proponowanym, przeznaczonym do:

ewolucji helisy,

rozpoznawania rezonansu,

dodawania nowych faz,

integracji z API.
