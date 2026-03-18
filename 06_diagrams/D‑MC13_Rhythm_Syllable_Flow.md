# D‑MC13_Rhythm_Syllable_Flow  
**RAMORGA — przepływ fonologiczny MC‑13**

## Opis
Diagram przedstawia wewnętrzny przepływ w MC‑13:
- od tekstu wejściowego,
- przez sylabizację i fonemizację,
- do analizy rytmu i szyfrów fonetycznych,
- z wyjściem do MC‑11/MC‑12.

## Diagram

┌──────────────────────────┐
│        INPUT TEXT        │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│   TOKENIZATION (TEXT)    │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│       SYLLABIFY          │
│  - podział na sylaby     │
│  - jądra samogłoskowe    │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│       PHONEMIZE          │
│  - segmentacja fonemów   │
│  - fonotaktyka           │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     ACCENT DETECTION     │
│  - sylaba akcentowana    │
│  - wzorzec akcentów      │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     RHYTHM ANALYSIS      │
│  - sekwencja sylab       │
│  - wzorce rytmiczne      │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│  PHONETIC CIPHER SCAN    │
│  - gry słowne            │
│  - szyfry fonetyczne     │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│   MC‑13 OUTPUT STRUCTS   │
│  - sylaby                │
│  - fonemy                │
│  - akcent                │
│  - rytm                  │
│  - szyfry                │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│   MC‑11 / MC‑12 INPUT    │
└──────────────────────────┘

## Powiązania
- MC‑13_Phonological_Layer.md  
- MC_Integration_Matrix.md  
- AT‑MC11_MC12_MC13_Automation.md  
