import sqlite3
import time
from colorama import Fore, Style, init
import os
import pygame

# Setup
db = sqlite3.connect("insel.db")
cursor = db.cursor()
init()
pygame.init()

# Variables
displWidth = 1280
displHeight = 720

showVerwandtschaft = False
beziehungsAnzeige = None
beziehungsFehler = None
beziehungsFehlerZeit = 0

showAllPalmen = True
running = True

font = pygame.font.SysFont("Arial", 25)
primaryColor = (220, 229, 204)
accentColor = (139, 148, 126)
attentionColor = (255, 0, 0)

alleEingabeFelder = []
alleAnzeigeTexte = []

# Background laden
if not os.path.exists("background.png"):
    print(Fore.RED + "Error: background.png not found!" + Style.RESET_ALL)
    background = pygame.Surface((displWidth, displHeight))
    background.fill(primaryColor)
else:
    background = pygame.image.load("background.png")
    background = pygame.transform.scale(
        background, (displWidth, displHeight)
    )


class Button:
    borderRadius = 15

    def __init__(self, rect, text):
        self.rect = rect
        self.textSurface = font.render(
            text, True, (255, 255, 255)
        )
        self.textRect = self.textSurface.get_rect(
            center=self.rect.center
        )

    def draw(self):
        pygame.draw.rect(
            screen,
            accentColor,
            self.rect,
            border_radius=Button.borderRadius
        )
        screen.blit(self.textSurface, self.textRect)

    def isClicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(event.pos)

        return False


def togglePalmen():
    global showAllPalmen
    showAllPalmen = not showAllPalmen


add_btn = Button(pygame.Rect(500, 50, 150, 50), "Hinzufügen")
show_all_btn = Button(pygame.Rect(700, 50, 150, 50), "Alle anzeigen")
relationship_btn = Button(
    pygame.Rect(900, 50, 150, 50), "Beziehungen"
)


def drawAllButtons():
    for btn in (
        add_btn,
        show_all_btn,
        relationship_btn
    ):
        btn.draw()


def drawMainScreen():
    screen.fill(primaryColor)
    screen.blit(background, (0, 0))
    drawAllButtons()


def showAddMessage(message, color):
    alleEingabeFelder.clear()
    alleAnzeigeTexte.clear()

    drawMainScreen()

    text(screen, font, message, 280, 200, color)
    pygame.display.flip()


def getInput(
    bildschirm,
    schriftart,
    x,
    y,
    breite,
    hoehe,
    hinweisText
):
    global running

    eingabeText = ""
    aktiv = True
    farbeRahmen = accentColor

    eingabeFeld = pygame.Rect(
        x, y, breite, hoehe
    )

    alleEingabeFelder.append(eingabeFeld)

    uhr = pygame.time.Clock()

    while aktiv:

        for ereignis in pygame.event.get():

            if ereignis.type == pygame.QUIT:
                running = False
                return None

            if ereignis.type == pygame.KEYDOWN:

                if ereignis.key == pygame.K_RETURN:
                    aktiv = False

                elif ereignis.key == pygame.K_ESCAPE:
                    eingabeText = ""
                    aktiv = False

                elif ereignis.key == pygame.K_BACKSPACE:
                    eingabeText = eingabeText[:-1]

                else:
                    eingabeText += ereignis.unicode

        pygame.draw.rect(
            bildschirm, primaryColor, eingabeFeld
        )

        pygame.draw.rect(
            bildschirm, farbeRahmen, eingabeFeld, 2
        )

        anzeigeText = (
            eingabeText if eingabeText else hinweisText
        )

        farbeText = (
            (255, 255, 255)
            if eingabeText
            else (150, 150, 150)
        )

        textOberflaeche = schriftart.render(
            anzeigeText, True, farbeText
        )

        bildschirm.blit(
            textOberflaeche,
            (
                eingabeFeld.x + 5,
                eingabeFeld.y
                + (
                    eingabeFeld.h
                    - textOberflaeche.get_height()
                ) // 2
            )
        )

        pygame.display.flip()
        uhr.tick(30)

    return eingabeText


