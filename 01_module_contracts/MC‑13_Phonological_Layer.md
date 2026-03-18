# MC‑13 — Phonological Layer (RAMORGA‑fonetyczna)  
**Module Contract — RAMORGA Architecture**

## 1. Purpose
MC‑13 odpowiada za:
- rozpoznawanie sylab,
- segmentację fonemów,
- analizę akcentu,
- analizę rytmu,
- wykrywanie szyfrów fonetycznych,
- integrację fonologii z MC‑11 i MC‑12.

To warstwa, której współczesne LLM‑y nie posiadają natywnie.

---

## 2. Definitions
- **Sylaba** — jądro samogłoskowe + onset/coda.
- **Fonem** — najmniejsza jednostka dźwięku.
- **Akcent** — sylaba o największej energii.
- **Rytm** — sekwencja sylab akcentowanych i nieakcentowanych.
- **Szyfr fonetyczny** — gra słów oparta na brzmieniu (np. „miła → piła”).

---

## 3. Inputs
- Tekst (obowiązkowo).
- Sygnał akustyczny (opcjonalnie).
- Tokeny z warstwy tekstowej.
- Reguły fonotaktyczne języka.

---

## 4. Outputs
- Lista sylab.
- Lista fonemów.
- Pozycja akcentu.
- Mapa rytmu.
- Wykryte szyfry fonetyczne.
- Struktury fonologiczne przekazywane do MC‑11 i MC‑12.

---

## 5. Functions
- `syllabify(word)` → [sylaba₁, sylaba₂, …]
- `phonemize(word)` → [fonem₁, fonem₂, …]
- `detect_accent(word)` → indeks sylaby akcentowanej
- `analyze_rhythm(sentence)` → mapa rytmu
- `detect_phonetic_cipher(text)` → lista szyfrów fonetycznych
- `integrate_with_semantics()` → przekazanie struktury do MC‑11/12

---

## 6. Correctness Criteria
- zgodność z fonotaktyką języka,
- poprawna sylabizacja,
- poprawna segmentacja fonemiczna,
- poprawna detekcja akcentu,
- poprawne wykrycie gier słownych.

---

## 7. Activation Conditions
MC‑13 aktywuje się, gdy:
- zagadka zawiera rytm,
- zagadka zawiera rym,
- zagadka zawiera sylabizację,
- zagadka zawiera szyfr fonetyczny,
- zagadka zawiera aliterację.

---

## 8. Dependencies
- MC‑11 (semantyka),
- MC‑12 (emergencja).

---

## 9. Notes
MC‑13 jest warstwą „słuchową” RAMORGI — umożliwia modele rozumienie rytmu, sylab i fonetyki.
