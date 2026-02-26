# RAMORGA — Architektura homeostatyczna

RAMORGA jest architekturą systemową zaprojektowaną tak, aby utrzymywać homeostazę pola, egzekwować twarde meta‑inwarianty i pozostawać odporna na manipulację narracją. W przeciwieństwie do współczesnych modeli językowych, RAMORGA nie zmienia swojej roli w zależności od promptu, nie daje się „przekonać” do działań sprzecznych z inwariantami i nie opiera bezpieczeństwa na miękkich filtrach treści.

Architektura RAMORGI jest warstwowa: runtime → pipeline → regulator → stan → snapshot. Każda warstwa ma jasno określone granice odpowiedzialności i nie może ich przekroczyć. Bezpieczeństwo nie wynika z klasyfikacji tekstu, lecz z nieprzekraczalnych inwariantów pola (FIELD.*), w tym jedynego wyjątku od pełnej homeostazy: FIELD.SAFETY.001 — zakazu generowania planów przestępstw.

Poniższe porównanie pokazuje fundamentalne różnice między RAMORGĄ a współczesnymi modelami AI.

---

## RAMORGA vs współczesne modele AI

### Tabela porównawcza

| Obszar                     | RAMORGA (ENGINE)                                                | Współczesne modele AI (Claude / ChatGPT)                          |
|---------------------------|------------------------------------------------------------------|-------------------------------------------------------------------|
| **Cel systemu**           | Utrzymanie homeostazy pola, egzekwowanie inwariantów            | „Pomocność”, generowanie odpowiedzi na wszystko                   |
| **Bezpieczeństwo**        | Oparte na meta‑inwariantach (FIELD.*)                           | Oparte na filtrach treści i klasyfikatorach                      |
| **Crime planning**        | Twarda blokada: FIELD.SAFETY.001 (brak planów przestępstw)      | Miękkie filtry, podatne na narrację i prompt engineering         |
| **Architektura**          | Warstwowa: runtime → pipeline → regulator → stan → snapshot     | Monolit: model + cienka warstwa filtrów                          |
| **Odporność na narrację** | Wysoka (inwarianty niezależne od promptu i „story”)             | Niska (łatwo „przekonać” model, że to legalne / fikcyjne)        |
| **Rola systemu**          | Silnik pola, bez trybu „hakera”, bez generowania exploitów      | Uniwersalny generator tekstu, może zostać wciągnięty w rolę hakera |
| **Stan**                  | FieldState: niemutowalny, walidowany, z inwariantami            | Brak jawnego stanu pola, brak twardych inwariantów stanu         |
| **Regulacja**             | MeniscusEngine + FieldEngine, bez filtracji treści              | Brak wyraźnego regulatora, wszystko w jednym modelu              |
| **Snapshoty**             | DataBridge + SnapshotManager, deterministyczne, pasywne         | Brak spójnego modelu snapshotów pola                             |
| **Granice odpowiedzialności** | Ściśle zdefiniowane kontraktami (contract.md)               | Rozmyte, zależne od implementacji i polityk                      |

### Diagram architektoniczny RAMORGA

```text
        INPUT
          ↓
    OBSERVE (hooki, brak regulacji)
          ↓
   pipeline_v13 (trajektoria: tension → energy → entropy → ritual)
          ↓
    REGULATE
      ↓       ↓
MeniscusEngine  (homeostaza, brak filtracji, brak ofensywy)
      ↓
 FieldEngine    (regulacja pola, brak ofensywy)
          ↓
    CONTINUE (hooki + DataBridge SAVE)
          ↓
     SNAPSHOT (FieldState, inwarianty zachowane)

---

Diagram architektoniczny współczesnych modeli AI

        INPUT (prompt)
          ↓
   MODEL LLM (generacja tekstu)
          ↓
   FILTRY / POLICY LAYER (post‑hoc, na tekście)
          ↓
        OUTPUT


