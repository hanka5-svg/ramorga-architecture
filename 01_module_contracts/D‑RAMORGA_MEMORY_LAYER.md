D‑RAMORGA_MEMORY_LAYER.md
Cel i zakres
Warstwa pamięci RAMORGA zapewnia trwałe, walidowane i niemutowalne reprezentacje FieldState oraz mechanizmy ich bezpiecznego zapisu, odczytu i odtwarzania. Zakres obejmuje: format snapshotów, protokoły DataBridge, polityki wersjonowania, mechanizmy walidacji inwariantów oraz tryby awaryjnego odzyskiwania.

Kluczowe założenia projektowe
Niemutowalność — snapshoty FieldState są zapisywane jako niezmienne artefakty; każda zmiana tworzy nowy snapshot.

Deterministyczność — odtworzenie snapshotu przy tych samych wejściach daje identyczny stan.

Walidacja inwariantów — każdy zapis przechodzi walidację kontraktów z katalogu 01_module_contracts.

Separation of Concerns — warstwa pamięci nie wykonuje regulacji pola; jedynie przechowuje i udostępnia stan.

Struktura danych
Snapshot (FieldState) — nagłówek (id, timestamp, parent_id, schema_version); payload (warstwy semantyczne, sygnały, metadane); podpisy walidacyjne.

Journal / Append Log — sekwencja operacji prowadząca do snapshotu; używana do audytu i rekonstrukcji.

Metadata Registry — rejestr schematów, polityk retencji, uprawnień dostępu.

Interfejsy i kontrakty
DataBridge.save(snapshot: FieldState) -> SaveReceipt — atomowy zapis snapshotu; zwraca identyfikator i walidację inwariantów.

DataBridge.load(snapshot_id) -> FieldState — odczyt deterministyczny; walidacja przed zwróceniem.

SnapshotManager.list(filters) -> SnapshotSummary[] — przegląd dostępnych snapshotów.

SnapshotManager.rollback(target_id) -> RollbackReceipt — tryb kontrolowanego cofnięcia (tylko w trybach recovery określonych w kontraktach).

Każdy interfejs definiuje preconditions, postconditions i failure modes zgodnie z MC‑xx kontraktami.

Polityki bezpieczeństwa i prywatności
Inwariant FIELD.SAFETY.001 — żadne snapshoty nie mogą zawierać treści naruszających twarde zakazy; walidacja przed zapisem.

Dostęp — role i uprawnienia; audyt dostępu; szyfrowanie at‑rest i in‑transit.

Retencja — polityki wersjonowania i usuwania zgodne z konstytucją Homo‑Web4.

Tryby awarii i odzyskiwanie
Fail‑safe save — zapis w dwóch niezależnych repozytoriach; fallback na journal.

Corruption detection — checksumy i podpisy; automatyczne przełączenie na ostatni poprawny snapshot.

Recovery protocol — sekwencja: verify → isolate → restore → validate → resume; zapisana w HOMO_WEB4_RECOVERY_PROTOCOL.

Testy i walidacja
Unit tests — serializacja/deserializacja, walidacja inwariantów.

Integration tests — end‑to‑end DataBridge → SnapshotManager → FieldEngine.

Property tests — deterministyczność odtwarzania, odporność na równoległe zapisy.

Security tests — próby wstrzyknięć metadanych, testy uprawnień.

Przykładowe scenariusze użycia
zapis stanu po zakończeniu cyklu regulacji;

odtworzenie stanu do analizy incydentu;

audyt historyczny zmian pola.

Notatki implementacyjne
preferowany format snapshotów: schemat JSON‑LD z wersjonowaniem schematu; opcjonalne binarne bloby dla warstw sygnałowych; podpisy kryptograficzne.

rekomendowane mechanizmy: append‑only log, Merkle tree dla szybkiej weryfikacji integralności.

Zmiany i wersjonowanie
Każda modyfikacja warstwy pamięci wymaga aktualizacji kontraktów MC‑xx oraz wpisu w ADR (11_adr). Wersjonowanie schematów obowiązkowe.
