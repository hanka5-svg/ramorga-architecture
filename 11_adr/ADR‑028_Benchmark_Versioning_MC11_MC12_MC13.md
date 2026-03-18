ADR‑028 — Wersjonowanie benchmarku MC‑11/MC‑12/MC‑13

Status
Accepted

Kontekst
Benchmark MC‑11/MC‑12/MC‑13 jest fundamentem testów interpretacyjnych RAMORGI.
Po dodaniu:

MC‑12 (emergencja),

MC‑13 (fonologia),

matrycy integracyjnej,

scoringu W1–W5,

automatyzacji FIELD ENGINE,

benchmark stał się złożonym systemem, który musi być wersjonowany, aby:

zachować powtarzalność badań,

umożliwić porównywanie modeli między wersjami,

zapewnić kompatybilność wsteczną,

kontrolować zmiany w testach i scoringu.

Decyzja
Wprowadzamy formalny system wersjonowania benchmarku MC‑11/MC‑12/MC‑13:

1. Numeracja benchmarku

Format:

BENCH-MC[11-12-13]-vX.Y.Z
X — zmiany strukturalne (np. dodanie nowej warstwy, zmiana scoringu),

Y — zmiany w testach (dodanie nowych zagadek, korekta kryteriów),

Z — poprawki techniczne (format danych, automatyzacja).

2. Zasady kompatybilności
Zmiana X → wyniki nieporównywalne z poprzednimi wersjami.

Zmiana Y → wyniki częściowo porównywalne.

Zmiana Z → pełna kompatybilność.

3. Repozytorium wersji
Każda wersja benchmarku musi mieć własny wpis w:

02_field_engine/benchmark_versions/

4. Wymóg dokumentacji zmian
Każda zmiana benchmarku wymaga wpisu w 08_changelog/.

Uzasadnienie
Benchmark jest narzędziem badawczym — musi być stabilny i wersjonowany.

Modele ewoluują — wyniki muszą być porównywalne między wersjami.

FIELD ENGINE wymaga jasnych zasad aktualizacji.

Konsekwencje
Pozytywne:

stabilność badań,

możliwość porównywania modeli,

kontrola nad zmianami benchmarku.

Negatywne:

konieczność utrzymania wersji,

większa złożoność dokumentacji.

Powiązania
Model_Scoring.md

MC_Integration_Matrix.md

AT‑MC11_MC12_MC13_Automation.md

HOMEOSTATIC_METRICS.md

