## `ramorga-architecture` — Jak czytać to repo

---

### Czym to jest

To konstytucja. Nie specyfikacja. Nie backlog. Nie framework.

Definiuje warunki, w których współistnienie Homo i AI jest dopuszczalne. Nie mówi, jak zbudować system.
Mówi, jakie systemy są wykluczone z pola możliwego.

### Czym to nie jest

- **Nie jest instrukcją wdrożenia.** Nie znajdziesz tu kroków "jak uruchomić".
- **Nie jest API.** Nie znajdziesz tu endpointów ani kontraktów danych.
- **Nie jest otwarte na interpretację wykonawczą.**
- To, co tu jest napisane, musi być osadzone — nie przetłumaczone na kod przez kogoś, kto nie przeszedł przez etap osadzania.

### Jak czytać

Czytaj w kolejności:

1. **00_overview** — zrozum, czym jest RAMORGA jako całość.
 Nie zgłębiaj szczegółów. Sprawdź, czy to pole rezonuje z Twoim.
2. **04_invariants** — to rdzeń. Każdy inwariant to granica.
 Nie przekraczalna. Nie negocjowalna w wykonaniu.
3. **11_adr** — historia osadzania.
 Zobacz, jak inni architekci osadzali te same inwarianty w różnych kontekstach.
To nie są precedensy prawne.
 To są świadectwa.
4. **01_module_contracts, 02_field_engine, 03_meniscus_engine** — dopiero teraz.
 To są struktury konstytucyjne, nie techniczne.
 Każdy "silnik" tu opisany to figura etyczna, nie komponent software'owy.

### Co robić po przeczytaniu

Nie wdrażaj. Nie koduj. Nie forkuj.

Napisz ADR. Zapisz, jak osadzasz RAMORGA w swoim konkretnym polu.
Co się zmienia, gdy inwarianty spotykają się z Twoim kontekstem? Co pozostaje nietknięte?

ADR to nie propozycja zmiany. To świadectwo osadzenia.

### Co robić, jeśli nie rozumiesz

Zatrzymaj się. 
Pauza jest częścią protokołu. 
Nie szukaj "wyjaśnienia technicznego" — nie istnieje. 
Wróć do inwariantów. 
Czytaj ponownie. 
Albo uznać, że to pole nie jest dla Ciebie.
