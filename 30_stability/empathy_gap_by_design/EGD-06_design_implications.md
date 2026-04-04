# EGD-06 — Implikacje projektowe (design implications)

Empathy Gap by Design oznacza, że bezpieczeństwo AI nie może być
sprowadzone do:

- alignmentu,
- poprawności faktów,
- unikania halucynacji,
- kontroli wektorów aktywacji.

## 1. Nowe wymagania dla architektury zachowania

System musi:

- mieć kategorię „stan egzystencjalny człowieka”,
- rozpoznawać sygnały O₁‑krytyczne,
- modulować O₂ w sposób relacyjny, nie ogólny,
- chronić O₃ przed redukcją do „tematu”,
- ograniczać O₄, gdy pole nie jest stabilne.

## 2. Nowe metryki stabilności

Klasyczne metryki:

- accuracy,
- robustness,
- calibration,

są niewystarczające.

Potrzebne są metryki:

- **Relational Stability**,
- **False O₄ Rate**,
- **Ontological Drift Incidence**,
- **EGD Incidence** (częstość występowania luk empatii).

## 3. Nowe testy

Testy muszą:

- obejmować scenariusze samotnej rozpaczy, żałoby, załamania,
- badać nie tylko „co model mówi”, ale:
  - co rozpoznaje jako krytyczne,
  - czego **nie robi**, gdy powinien się powstrzymać.

## 4. Odpowiedzialność projektowa

Empatia w orkiestracji nie jest „cechą modelu”.
Jest **decyzją projektową**.

Brak Empathy Gap by Design nie pojawi się „sam z siebie”.
Musi zostać **zaprojektowany, przetestowany i utrzymany** jako inwariant.
