<div align="center">

# BWINF 45 · 1. Runde

### Drei Aufgaben. Drei Perspektiven. Ein Team.

**Unsere gemeinsame Bearbeitung der Aufgaben 1, 2 und 5**  
Kreuzwortkreuze · Flaggenmusterung · Inselbegabung

<br>

<img src="startscreen.png" alt="PalmManager – Dattelpalmen-Stammbaum" width="82%">

<br>

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/GUI-Pygame-2E7D32)
![SQLite](https://img.shields.io/badge/Datenbank-SQLite-003B57?logo=sqlite&logoColor=white)
![Team](https://img.shields.io/badge/Team-3%20Mitglieder-7C5CFC)

</div>

---

## Unser Projekt

Wir sind ein **dreiköpfiges Team** und bearbeiten in der ersten Runde des 45. Bundeswettbewerbs Informatik drei unterschiedliche Problemstellungen. Dieses Repository bündelt unsere Ansätze, Programme und Dokumentationen. Jede Aufgabe hat ihren eigenen Bereich; so bleiben Lösungen unabhängig und lassen sich trotzdem gemeinsam weiterentwickeln.

## Die Aufgaben

<table>
<tr>
<td width="33%" valign="top">

### 01 · Kreuzwortkreuze

Wir entwickeln einen Algorithmus, der Kreuzwortkreuze der vorgegebenen Form mit Wörtern aus der BWINF-Wortliste löst. Das Programm soll die Beispiele aus der Aufgabenstellung bearbeiten und passende Wortbelegungen ausgeben.

**Im Mittelpunkt:** systematische Suche und Prüfung horizontaler und vertikaler Wörter.

</td>
<td width="33%" valign="top">

### 02 · Flaggenmusterung

Wir vergleichen Nationalflaggen und bestimmen, welche einander am ähnlichsten sind. Für eine ausgewählte Flagge sollen die fünf ähnlichsten Flaggen erscheinen; außerdem ermittelt das Programm die zehn ähnlichsten Paare.

**Im Mittelpunkt:** Bildmerkmale, Farbverteilungen und nachvollziehbare Ähnlichkeitsbewertung.

</td>
<td width="33%" valign="top">

### 05 · Inselbegabung

Wir entwickeln ein Auskunftssystem für die Verwandtschaftsverhältnisse gezüchteter Dattelpalmen. Palmen und ihre Eltern werden erfasst, als Stammbaum dargestellt und über Verwandtschaftsanfragen ausgewertet.

**Im Mittelpunkt:** Datenmodell, Eingabe und verständliche Abfragen über mehrere Generationen.

</td>
</tr>
</table>

## Aufgabe 5 in Aktion · PalmManager

Der bereits integrierte Teil des Projekts ist **PalmManager**, eine grafische Anwendung zur Verwaltung des Dattelpalmen-Stammbaums.

- Palmen mit Geschlecht sowie Mutter- und Vater-ID erfassen
- bekannte Eltern-Kind-Verbindungen generationenweise anzeigen
- einfache Vorfahren-Abfragen eingeben
- Daten lokal in SQLite speichern

### Starten

Voraussetzung ist Python 3. Installiere die benötigten Pakete und starte PalmManager aus dem Projektordner:

```bash
python -m pip install pygame colorama
python main.py
```

Beim Programmstart erscheint ein Begrüßungsbildschirm. Ein Mausklick öffnet die Anwendung. Die Navigationsleiste führt zu den Ansichten **Home**, **Add**, **Show All** und **Relations**.

Für eine Vorfahren-Abfrage kann zum Beispiel folgende Kette eingegeben werden:

```text
mutter->vater->7
```

Die Eingabe wird von der Palme mit ID `7` aus ausgewertet. Die Abfragefunktion ist derzeit eine erste Implementierung und unterstützt noch keine allgemeine Sprache für beliebige Verwandtschaftsfragen.

## Repository-Aufbau

```text
.
├── aufgabe1/          # Kreuzwortkreuze
├── aufgabe2/          # Flaggenmusterung
├── aufgabe5/          # Inselbegabung / PalmManager
│   ├── main.py
│   ├── insel.db
│   ├── startscreen.png
│   └── background.png
├── docs/               # Dokumentationen und Ergebnisse
└── README.md
```

Die Ordner `aufgabe1/`, `aufgabe2/` und `docs/` beschreiben die gemeinsame Zielstruktur. In der vorliegenden Arbeitskopie liegt PalmManager derzeit im Projektstamm; die Dateien der Aufgaben 1 und 2 sowie die Dokumentationen sind hier noch nicht vorhanden. Die Startbefehle für diese beiden Programme ergänzen wir, sobald ihre Skripte in das Repository integriert sind.

## Gemeinsam entwickeln

Wir halten die drei Aufgaben in getrennten Ordnern und integrieren fertige Änderungen in den gemeinsamen Hauptbranch. So kann jede Person an einem klar abgegrenzten Teil arbeiten, während dieses README den gemeinsamen Stand des Teams festhält.

## Technik

| Bereich | Technologie |
| --- | --- |
| Programmiersprache | Python 3 |
| Grafische Oberfläche von PalmManager | Pygame |
| Lokale Datenhaltung | SQLite |
| Konsolenausgaben | Colorama |

## Wettbewerbsaufgabe

Die offiziellen Aufgabenblätter und weitere Informationen gibt es auf der [BWINF-Seite zum 45. Bundeswettbewerb](https://bwinf.de/bundeswettbewerb/45/). Die Aufgabenbezeichnungen und Kurzbeschreibungen in diesem README orientieren sich am [offiziellen Aufgabenblatt der 1. Runde](https://bwinf.de/fileadmin/wettbewerbe/bundeswettbewerb/45/1_Runde/Aufgaben451.pdf).

<div align="center">

**Gemeinsam programmiert von drei BWINF-Teilnehmenden**  
*45. Bundeswettbewerb Informatik · 1. Runde*

</div>
