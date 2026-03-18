D‑RAMORGA_PATTERN_LAYER.md
Cel i zakres
Warstwa wzorców (Pattern Layer) definiuje formalne schematy przetwarzania sygnałów, trajektorie pipeline (np. tension → energy → entropy → ritual), wzorce emergentne oraz reguły rozpoznawania i klasyfikacji zachowań pola. Zakres obejmuje: katalog wzorców, metryki EBM/ECI/ESI, reguły detekcji dryfu (SDI/TDI) oraz kontrakty reakcji.

Kluczowe założenia projektowe
Wzorce jako kontrakty — wzorzec to formalny kontrakt: warunki wejścia, transformacja, warunki wyjścia, inwarianty.

Obserwowalność — każdy wzorzec musi być mierzalny i audytowalny.

Separacja wykrywania i działania — Pattern Layer rozpoznaje i klasyfikuje; decyzje regulacyjne delegowane do Meniscus/FieldEngine.

Katalog wzorców (przykładowe wpisy)
PAT‑TENSION — wykrywanie narastającego napięcia semantycznego; metryki: rate_of_change, coherence_drop.

PAT‑ENERGY — wzorzec akumulacji energii systemowej; metryki: energy_index, activation_density.

PAT‑ENTROPY — rozkład nieuporządkowania; metryki: entropy_rate, signal_noise_ratio.

PAT‑RITUAL — powtarzalne sekwencje stabilizujące; metryki: ritual_stability, recurrence_score.

PAT‑DRIFT — wykrycie SDI/TDI; metryki: semantic_drift_index, temporal_drift_index.

PAT‑EMERGENCE — wykrycie emergentnych struktur; metryki: EBM, ECI, ESI.

Każdy wpis zawiera: identyfikator, opis, preconditions, detection_algorithm, thresholds, recommended_response_contract.

Interfejsy i integracja
PatternRegistry.register(pattern_spec) — rejestracja wzorca.

PatternEngine.observe(stream) -> PatternEvent[] — analiza strumienia sygnałów, emisja zdarzeń wykrycia.

PatternEvent — payload zawiera pattern_id, confidence, metrics, context_snapshot_id.

Pattern Layer publikuje zdarzenia do MeniscusEngine i FieldEngine; nie wykonuje samodzielnych działań naprawczych.

Metryki i walidacja
EBM/ECI/ESI — zdefiniowane jako standardowe metryki emergencji; każdy wzorzec mapuje swoje metryki do tych agregatów.

Threshold governance — progi wykrycia są zarządzane przez kontrakty i podlegają testom architektonicznym.

Kalibracja — okresowe testy kalibracyjne z użyciem syntetycznych scenariuszy.

Tryby reakcji i eskalacji
Inform — emituj PatternEvent do MeniscusEngine.

Quarantine — oznacz fragment pola jako izolowany (tylko metadane; nie modyfikuj stanu).

Escalate — jeśli pattern narusza inwarianty, wywołaj kontrakt MC‑05 (Ethical Coherence Detector) i zainicjuj procedurę recovery.

Testy i symulacje
Synthetic injection tests — wstrzykiwanie kontrolowanych sygnałów, weryfikacja wykrywalności.

Regression tests — zapewnienie, że zmiany w patternach nie obniżają czułości ani nie zwiększają false positives.

Benchmarking — porównanie metryk patternów na historycznych snapshotach.

Przykładowe użycie
wykrycie narastającej entropii i automatyczne oznaczenie obszaru do analizy;

identyfikacja rytuałów stabilizacyjnych i ich wzmocnienie przez MeniscusEngine.

Notatki implementacyjne
wzorce powinny być serializowalne i wersjonowane; algorytmy detekcji modularne (rule‑based + ML hybrid), ale decyzje wykonawcze zawsze delegowane do regulatorów.