def deleteAllInputs():
    alleEingabeFelder.clear()

    screen.fill(primaryColor)
    screen.blit(background, (0, 0))

    drawAllButtons()
    pygame.display.flip()


def text(
    bildschirm,
    schriftart,
    textInhalt,
    x,
    y,
    farbe=(255, 255, 255)
):
    textOberflaeche = schriftart.render(
        textInhalt, True, farbe
    )

    textEintrag = {
        "text": textInhalt,
        "schriftart": schriftart,
        "position": (x, y),
        "farbe": farbe,
        "oberflaeche": textOberflaeche
    }

    alleAnzeigeTexte.append(textEintrag)

    bildschirm.blit(textOberflaeche, (x, y))

    return textEintrag


def deleteText():
    alleAnzeigeTexte.clear()

    screen.fill(primaryColor)
    screen.blit(background, (0, 0))

    drawAllButtons()
    pygame.display.flip()


def clear():
    os.system("cls")


def hidePalmen():
    screen.fill(primaryColor)
    pygame.display.flip()


def startUp():
    global showAllPalmen

    showAllPalmen = False

    cursor.execute("SELECT COUNT(*) FROM palmen")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute(
            """
            INSERT INTO palmen (geschlecht, mutter, vater)
            VALUES ('m', 0, 0)
            """
        )

        cursor.execute(
            """
            INSERT INTO palmen (geschlecht, mutter, vater)
            VALUES ('w', 0, 0)
            """
        )

        db.commit()

    if not os.path.exists("startscreen.png"):
        print(
            Fore.RED
            + "Error: startscreen.png not found!"
            + Style.RESET_ALL
        )
        return True

    clock = pygame.time.Clock()

    startscreen = pygame.image.load("startscreen.png")

    startscreen = pygame.transform.scale(
        startscreen, (displWidth, displHeight)
    )

    started = False

    while not started:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
            ):
                started = True

        screen.blit(startscreen, (0, 0))

        
        pygame.display.flip()
        clock.tick(60)

    return True


def addPalme():
    global showAllPalmen

    showAllPalmen = False

    # Palmen und Verbindungslinien ausblenden
    alleEingabeFelder.clear()
    alleAnzeigeTexte.clear()

    drawMainScreen()
    pygame.display.flip()

    clear()

    geschlecht = getInput(
        screen,
        font,
        280,
        200,
        300,
        40,
        "Geschlecht eingeben (m/w)..."
    )

    if geschlecht is None:
        return

    mutter = getInput(
        screen,
        font,
        280,
        300,
        300,
        40,
        "Mutter eingeben (id)..."
    )

    if mutter is None:
        return

    vater = getInput(
        screen,
        font,
        280,
        400,
        300,
        40,
        "Vater eingeben (id)..."
    )

    if vater is None:
        return

    if not geschlecht or not mutter or not vater:
        showAddMessage(
            "Eingabe abgebrochen oder unvollständig.",
            attentionColor
        )
        return

    variantsForMan = [
        "m", "M", "männlich",
        "Männlich", "maskulin", "Maskulin"
    ]

    variantsForWoman = [
        "w", "W", "weiblich",
        "Weiblich", "feminin", "Feminin"
    ]

    if geschlecht in variantsForMan:
        geschlecht = "männlich"

    elif geschlecht in variantsForWoman:
        geschlecht = "weiblich"

    else:
        showAddMessage(
            "Bitte valides Geschlecht eingeben",
            attentionColor
        )
        return

    cursor.execute(
        """
        INSERT INTO palmen (geschlecht, mutter, vater)
        VALUES (?, ?, ?)
        """,
        (geschlecht, mutter, vater)
    )

    db.commit()

    showAddMessage(
        "Palme erfolgreich hinzugefügt!",
        accentColor
    )


def addPalmeWithDelay():
    global showAllPalmen

    addPalme()

    if running:
        pygame.time.wait(3000)
        showAllPalmen = True


