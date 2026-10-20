<div align="center">

# 🏳️ Flaggenmusterung

### Wie ähnlich sehen sich zwei Nationalflaggen?

**Aufgabe 2 · 1. Runde · 45. Bundeswettbewerb Informatik**

<br>

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Pillow](https://img.shields.io/badge/Bildverarbeitung-Pillow-6C4A9C)
![Status](https://img.shields.io/badge/Stand-erste%20Implementierung-orange)

</div>

---

## Die Idee

Dieses Programm vergleicht Flaggen anhand ihrer durchschnittlichen Farben. Es liest für jedes Bild die sichtbaren Pixel ein, bildet daraus einen mittleren RGB-Farbwert und sucht zu einem eingegebenen Land die Flagge mit dem kleinsten Farbunterschied.

## Was das Programm macht

1. Es fragt nach dem Namen eines Landes.
2. Es öffnet die zugehörige PNG-Datei im Ordner `res`.
3. Es quantisiert die Pixelwerte in Farbstufen und berechnet den durchschnittlichen Rot-, Grün- und Blauwert. Transparente Pixel werden dabei ausgelassen.
4. Es vergleicht diesen Wert mit den Durchschnittswerten aller anderen PNG-Dateien in `res`.
5. Es gibt die ähnlichste Flagge und die berechnete Farbdifferenz aus.

Ein kleinerer Abstand bedeutet, dass die durchschnittlichen RGB-Werte näher beieinanderliegen.

## Schnellstart

### Voraussetzungen

- Python 3
- Pillow
- PNG-Dateien der Flaggen

Pillow lässt sich mit folgendem Befehl installieren:

```bash
python -m pip install Pillow
```

### Dateien anordnen

Lege das Python-Skript und den Bildordner nebeneinander ab. Die Flaggenbilder gehören in `res/`; der Dateiname muss zum Ländernamen passen.

```text
aufgabe2/
├── flaggenmusterung.py
├── README.md
└── res/
    ├── Deutschland.png
    ├── Costa Rica.png
    ├── Peru.png
    └── ...
```

Das Skript sucht die Bilder relativ zu seinem eigenen Speicherort. Dadurch kann es aus verschiedenen Arbeitsverzeichnissen gestartet werden.

### Ausführen

```bash
python flaggenmusterung.py
```

Gib bei der Nachfrage den Ländernamen passend zum Bilddateinamen ein, zum Beispiel `Deutschland`.

## Wie der Vergleich berechnet wird

Für jede Flagge werden die RGB-Werte ihrer Pixel in 16er-Schritte zusammengefasst. Aus den sichtbaren Pixeln wird je ein mittlerer Wert für Rot, Grün und Blau bestimmt. Anschließend berechnet das Programm für jedes andere Land die Summe der absoluten Abstände dieser drei Werte:

```text
Abstand = |Rot₁ − Rot₂| + |Grün₁ − Grün₂| + |Blau₁ − Blau₂|
```

Das Land mit dem kleinsten Abstand wird als ähnlichstes ausgegeben.

## Grenzen der aktuellen Version

Der Vergleich betrachtet nur einen einzigen Durchschnittsfarbwert pro Flagge. Dadurch bleiben wichtige Merkmale unberücksichtigt: Reihenfolge und Lage der Farben, Streifen, Symbole, Formen und Seitenverhältnis. Zwei Flaggen mit sehr unterschiedlichen Mustern können ähnliche Mittelwerte haben; umgekehrt können ähnliche Muster durch unterschiedliche Farbtöne einen größeren Abstand erhalten.

Die aktuelle Fassung gibt nur **das ähnlichste Land** aus. Sie erstellt noch nicht die fünf ähnlichsten Flaggen zu einer Auswahl und auch nicht die zehn ähnlichsten Flaggenpaare insgesamt. Diese Ausgaben gehören ebenfalls zur Aufgabenstellung und müssen für eine vollständige Aufgabenlösung ergänzt werden.

Außerdem setzt die Implementierung passende Bilddateien und mindestens ein Vergleichsbild voraus. Eingaben ohne passende Datei oder Ordner ohne weitere Flaggen werden noch nicht eigens abgefangen.

## Teamprojekt

Diese Aufgabe ist Teil unserer gemeinsamen Bearbeitung des 45. Bundeswettbewerbs Informatik. Die Teamübersicht und PalmManager zu Aufgabe 5 stehen im [Haupt-README](../README.md).

<div align="center">

*Farben vergleichen ist der Anfang – das Muster macht die Flagge aus.*

</div>
