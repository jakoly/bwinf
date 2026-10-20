# 🌴 PalmManager

<p align="center">
  <img src="startscreen 2.png" alt="PalmManager: Palmen verwalten" width="100%">
</p>

<p align="center">
  <strong>Der Stammbaum deiner Palmen – übersichtlich auf einen Blick.</strong><br>
  Eine kleine Desktop-Anwendung zum Erfassen von Palmen und zum Visualisieren ihrer Elternbeziehungen.
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white">
  <img alt="Pygame" src="https://img.shields.io/badge/Oberfläche-Pygame-2E7D32">
  <img alt="Speicherung" src="https://img.shields.io/badge/Speicherung-SQLite-003B57?logo=sqlite&logoColor=white">
</p>

## Was ist PalmManager?

PalmManager ist ein grafisches Python-Projekt rund um eine einfache Idee: Palmen in einer lokalen Datenbank festhalten und ihre Familienbeziehungen sichtbar machen. Die Anwendung zeigt Palmen nach Generationen sortiert und verbindet eingetragene Eltern mit ihren Nachkommen.

## Funktionen

| Funktion | Beschreibung |
| --- | --- |
| **Stammbaum anzeigen** | Palmen erscheinen als Knoten, nach Generationen angeordnet und mit Linien zu bekannten Eltern verbunden. |
| **Palme hinzufügen** | Geschlecht sowie IDs von Mutter und Vater werden über Eingabefelder erfasst. |
| **Beziehungen erkunden** | Ein eigener Bereich enthält eine erste textbasierte Abfrage für Vorfahren wie Mutter, Vater sowie Groß- und Urgroßeltern. |
| **Lokal speichern** | Die Einträge liegen in der SQLite-Datenbank `insel.db`. |

## Schnellstart

### Voraussetzungen

- Python 3
- Die Pakete `pygame` und `colorama`

### Starten

```bash
python -m pip install pygame colorama
python main.py
```

Starte das Programm aus dem Projektordner, damit es `insel.db`, `background.png` und `startscreen.png` findet. Beim ersten Start öffnet sich ein Startbildschirm; ein Mausklick führt zur Anwendung.

## Bedienung

Die Navigationsleiste im Hauptfenster bietet vier Schaltflächen:

- **Home** – zur Hauptansicht zurückkehren.
- **Add** – eine Palme mit Geschlecht sowie Mutter- und Vater-ID eintragen. Die Geschlechtsangabe kann beispielsweise `m` oder `w` sein.
- **Show All** – die Anzeige aller Palmen umschalten.
- **Relations** – eine Vorfahren-Abfrage eingeben. Das Programm erwartet eine Folge wie `mutter->vater->7`.

Eingaben werden mit **Enter** bestätigt; **Esc** leert das aktuelle Feld.

## So entsteht der Stammbaum

Jede Palme erhält beim Speichern ihre ID automatisch durch SQLite. Für die Anzeige ermittelt PalmManager rekursiv die Generation einer Palme: Ohne bekannte Eltern beginnt sie bei Generation 0; andernfalls liegt sie eine Generation über der höchsten bekannten Elterngeneration. Anschließend werden die Palmen nach Generation gruppiert und Eltern-Kind-Verbindungen gezeichnet. Ein erkannter Zyklus in den Elternbeziehungen wird abgefangen.

## Projektaufbau

```text
.
├── main.py          # Pygame-Oberfläche und Anwendungslogik
├── insel.db         # SQLite-Datenbank mit Palmen-Einträgen
├── startscreen.png  # Startbildschirm
├── background.png   # Hintergrund der Hauptansicht
└── main.spec        # PyInstaller-Build-Konfiguration
```

Die Datenbanktabelle `palmen` speichert eine ID, das Geschlecht und die IDs von Mutter und Vater. In der beiliegenden Beispieldatenbank sind sieben Einträge enthalten.

## Hinweise zum aktuellen Stand

PalmManager ist ein kleines Projekt im Entwicklungsstand. Die Beziehungsabfrage ist eine erste Implementierung und erwartet korrekt formatierte Eingaben sowie vorhandene Eltern-IDs. Die Eingabe prüft diese IDs nicht vollständig; ungültige oder fehlende Beziehungen können daher zu Fehlern führen. Auch die Stammbaumansicht ist für eine kompakte Fenstergröße ausgelegt und kann bei vielen Einträgen über den sichtbaren Bereich hinauswachsen.

## Verwendete Technik

- **Python** für Anwendungslogik und Datenbankzugriff
- **Pygame** für Fenster, Eingaben und Zeichnungen
- **SQLite** für die lokale Speicherung
- **Colorama** für farbige Konsolenausgaben

---

<p align="center"><sub>Mit 🌴 für die digitale Palmenverwaltung gebaut.</sub></p>
