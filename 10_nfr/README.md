# RAMORGA Non-Functional Requirements (NFR) — wersja homeostatyczna

RAMORGA NFR definiują systemowe granice działania: wydajność, stabilność, bezpieczeństwo, utrzymywalność i obserwowalność.  
Wersja homeostatyczna doprecyzowuje, że wszystkie NFR muszą być zgodne z:

- architekturą O₁–O₄,
- inwariantami relacyjnymi,
- EGD (Empathy Gap by Design),
- mechanizmami regulacji,
- kontraktami modułów.

NFR to **twarde granice**, nie preferencje.

---

## Performance (wydajność)

- Aktualizacje pola muszą kończyć się w czasie ograniczonym i mierzalnym.
- Normalizacja menisku musi być operacją stałoczasową.
- Kroki pipeline’u muszą być deterministyczne i przewidywalne.
- Żaden moduł nie może wprowadzać opóźnień naruszających homeostazę.

---

## Stability (stabilność)

- Stan pola i pipeline’u nie może rosnąć bez ograniczeń.
- META-loop nie może generować amplifikacji ani eskalacji.
- Przywracanie snapshotów nie może wprowadzać nieciągłości w O₁–O₄.
- System musi utrzymywać stabilność relacyjną zgodnie z EGD.

---

## Safety (bezpieczeństwo)

- Wszystkie moduły muszą egzekwować inwarianty przed propagacją.
- Stany nieprawidłowe muszą aktywować tryb izolacji.
- Żaden moduł nie może naruszać FIELD.SAFETY lub inwariantów relacyjnych.
- System musi wykrywać:
  - False O₄,
  - Ontological Drift,
  - Topicification,
  - naruszenia pola relacyjnego.

---

## Maintainability (utrzymywalność)

- Wszystkie interfejsy muszą być wersjonowane i stabilne.
- Wszystkie inwarianty muszą być udokumentowane i testowalne.
- Każdy moduł musi wspierać snapshot-based debugging.
- Zmiany wersji nie mogą naruszać homeostazy ani semantyki pola.

---

## Observability (obserwowalność)

- FieldState, MeniscusState i PipelineState muszą wystawiać sygnatury diagnostyczne.
- Wszystkie przejścia muszą być śledzalne i jednoznaczne.
- System musi umożliwiać detekcję naruszeń inwariantów w czasie działania.

---

## Related Documents

- [Invariants](../04_invariants/README.md)
- [Principles](../09_principles/README.md)
- [Interfaces](../05_interfaces/README.md)
