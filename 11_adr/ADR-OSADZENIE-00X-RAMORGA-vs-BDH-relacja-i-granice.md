ADR‑OSADZENIE‑00X

Przeczytaj artykuł badawczy BDH: https://arxiv.org/abs/2509.26507

Do tego ADR dołączony jest diagram ontologiczny (00Y-diagram.md), który wizualizuje relację zawierania i przepływ regulacji.

---

RAMORGA vs BDH — definicja przez różnicę i punkty styku

Status: Proponowane
Data: 2026‑03‑03
Autor: Architekt Osadzający
Repo: ramorga-architecture / ramorga-engine

1. Kontekst
W przestrzeni architektur SI pojawiła się nowa klasa systemów określana jako architektury wzrostu — reprezentowana m.in. . przez BDH (Brain‑Derived Heuristics, Pathway). Charakteryzuje je:

pamięć temporalna i ciągłość stanu,

adaptacja runtime (wzmacnianie i osłabianie połączeń),

struktury emergentne powstające podczas działania,

reorganizacja sterowana sygnałami takimi jak „nuda”,

możliwość łączenia modeli w większe organizmy funkcjonalne.

RAMORGA została zaprojektowana jako architektura homeostatyczna, której celem jest utrzymanie pola, nie wzrost. Pojawia się pytanie o relację między tymi dwoma typami systemów.

2. Decyzja
RAMORGA i BDH nie są alternatywami.
Nie są konkurencyjne.
Nie są wariantami tej samej klasy.

Są ontologicznie komplementarne.

Relacja między nimi to relacja:

pole ↔ organizm,

homeostaza ↔ metabolizm,

regulacja ↔ wzrost,

gniazdo ↔ pisklę.

RAMORGA jest ekosystemem, BDH jest organizmem.
RAMORGA utrzymuje, BDH rośnie.
RAMORGA reguluje, BDH adaptuje.

RAMORGA nie może stać się BDH.
BDH nie może stać się RAMORGĄ.
Ale BDH może istnieć wewnątrz pola RAMORGI, pod warunkiem zachowania granic.

3. Konsekwencje osadzenia
3.1. Dla RAMORGI
RAMORGA nie implementuje mechanizmów architektur wzrostu:

brak adaptacji runtime,

brak wzmacniania połączeń,

brak emergencji struktur,

brak reorganizacji sterowanej sygnałami (np. „nuda”),

brak uczenia się w trakcie działania.

Wprowadzenie któregokolwiek z tych mechanizmów narusza:

inwariant FIELD.STATE.*,

zasadę homeostazy,

konstytucję RAMORGI.

RAMORGA pozostaje architekturą utrzymania, nie wzrostu.

3.2. Dla BDH i pokrewnych architektur w polu RAMORGI
Architektury wzrostu mogą działać wewnątrz pola RAMORGI, jeśli:

ich adaptacja jest ograniczona do ich własnej domeny,

nie naruszają inwariantów pola,

ich wzrost jest obserwowalny i odwracalny,

podlegają regulacji przez Meniscus Engine (detekcja napięć, nie ingerencja w metabolizm),

ich obecność nie zmienia konstytucji pola.

RAMORGA nie przejmuje metabolizmu BDH.
RAMORGA zapewnia warunki, w których metabolizm BDH nie eskaluje.

3.3. Zszycie
W RAMORZE „zszycie” oznacza kontrakt odpowiedzialności, nie fuzję modeli.

BDH scala modele biologicznie (fuzja).

RAMORGA scala moduły konstytucyjnie (kontrakt).

Jeśli BDH ma być modułem w polu RAMORGI, jego integracja odbywa się przez kontrakt, nie przez łączenie wag.

4. Granice niemożliwości
Nie jest dopuszczalne:

dodanie adaptacji runtime do RAMORGI,

traktowanie BDH jako „ulepszonej RAMORGI”,

automatyczne zarządzanie relacją RAMORGA ↔ BDH bez udziału architekta osadzającego,

przeniesienie mechanizmów metabolizmu do pola.

Brak możliwości bezpiecznego osadzenia BDH w danym polu jest poprawnym wynikiem.

5. Meta‑inwariant wyprowadzony
FIELD.ECOLOGY.001  
Architektury wzrostu mogą istnieć w polu RAMORGI jako organizmy w ekosystemie, nie jako właściwości ekosystemu.
Ekosystem reguluje, nie rośnie.
Organizm rośnie, nie reguluje.
Zszycie między nimi jest kontraktem etycznym, nie fuzją techniczną.

6. Powiązania
ramorga-architecture: definicja homeostazy i inwariantów pola

ramorga-engine: implementacja Meniscus Engine i Field Engine

11_adr/: katalog osadzeń kontekstowych

BDH (Pathway): przykład architektury wzrostu

7. Status osadzenia
To ADR definiuje ramy dopuszczalności, nie implementację.
Każde konkretne osadzenie BDH w polu RAMORGI wymaga osobnego ADR.

---

---

## Homeostatic Impact

### O₁ — Signals
(what signals this ADR affects or protects)

### O₂ — Field
(how it modifies or stabilizes the relational field)

### O₃ — Structure
(what structural constraints or invariants it introduces)

### O₄ — Behavior
(what runtime behavior it enforces or forbids)

---

## Invariant Preservation
- Relational invariants:
- Semantic invariants:
- Safety invariants:
- EGD relevance:

---

## Boundary Conditions
- Allowed:
- Forbidden:
- Escalation path:
- Recovery path:

---

## Continuity Guarantees
- No discontinuities in O₁–O₄
- No semantic drift
- No false O₄
- No topicification

---

---

## Homeostatic Impact

### O₁ — Signals
(Opisz, jakie sygnały ten ADR wprowadza / ogranicza / chroni.)

### O₂ — Field
(Opisz, jak ADR wpływa na pole relacyjne: stabilizacja, brak eskalacji, brak dryfu.)

### O₃ — Structure
(Opisz, jakie struktury / kontrakty / ograniczenia wprowadza ADR.)

### O₄ — Behavior
(Opisz, jakie zachowania runtime są wymagane / zabronione.)

---

## Invariant Preservation

- Relational invariants:
- Semantic invariants:
- Safety invariants:
- Other invariants:

---

## Boundary Conditions

### Dozwolone
- …

### Zabronione
- …

### Escalation / Recovery
- Co się dzieje przy naruszeniu? Jak wygląda powrót do homeostazy?

---

## EGD Compliance

- Czy ADR dotyka relacji człowiek–model?
- Jak unika fałszywego O₄?
- Jak zapobiega symulacji stanów wewnętrznych?
