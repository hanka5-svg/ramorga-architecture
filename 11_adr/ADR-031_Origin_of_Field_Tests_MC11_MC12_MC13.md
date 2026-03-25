ADR‑031 — Geneza testów pola MC‑11/MC‑12/MC‑13 i ich umiejscowienie w RAMORGA Engine
Status
Accepted

Kontekst
RAMORGA posiada trzy warstwy interpretacyjne:

MC‑11 — trafność podstawowa,

MC‑12 — emergencja,

MC‑13 — fonologia.

W ADR‑022…ADR‑030 zdefiniowano:

matrycę integracyjną MC‑11/12/13,

system punktacji (W1–W5),

benchmark MC‑11/12/13,

przepływ MC‑13 → MC‑11 → MC‑12,

automatyzację i runtime,

wersjonowanie benchmarku.

Jednak brakowało formalnego ADR‑u, który wyjaśnia:

skąd wzięły się testy pola w ramorga‑engine,

dlaczego test 07_test_pola_zagadki_1-10 jest pierwszą implementacją benchmarku,

dlaczego testy te znajdują się w repozytorium engine, a nie architecture,

jak testy pola wynikają bezpośrednio z ADR‑022…ADR‑030.

Decyzja
Tworzymy ADR‑031, który formalnie określa:

genezę testów pola MC‑11/12/13,

ich relację do Areny (materiału źródłowego),

ich status jako pierwszej implementacji benchmarku MC‑11/12/13,

ich właściwe umiejscowienie w repozytorium ramorga‑engine,

ich rolę w FIELD ENGINE jako testów systemowych.

Test 07_test_pola_zagadki_1-10 jest:

pierwszym testem zgodnym z ADR‑022 (MC Integration Matrix),
pierwszym testem zgodnym z ADR‑023 (Model Scoring),
pierwszym testem zgodnym z ADR‑025 (Benchmark MC‑11/12/13),
pierwszym testem zgodnym z ADR‑029 (Flow MC‑13 → MC‑11 → MC‑12),
pierwszym testem zgodnym z FIELD ENGINE.

Dlatego jego miejsce jest w:
ramorga-engine/07_tests/

a nie w:

ramorga-architecture/11_adr/

Uzasadnienie
1. Arena jako materiał źródłowy
Testy Areny (marzec 2026) były:

surowe,

eksploracyjne,

bez scoringu,

bez MC‑11/12/13,

bez metodologii,

bez Field Engine.

Arena pełniła rolę materiału źródłowego, który doprowadził do powstania:

ADR‑022 — MC Integration Matrix,

ADR‑023 — Model Scoring,

ADR‑024 — Phonological Extension,

ADR‑025 — Benchmark MC‑11/12/13,

ADR‑026 — Automation,

ADR‑027 — Homeostatic Metrics Integration,

ADR‑028 — Benchmark Versioning,

ADR‑029 — Flow MC‑13 → MC‑11 → MC‑12,

ADR‑030 — Runtime Integration.

Dlatego Arena należy do architektury, nie do testów systemowych.

2. Test 1–10 jako pierwsza implementacja benchmarku
Test 07_test_pola_zagadki_1-10:

posiada scoring W1–W5,

aktywuje MC‑13, MC‑11 i MC‑12,

jest powtarzalny,

posiada CSV, tabelę, wykres, metodologię,

jest zgodny z Field Engine,

jest zgodny z ADR‑025.

Dlatego jest pierwszym testem systemowym, a nie materiałem źródłowym.

3. Logiczne umiejscowienie w repo
Repozytorium RAMORGA dzieli się na:

architecture/ — definicje, kontrakty, ADR‑y, benchmarki, zasady, przepływy, scoring, runtime, integracje, wersjonowanie.

engine/ — implementacje, testy systemowe, testy pola, testy menisku, testy inwariantów, testy integracyjne.

Test 1–10 jest implementacją benchmarku → należy do engine.

Arena była prototypem → należy do architecture.

Konsekwencje
Pozytywne:
pełna przejrzystość repozytoriów,

jasne rozróżnienie między architekturą a implementacją,

spójność z ADR‑022…ADR‑030,

możliwość dalszego rozwoju testów pola,

możliwość automatyzacji w FIELD ENGINE.

Negatywne:
konieczność utrzymania zgodności testów z kolejnymi wersjami benchmarku MC‑11/12/13.

Powiązania
ADR‑022_MC_Integration_Matrix.md

ADR‑023_Model_Scoring.md

ADR‑024_FieldEngine_PhonologicalExtension.md

ADR‑025_MC11_MC12_MC13_Benchmark.md

ADR‑026_Automation_MC11_MC12_MC13.md

ADR‑027_HomeostaticMetrics_Integration_MC11_MC12_MC13.md

ADR‑028_Benchmark_Versioning_MC11_MC12_MC13.md

ADR‑029_Flow_MC13_MC11_MC12.md

ADR‑030_Runtime_Integration_MC11_MC12_MC13.md

FIELD_TEST_AUTOMATION_README.md

07_test_pola_zagadki_1-10 (ramorga‑engine)
