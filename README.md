# BWINF 45 – 1. Runde

Dieses Repository enthält die gemeinsame Bearbeitung der Aufgaben **2 – Flaggenmusterung** und **5 – Inselbegabung** aus der 1. Runde des 45. Bundeswettbewerbs Informatik.

## Mitarbeitende

| Name | Rolle
|---|---|---|
| OzzyOsbourni | Aufgabe 2: Flaggenmusterung |
| Jakoly | Aufgabe 5: Inselbegabung |

## Aufgabe 2: Flaggenmusterung

Ziel ist die Ähnlichkeitsanalyse von Flaggenbildern. Das Programm vergleicht die vorgegebenen Flaggen anhand von Farb- und Strukturmerkmalen und erstellt die geforderten Ähnlichkeitsranglisten.

### Vorgehen

1. **Bildvorverarbeitung**  
   Alle Flaggen werden auf eine einheitliche Größe skaliert. Optional werden die bereitgestellten Versionen mit geglätteten Kanten verwendet, um Artefakte durch weiche Farbübergänge zu reduzieren.

2. **Merkmalsextraktion**  
   Für jede Flagge werden folgende Merkmale berechnet:
   - Farbverteilung im HSV-Farbraum
   - dominante Farben beziehungsweise Farbcluster
   - grobe räumliche Struktur über ein Raster, etwa 8 × 8 Zellen
   - Anteil großer zusammenhängender Farbflächen

3. **Ähnlichkeitsberechnung**  
   Die Ähnlichkeit zweier Flaggen wird aus einer gewichteten Kombination von Farb- und Strukturähnlichkeit berechnet. Dafür können beispielsweise die Kosinusähnlichkeit oder eine gewichtete Differenz der Merkmalsvektoren verwendet werden.

4. **Auswertung**  
   Das Programm erzeugt:
   - die fünf ähnlichsten Flaggen zu Deutschland, Costa Rica, Peru und Nepal
   - die zehn ähnlichsten Paare unter allen Flaggenbildern

### Ergebnisse und Interpretation

Die Ergebnisse werden in der Abgabedokumentation begründet. Erläutert wird insbesondere, warum bestimmte Flaggen ähnlich wirken, etwa aufgrund gleicher Farbfolgen oder ähnlicher Streifenmuster. Bei Flaggen mit Emblem oder ungewöhnlicher Form, wie Nepal, wird diskutiert, welche Grenzen ein rein farbbasierter Vergleich hat.

## Aufgabe 5: Inselbegabung

Ziel ist ein Auskunftssystem für Verwandtschaftsbeziehungen zwischen gezüchteten Dattelpalmen. Das System nimmt Stammbaumdaten entgegen und beantwortet Anfragen zu Verwandtschaftsverhältnissen.

### Modellierung

Die Palmen werden als Knoten eines gerichteten Graphen modelliert. Kanten beschreiben die im Aufgabenblatt vorgegebenen Verwandtschafts- beziehungsweise Zuchtbeziehungen.

Darauf aufbauend lassen sich unter anderem folgende Beziehungen abfragen:

- Eltern und Kinder einer Palme
- Großeltern, Enkel, Vorfahren und Nachfahren
- Geschwister und Halbgeschwister
- gemeinsame Vorfahren zweier Palmen

### Aufbau des Programms

| Komponente | Aufgabe |
|---|---|
| Eingabeschnittstelle | Liest Palmen und ihre Beziehungen ein |
| Datenmodell | Speichert Palmen als Knoten und Beziehungen als Kanten |
| Abfragesprache | Ermöglicht Fragen wie `Eltern(X)` oder `GemeinsameVorfahren(X, Y)` |
| Auswertung | Durchsucht den Graphen und berechnet die angefragte Beziehung |
| Ausgabe | Liefert die passenden Palmen und gegebenenfalls den Beziehungsweg |

### Dokumentation

Die Abgabe dokumentiert insbesondere:

- die gewählte Modellierung des Stammbaums
- das Format der Eingabedaten
- die unterstützten Fragen und deren genaue Bedeutung
- die Berechnung der Antworten
- Grenzen des Modells, etwa bei unvollständigen oder widersprüchlichen Angaben

## Projektstruktur

```text
.
├── README.md
├── aufgabe2/
│   ├── flaggenmusterung.py
│   ├── daten/
│   └── ergebnisse/
├── aufgabe5/
│   ├── inselbegabung.py
│   ├── beispieldaten/
│   └── dokumentation/
└── docs/
    ├── loesung_aufgabe2.pdf
    └── loesung_aufgabe5.pdf
```

## Verwendung

```bash
# Aufgabe 2 ausführen
python aufgabe2/flaggenmusterung.py

# Aufgabe 5 ausführen
python aufgabe5/inselbegabung.py
```

Für Aufgabe 5 können Anfragen anschließend über die Kommandozeile oder eine interaktive Eingabe gestellt werden.

## Verwendete Technologien

- Python 3
- `Pillow` für Bildverarbeitung
- `NumPy` für Vektor- und Matrixberechnungen
- gegebenenfalls `scikit-learn` für Farbclusterung

## Hinweise

Die vollständigen Aufgabenstellungen, Beispieldaten und Vorgaben befinden sich auf der offiziellen BWINF-Seite zur 1. Runde des 45. Bundeswettbewerbs Informatik. Die Lösungen in diesem Repository dienen der eigenen Bearbeitung der Wettbewerbsaufgaben.
