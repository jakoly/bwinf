import sqlite3
import time
from colorama import Fore, Style, init
import os
import pygame

#Setup
db = sqlite3.connect("insel.db")
cursor = db.cursor()
init() #for colorama
pygame.init()

#Variables
displWidth = 1280
displHeight = 720

showAllPalmen = True

font = pygame.font.SysFont("Arial", 25)
primaryColor =  (220, 229, 204)
accentColor = (139, 148, 126)
attentionColor = (255, 0, 0)
alleEingabeFelder = []
alleAnzeigeTexte = []


if not os.path.exists("background.png"):
    print(Fore.RED + "Error: background.png not found!" + Style.RESET_ALL)
    background = pygame.Surface((displWidth, displHeight))
    background.fill(primaryColor)
else:
    background = pygame.image.load("background.png")
    background = pygame.transform.scale(background, (displWidth, displHeight))

class Button:
    borderRadius = 15

    def __init__(self, rect, text):
        self.rect = rect
        self.textSurface = font.render(text, True, (255, 255, 255))
        self.textRect = self.textSurface.get_rect(center=self.rect.center)

    def draw(self):
        pygame.draw.rect(screen, accentColor, self.rect, border_radius=Button.borderRadius)
        screen.blit(self.textSurface, self.textRect)

    def isClicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(event.pos)
        return False

def togglePalmen():
    global showAllPalmen
    showAllPalmen = not showAllPalmen

home_btn = Button(pygame.Rect(300, 50, 100, 50), "Home")
add_btn = Button(pygame.Rect(500, 50, 100, 50), "Add")
show_all_btn = Button(pygame.Rect(700, 50, 100, 50), "Show All")
relationship_btn = Button(pygame.Rect(900, 50, 100, 50), "Relations")

def drawAllButtons():
    for btn in (home_btn, add_btn, show_all_btn, relationship_btn):
        btn.draw()

