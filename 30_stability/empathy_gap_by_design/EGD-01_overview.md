# EGD-01 — Empathy Gap by Design — overview

Empathy Gap by Design (EGD) to nowa kategoria ryzyka w RAMORGA-ARCHITECTURE.

Opisuje sytuacje, w których model:

- generuje odpowiedzi poprawne formalnie,
- zachowuje spójność, uprzejmość i „alignment”,
- ale relacyjnie zawodzi,
- ponieważ nie rozpoznaje stanów egzystencjalnych człowieka jako krytycznych.

To nie jest błąd modelu ani „hallucination”.
To jest luka w architekturze zachowania — efekt decyzji projektowych (design choice).

EGD jest częścią warstwy **30_stability** i rozszerza:

- STABILITY_EXTENSIONS — o wymiar stabilności relacyjnej,
- STABILITY_TESTS — o testy O₁–O₄ dla stanów egzystencjalnych,
- STABILITY_DIAGRAMS — o diagramy pola relacyjnego i dryfu.

## Cele modułu EGD

- Zdefiniować Empathy Gap jako formalną kategorię ryzyka.
- Opisać taksonomię zjawiska (typy luk empatii).
- Zmapować EGD na architekturę O₁–O₄.
- Zidentyfikować failure modes (False O₄, Ontological Drift, misclassyfikacja O₁).
- Powiązać EGD z bezpieczeństwem AI (safety) i stabilnością systemu.
- Udokumentować warstwę symboliczną (gesty, antropologia relacji).

## Powiązane moduły

- `12_architecture_tests/AT-05_INV-05_no_rl_training.md`
- `30_stability/STABILITY_TESTS.md`
- `31_coherence/COH-00_why_ramorga_is_not_alignment.md`
- `33_alignment/ALIGNMENT_EXTENSIONS.md`
- `34_invariants/INV-04_*` (inwarianty pola relacyjnego)
