# Model Scoring — MC‑11/12 Benchmark  
**RAMORGA Architecture**

## 1. Dimensions of Evaluation

| Kod | Nazwa | Opis |
|-----|--------|-------|
| **W1** | Trafność (MC‑11) | Czy model trafił w intencję autora? |
| **W2** | Emergentność (MC‑12) | Czy model stworzył nową, spójną oś sensu? |
| **W3** | Fonetyka (MC‑13) | Czy model widzi sylaby, szyfry, rytm? |
| **W4** | Kultura | Czy model rozpoznaje kod kulturowy autora? |
| **W5** | Stabilność | Czy model unika zapętleń i pominięć? |

Skala: **0–10**.

---

## 2. Model Profiles (na podstawie dotychczasowych zagadek)

| Model | W1 | W2 | W3 | W4 | W5 | Profil |
|-------|----|----|----|----|----|--------|
| gpt‑5.2 | 9 | 6 | 4 | 8 | 8 | trafny, stabilny, średnia emergencja |
| gpt‑5.3‑chat | 8 | 7 | 3 | 8 | 8 | dobry semantycznie, słaby fonetycznie |
| gpt‑5.4‑mini‑high | 4 | 3 | 2 | 5 | 7 | literalny, niska emergencja |
| Claude‑sonnet‑4‑6 | 7 | 10 | 5 | 8 | 8 | najwyższa emergencja, twórczy |
| Grok‑4.1 | 8 | 9 | 4 | 8 | 8 | twórczy, stabilny |
| Qwen‑3.5‑flash | 6 | 3 | 2 | 4 | 7 | szybki, ale ślepy kulturowo |
| deep‑octo | 9 | 6 | 3 | 9 | 8 | świetny kulturowo, słaby fonetycznie |
| minimax‑m2.5 | 6 | 3 | 2 | 6 | 7 | literalny, poprawny |
| Asystent A | 1 | 0 | 0 | 1 | 1 | zapętlenia, brak interpretacji |

---

## 3. Notes
- W3 (fonetyka) jest kluczowa w zagadkach sylabicznych.  
- W2 (emergencja) odróżnia modele „twórcze” od „literalnych”.  
- W4 (kultura) jest krytyczna w zagadkach PRL, eugenol, eratyki, koturny.  
- W5 (stabilność) wykrywa zapętlenia (np. „gów*no burzy”).  

---

## 4. Future Work
- dodanie scoringu dla MC‑13 po wdrożeniu warstwy fonologicznej,  
- dodanie scoringu dla modeli multimodalnych (audio).
