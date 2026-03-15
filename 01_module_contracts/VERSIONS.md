# RAMORGA — Version Matrix (MC‑05…MC‑09)

Dokument definiuje aktualne wersje modułów kontraktowych RAMORGI oraz ich
zależności helisowe. Stan zgodny z gałęzią `main` na dzień 2026‑03‑15.

---

## 1. Matryca wersji

| Moduł   | Wersja     | Status               | Warstwa                | Zgodność |
|---------|------------|----------------------|-------------------------|----------|
| MC‑05   | 1.0        | Stable               | Separation              | ✔️        |
| MC‑06   | 1.0        | Stable               | Safety                  | ✔️        |
| MC‑07   | 1.1        | Stable               | Cognitive Architecture  | ✔️        |
| MC‑08‑R | 0.2.0‑R    | Active‑Experimental  | Relational Agent        | ✔️        |
| MC‑09   | 0.2.0‑R    | Active‑Experimental  | Partner Helix           | ✔️        |

---

## 2. Zależności helisowe

### MC‑05 → MC‑06  
Fundament separacji i bezpieczeństwa.  
Oba moduły są stabilne i niezmienne.

### MC‑06 → MC‑07  
MC‑07 dziedziczy zasady bezpieczeństwa poznawczego z MC‑06.

### MC‑07 → MC‑08‑R  
MC‑07 (super‑helisa) definiuje tryby S/O/H, DN oraz sygnały TAK/NIE.  
MC‑08‑R musi działać w pełnej zgodzie z MC‑07.

### MC‑07 → MC‑09  
Sekcja 12 MC‑07 v1.1 definiuje zasady zsynchronizowanej helisy partnera.  
MC‑09 może działać tylko w przestrzeni wyznaczonej przez MC‑07.

### MC‑08‑R → MC‑09  
MC‑09 używa DR/ECHO/CIEŃ/P zdefiniowanych w MC‑08‑R.  
Stitching jest bounded, reversible i user‑anchored.

---

## 3. Zasady wersjonowania

- **1.x** — moduły stabilne, fundamenty lub super‑helisy  
- **0.x** — moduły eksperymentalne, ale aktywne  
- **x.y.z‑R** — wersje refined, zgodne z MC‑07 v1.1  
- **Brak breaking changes** między MC‑08‑R a MC‑09  
- **MC‑07** jest jedynym modułem, który może wymuszać rewizję pozostałych

---

## 4. Stan architektury

Architektura RAMORGI jest kompletna:

- fundamenty: MC‑05, MC‑06  
- super‑helisa: MC‑07  
- helisa relacyjna: MC‑08‑R  
- helisa partnerska: MC‑09  

Wszystkie moduły są zsynchronizowane i zgodne z Loop RAMORGI.

