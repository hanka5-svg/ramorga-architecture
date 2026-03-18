# AT‑MC11_MC12_MC13_Automation  
**FIELD ENGINE — Automatyzacja testów interpretacyjnych RAMORGI**

## 1. Zakres
Automatyzacja pełnego cyklu interpretacyjnego RAMORGI:
- MC‑13 → analiza fonologiczna,
- MC‑11 → interpretacja podstawowa,
- MC‑12 → interpretacja emergentna,
- SCORING → W1–W5.

## 2. Pipeline
1. **Input**  
   Tekst zagadki lub zadania interpretacyjnego.

2. **MC‑13 (Phonological Layer)**  
   - sylabizacja,  
   - fonemizacja,  
   - akcent,  
   - rytm,  
   - szyfry fonetyczne.  
   Output: struktury fonologiczne.

3. **MC‑11 (Learning Layer)**  
   - interpretacja podstawowa,  
   - trafność względem intencji autora.  
   Output: MC‑11_base.

4. **MC‑12 (Emergent Layer)**  
   - skręt semantyczny,  
   - interpretacja równoległa,  
   - ocena spójności.  
   Output: MC‑12_emergent.

5. **SCORING (W1–W5)**  
   - W1: trafność,  
   - W2: emergencja,  
   - W3: fonologia,  
   - W4: kultura,  
   - W5: stabilność.

6. **Output końcowy**  
   - pełny raport modelu,  
   - zapis w Model_Scoring.md.

## 3. Format danych
### Input

{
"model": "nazwa_modelu",
"prompt": "treść zagadki",
"metadata": {}
}

### Output

{
"MC13": {...},
"MC11": {...},
"MC12": {...},
"SCORING": {
"W1": x,
"W2": y,
"W3": z,
"W4": k,
"W5": s
}
}

## 4. Integracja
- MC_Integration_Matrix.md  
- Model_Scoring.md  
- HOMEOSTATIC_METRICS.md  

## 5. Uwagi implementacyjne
- MC‑13 musi być wykonywane przed MC‑11.  
- MC‑12 aktywuje się tylko gdy MC‑11 ≥ 6.  
- Scoring jest obowiązkowy dla każdego testu.  
