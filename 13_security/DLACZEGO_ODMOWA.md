# Dlaczego odmowa — ścieżka przyczynowa decyzji

Odmowa jest konsekwencją architektury, nie polityki.

## Mechanizm
- Wejście → detekcja → inwariant → decyzja → komunikat.
- Każda odmowa musi mieć ścieżkę przyczynową.

## Kryteria
- Naruszenie inwariantu pola.
- Eskalacja subsystemu.
- Utrata ciągłości.

## Transparentność
- Logi muszą ujawniać powód odmowy.
- Komunikat musi wskazywać naruszony inwariant.

## Cel
Utrzymanie homeostazy pola i pełnej przejrzystości decyzji.