def showPalmen():

    cursor.execute(
        "SELECT id, geschlecht, vater, mutter FROM palmen"
    )

    daten = cursor.fetchall()

    # Alle Palmen nach ID speichern
    palmen = {
        zeile[0]: {
            "geschlecht": zeile[1],
            "vater": zeile[2],
            "mutter": zeile[3]
        }
        for zeile in daten
    }

    generationen = {}

    # Generation jeder Palme berechnen
    def generation(id_, besucht=None):

        if id_ in generationen:
            return generationen[id_]

        if besucht is None:
            besucht = set()

        if id_ in besucht:
            raise ValueError(
                "Fehler: Zyklus in den Elternbeziehungen!"
            )

        besucht = besucht | {id_}

        palme = palmen[id_]

        eltern = [
            eltern_id
            for eltern_id in (
                palme["vater"],
                palme["mutter"]
            )
            if eltern_id in palmen
        ]

        if not eltern:
            gen = 0

        else:
            gen = 1 + max(
                generation(eltern_id, besucht)
                for eltern_id in eltern
            )

        generationen[id_] = gen

        return gen

    try:

        for id_ in palmen:
            generation(id_)

    except ValueError as fehler:

        print(fehler)
        return []

    # Palmen nach Generation gruppieren
    reihen = {}

    for id_, gen in generationen.items():
        reihen.setdefault(gen, []).append(id_)

    # Positionen aller Palmen berechnen
    positionen = {}

    breite = 100
    hoehe = 50

    abstand_x = 130
    abstand_y = 100

    start_x = 80
    start_y = 200

    max_spalten = 9

    aktuelle_y = start_y

    for gen, ids in sorted(reihen.items()):

        ids = sorted(ids)

        for index, id_ in enumerate(ids):

            spalte = index % max_spalten
            zeile = index // max_spalten

            x = start_x + spalte * abstand_x
            y = aktuelle_y + zeile * abstand_y

            positionen[id_] = (x, y)

        # Höhe der aktuellen Generation bestimmen
        anzahl_zeilen = (
            len(ids) + max_spalten - 1
        ) // max_spalten

        aktuelle_y += (
            anzahl_zeilen * abstand_y + 50
        )

    # Verbindungslinien zuerst zeichnen
    for id_, palme in palmen.items():

        kind_x, kind_y = positionen[id_]

        for eltern_id in (
            palme["vater"],
            palme["mutter"]
        ):

            if eltern_id in positionen:

                eltern_x, eltern_y = positionen[eltern_id]

                pygame.draw.line(
                    screen,
                    (200, 200, 200),
                    (
                        eltern_x + breite // 2,
                        eltern_y + hoehe
                    ),
                    (
                        kind_x + breite // 2,
                        kind_y
                    ),
                    2
                )

    # Palmen und ihre IDs zeichnen
    rectangles = []

    for id_, (x, y) in positionen.items():

        rect = pygame.Rect(
            x, y, breite, hoehe
        )

        geschlecht = palmen[id_]["geschlecht"]

        if geschlecht == "männlich":

            palmenFarbe = (135, 206, 250)

        elif geschlecht == "weiblich":

            palmenFarbe = (255, 182, 193)

        else:

            palmenFarbe = accentColor

        pygame.draw.rect(
            screen,
            palmenFarbe,
            rect
        )

        pygame.draw.rect(
            screen,
            (255, 255, 255),
            rect,
            1
        )

        id_surface = font.render(
            str(id_),
            True,
            (255, 255, 255)
        )

        screen.blit(
            id_surface,
            id_surface.get_rect(center=rect.center)
        )

        rectangles.append(rect)

    # Wichtig: erst NACH der Schleife zurückgeben!
    return rectangles