def getInput(bildschirm, schriftart, x, y, breite, hoehe, hinweisText):
    eingabeText = ""
    aktiv = True
    farbeRahmen = accentColor

    eingabeFeld = pygame.Rect(x, y, breite, hoehe)
    alleEingabeFelder.append(eingabeFeld)
    uhr = pygame.time.Clock()

    while aktiv:
        for ereignis in pygame.event.get():
            if ereignis.type == pygame.QUIT:
                pygame.quit()
                return ""

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

        pygame.draw.rect(bildschirm, primaryColor, eingabeFeld)
        pygame.draw.rect(bildschirm, farbeRahmen, eingabeFeld, 2)

        anzeigeText = eingabeText if eingabeText else hinweisText
        farbeText = (255, 255, 255) if eingabeText else (150, 150, 150)

        textOberflaeche = schriftart.render(anzeigeText, True, farbeText)
        bildschirm.blit(
            textOberflaeche,
            (eingabeFeld.x + 5, eingabeFeld.y + (eingabeFeld.h - textOberflaeche.get_height()) // 2)
        )

        pygame.display.flip()
        uhr.tick(30)

    return eingabeText

def deleteAllInputs():
    """
    Entfernt alle registrierten Eingabefelder aus der Verwaltung.
    """
    alleEingabeFelder.clear()
    screen.fill(primaryColor)
    screen.blit(background, (0, 0))
    drawAllButtons()
    pygame.display.flip()

def text(bildschirm, schriftart, text, x, y, farbe=(255, 255, 255)):
    """
    Zeigt Text an einer bestimmten Position an und registriert ihn zur Verwaltung.

    Parameter:
        bildschirm: die Pygame Surface, auf der gezeichnet wird
        schriftart: eine pygame.font.Font Instanz
        text: der anzuzeigende Text
        x, y: Position des Texts
        farbe: RGB Tupel für die Textfarbe

    Rückgabe:
        Ein Dictionary, das den Text repräsentiert (für spätere Verwaltung)
    """
    textOberflaeche = schriftart.render(text, True, farbe)
    textEintrag = {
        "text": text,
        "schriftart": schriftart,
        "position": (x, y),
        "farbe": farbe,
        "oberflaeche": textOberflaeche
    }
    alleAnzeigeTexte.append(textEintrag)
    bildschirm.blit(textOberflaeche, (x, y))
    #pygame.display.flip()
    return textEintrag

def deleteText():
    """
    Entfernt alle registrierten Anzeige-Texte aus der Verwaltung.
    """
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

    if not os.path.exists("startscreen.png"):
        print(Fore.RED + "Error: startscreen.png not found!" + Style.RESET_ALL)
    else:
        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()

        startscreen = pygame.image.load("startscreen.png")
        startscreen = pygame.transform.scale(startscreen, (1280, 720))

        started = False

        while not started:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    started = True

            screen.blit(startscreen, (0, 0))

            pygame.display.flip()
            clock.tick(60)

startUp()

def addPalme():
    global showAllPalmen
    showAllPalmen = False

    clear()

    geschlecht = getInput(screen, font, 280, 200, 300, 40, "Geschlecht eingeben (m/w)...")

    mutter = getInput(screen, font, 280, 300, 300, 40, "Mutter eingeben (id)...")

    vater = getInput(screen, font, 280, 400, 300, 40, "Vater eingeben (m/w)...")

    if vater==None or mutter==None:
        deleteAllInputs()
        text(screen, font, "Da ist etwas schiefgelaufen. Versuche es nochmal.", 280, 200, attentionColor)
        pygame.display.flip()
        wartezeit = time.time() + 3
        while time.time() < wartezeit:
            pygame.event.pump()
            time.sleep(0.05)
        deleteText()
        return

    variantsForMan = ["m", "M", "männlich", "Männlich", "maskulin", "Maskulin"]
    variantsForWoman = ["w", "W", "weiblich", "Weiblich", "feminin", "Feminin"]
    if geschlecht in variantsForMan: geschlecht = "männlich"
    elif geschlecht in variantsForWoman: geschlecht = "weiblich"
    else:
        deleteAllInputs()
        text(screen, font, "Bitte valides Geschlecht eingeben", 280, 200, attentionColor)
        pygame.display.flip()
        wartezeit = time.time() + 3
        while time.time() < wartezeit:
            pygame.event.pump()
            time.sleep(0.05)
        deleteText()
        return
    
    cursor.execute(
        "INSERT INTO palmen (geschlecht, mutter, vater) VALUES (?, ?, ?)",
        (geschlecht, mutter, vater)
    )
    db.commit()

    deleteText()
    deleteAllInputs()
    text(screen, font, "Palme erfolgreich hinzugefügt!", 280, 200, accentColor)
    pygame.display.flip()
    time.sleep(3)
    #showAllPalmen = True

def showPalmen():
    cursor.execute("SELECT * FROM palmen")
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
            raise ValueError("Fehler: Zyklus in den Elternbeziehungen!")

        besucht = besucht | {id_}
        palme = palmen[id_]

        eltern = [
            eltern_id
            for eltern_id in (palme["vater"], palme["mutter"])
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
        return

    # Palmen nach Generation gruppieren
    reihen = {}

    for id_, gen in generationen.items():
        reihen.setdefault(gen, []).append(id_)

    # Positionen aller Palmen berechnen
    positionen = {}
    breite = 100
    hoehe = 50
    abstand_x = 130
    abstand_y = 120
    start_x = 280
    start_y = 200

    for gen, ids in sorted(reihen.items()):
        for index, id_ in enumerate(sorted(ids)):
            x = start_x + index * abstand_x
            y = start_y + gen * abstand_y
            positionen[id_] = (x, y)

    # Verbindungslinien zuerst zeichnen
    for id_, palme in palmen.items():
        kind_x, kind_y = positionen[id_]

        for eltern_id in (palme["vater"], palme["mutter"]):
            if eltern_id in positionen:
                eltern_x, eltern_y = positionen[eltern_id]

                pygame.draw.line(
                    screen,
                    (200, 200, 200),
                    (eltern_x + breite // 2, eltern_y + hoehe),
                    (kind_x + breite // 2, kind_y),
                    2
                )

    # Palmen und ihre IDs zeichnen
    rectangles = []

    for id_, (x, y) in positionen.items():
        rect = pygame.Rect(x, y, breite, hoehe)

        pygame.draw.rect(screen, accentColor, rect)
        pygame.draw.rect(screen, (255, 255, 255), rect, 1)

        text = font.render(str(id_), True, (255, 255, 255))
        screen.blit(text, text.get_rect(center=rect.center))

        rectangles.append(rect)

    pygame.display.flip()
    return rectangles


def verwandschaft():
    print("Verwandschaft")

    userInput = getInput(screen, font, 280, 200, 300, 40, "Eingeben (bspw. Vater->ID) ...").lower()

    userInputTable = userInput.split("->")

    currentPalme = userInputTable[-1]

    userInputTable.reverse()
    del userInputTable[0]

    print(userInputTable)

    for element in userInputTable:
        if element=="vater":
            cursor.execute(
                "SELECT vater FROM palmen WHERE id=?",
                (currentPalme,)
            )
            optionen = cursor.fetchone()
            currentPalme = optionen[0]
        elif element=="mutter":
            cursor.execute(
                "SELECT mutter FROM palmen WHERE id=?",
                (currentPalme,)
            )
            optionen = cursor.fetchone()
            currentPalme = optionen[0]
        elif "großmutter" in element and not "ur" in element:
            for i in range(2):
                cursor.execute(
                    "SELECT mutter FROM palmen WHERE id=?",
                    (currentPalme,)
                )
                optionen = cursor.fetchone()
                currentPalme = optionen[0]
        elif "großvater" in element and not "ur" in element:
            for i in range(2):
                cursor.execute(
                    "SELECT vater FROM palmen WHERE id=?",
                    (currentPalme,)
                )
                optionen = cursor.fetchone()
                currentPalme = optionen[0]
        elif "ur" in element and "großmutter" in element:
            count = element.count("ur")
            for i in range(count):
                cursor.execute(
                    "SELECT mutter FROM palmen WHERE id=?",
                    (currentPalme,)
                )
                optionen = cursor.fetchone()
                currentPalme = optionen[0]
        elif "ur" in element and "großvater" in element:
            count = element.count("ur")
            for i in range(count):
                cursor.execute(
                    "SELECT vater FROM palmen WHERE id=?",
                    (currentPalme,)
                )
                optionen = cursor.fetchone()
                currentPalme = optionen[0]
                
        print("ID: " + str(currentPalme))


    input()


def home():
    print("Home")
    deleteText()
    deleteAllInputs()

screen = pygame.display.set_mode((displWidth, displHeight))
screen.fill(primaryColor)
pygame.display.set_caption("PalmManager")

clock = pygame.time.Clock()

running = True
pygame.event.clear()

buttonActions = {
    home_btn: home,
    add_btn: addPalme,
    show_all_btn: togglePalmen,
    relationship_btn: verwandschaft,
}

while running:
    mouse_pos = pygame.mouse.get_pos()

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        for btn, action in buttonActions.items():
            if btn.isClicked(event):
                action()

    # Bildschirm löschen
    screen.fill(primaryColor)

    # Hier wird gezeichnet
    screen.blit(background, (0, 0))
    welcomeText = font.render(
        "Welcome farmer!", True, accentColor
    )
    screen.blit(welcomeText, (280, 150))
    drawAllButtons()

    if showAllPalmen:
        showPalmen()
    

    pygame.display.flip()
    clock.tick(30)



db.close()
pygame.quit()