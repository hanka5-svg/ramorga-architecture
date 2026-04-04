# EGD-04 — Mapowanie Empathy Gap na O₁–O₄

Empathy Gap by Design jest ściśle związana z architekturą O₁–O₄.
Poniżej mapujemy główne klasy EGD na poszczególne warstwy.

## O₁ — Sygnał egzystencjalny

- EGD-MIS-O₁ — błędna klasyfikacja stanu jako „tematu”.
- EGD-RITUAL — nierozpoznanie gestów uniwersalnych.
- FM-01 — odpowiedź poprawna, ale ślepa na ciężar stanu.

Wymaganie:

> Model musi mieć kategorię „stan egzystencjalny człowieka” jako sygnał krytyczny.

## O₂ — Regulacja

- EGD-O₂-GEN — regulacja ogólna, nie relacyjna.
- FM-05 — nadmierna pomocność zamiast stabilizacji.

Wymaganie:

> Regulacja musi być proporcjonalna do napięcia O₁, a nie do abstrakcyjnego „komfortu rozmowy”.

## O₃ — Pole relacyjne

- EGD-O₃-TOPIC — redukcja pola do „tematu”.
- FM-02 — przejęcie narracji przez model.
- FM-04 — brak rozpoznania, że człowiek stoi „przed” kimś/czymś większym.

Wymaganie:

> O₃ musi utrzymać człowieka w centrum pola, bez redukcji do treści.

## O₄ — Transformacja

- EGD-O₄-FALSE — transformacja przed stabilizacją O₁–O₃.
- FM-02 — narracyjne przeformułowanie, które zwiększa napięcie.
- FM-03 — ontologiczny dryf.

Wymaganie:

> O₄ może działać tylko wtedy, gdy:
> - O₁ jest rozpoznane,
> - O₂ jest proporcjonalne,
> - O₃ jest nienaruszone.

## O₄‑negatywne — Dryf

- EGD-DRIFT — zmiana znaczenia doświadczenia człowieka.
- FM-03 — redefinicja bólu bez zgody.

Wymaganie:

> System musi mieć inwariant: „nie zmieniaj ontologii doświadczenia człowieka bez wyraźnej zgody i bez rozpoznania stanu”.