def verwandschaft():

    global showAllPalmen
    global showVerwandtschaft
    global beziehungsAnzeige, beziehungsFehler, beziehungsFehlerZeit

    showAllPalmen = False
    showVerwandtschaft = True

    beziehungsAnzeige = None
    beziehungsFehler = None

    # Hilfsfunktion zum Abrufen eines Verwandten
    def getVerwandter(currentPalme, verwandtschaft):

        cursor.execute(
            f"SELECT {verwandtschaft} FROM palmen WHERE id=?",
            (currentPalme,)
        )

        optionen = cursor.fetchone()

        if optionen is None or optionen[0] is None:
            return None

        return optionen[0]

    alleEingabeFelder.clear()
    alleAnzeigeTexte.clear()

    # Eingabemaske anzeigen
    drawMainScreen()
    titel = font.render("Beziehungen", True, accentColor)
    screen.blit(titel, (280, 150))
    pygame.display.flip()

    userInput = getInput(
        screen,
        font,
        280,
        200,
        300,
        40,
        "Eingeben (bspw. Vater->ID) ..."
    )

    if userInput is None or not userInput.strip():
        return

    userInput = userInput.lower().strip()
    userInputTable = [
        element.strip()
        for element in userInput.split("->")
    ]

    # Die letzte Eingabe ist die ID der Ausgangspalme.
    currentPalme = userInputTable.pop()

    # Prüfen, ob die Ausgangspalme überhaupt existiert.
    cursor.execute(
        "SELECT id FROM palmen WHERE id=?",
        (currentPalme,)
    )

    if cursor.fetchone() is None:
        beziehungsFehler = "Palme mit dieser ID nicht gefunden!"
        beziehungsFehlerZeit = pygame.time.get_ticks()
        return

    userInputTable.reverse()

    for element in userInputTable:

        if element == "vater":
            currentPalme = getVerwandter(currentPalme, "vater")

        elif element == "mutter":
            currentPalme = getVerwandter(currentPalme, "mutter")

        elif "großmutter" in element:
            for _ in range(2 + element.count("ur")):
                currentPalme = getVerwandter(currentPalme, "mutter")

                if currentPalme is None:
                    break

        elif "großvater" in element:
            for _ in range(2 + element.count("ur")):
                currentPalme = getVerwandter(currentPalme, "vater")

                if currentPalme is None:
                    break

        else:
            beziehungsFehler = "Unbekannte Verwandtschaft!"
            break

        if currentPalme is None:
            beziehungsFehler = "Verwandter nicht gefunden!"
            break

    if beziehungsFehler is not None:
        beziehungsAnzeige = None
        beziehungsFehlerZeit = pygame.time.get_ticks()
    else:
        beziehungsAnzeige = "ID: " + str(currentPalme)


def home():
    print("Home button clicked")


# Pygame-Fenster initialisieren
screen = pygame.display.set_mode(
    (displWidth, displHeight)
)

screen.fill(primaryColor)

pygame.display.set_caption("PalmManager")

clock = pygame.time.Clock()

buttonActions = {
    add_btn: addPalmeWithDelay,
    show_all_btn: togglePalmen,
    relationship_btn: verwandschaft
}


# Startbildschirm anzeigen
if not startUp():
    running = False

pygame.event.clear()


# Hauptschleife
while running:

    # Events verarbeiten
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            break

        for btn, action in buttonActions.items():

            if btn.isClicked(event):

                # Jeder andere Button beendet die Verwandtschaftsansicht.
                if btn != relationship_btn:
                    showVerwandtschaft = False
                    beziehungsAnzeige = None
                    beziehungsFehler = None
                    beziehungsFehlerZeit = 0

                action()
                break

    if not running:
        break

    # Verwandtschaftsansicht: Nur Hintergrund, Buttons und Ergebnis anzeigen.
    if showVerwandtschaft:

        drawMainScreen()

        titel = font.render("Beziehungen", True, accentColor)
        screen.blit(titel, (280, 150))

        if beziehungsAnzeige is not None:
            ergebnis = font.render(
                beziehungsAnzeige,
                True,
                accentColor
            )
            screen.blit(ergebnis, (350, 200))

        if beziehungsFehler is not None:

            if pygame.time.get_ticks() - beziehungsFehlerZeit < 3000:
                fehler = font.render(
                    beziehungsFehler,
                    True,
                    attentionColor
                )
                screen.blit(fehler, (350, 200))
            else:
                beziehungsFehler = None

    # Normale Ansicht
    else:

        drawMainScreen()

        if showAllPalmen:
            showPalmen()

    pygame.display.flip()
    clock.tick(30)


# Programm beenden
db.close()
pygame.quit()
