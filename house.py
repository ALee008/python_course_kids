import turtle


def gehe_zum_startpunkt(x, y):
    """Hebe den Stift und gehe zum definierten Startpunkt.

    :param x: x-Koordinate vom Startpunkt
    :param y: y-Koordinate vom Startpunkt
    """
    stift.up()
    stift.goto(x, y)
    stift.down()

    return None


def male_quadrat(laenge: float, farbe: str ="white"):
    """Zeichne ein Quadrat mit den Seitenlaengen `laenge`.

    :param laenge: die Seitenlaenge des Quadrates
    :param farbe: die Farbe des Quadrates
    """
    stift.fillcolor(farbe)
    stift.begin_fill()
    for _ in range(4):
        stift.forward(laenge)
        stift.left(90)
    stift.end_fill()
    return None


def male_rechteck(breite: float, hoehe: float, farbe: str = "white"):
    """Zeichne ein Rechteck mit den Seitenlaengen `breite` und `hoehe`.

    :param breite: die Breite des Rechtecks
    :param hoehe: die Hoehe des Rechtecks
    :param farbe: Farbe des Rechtecks
    """
    stift.fillcolor(farbe)
    stift.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            stift.forward(breite)
            stift.left(90)
        else:
            stift.forward(hoehe)
            stift.left(90)
    stift.end_fill()
    return None


def male_tuer(breite: float, hoehe: float, farbe: str = "white"):
    """Male die Tuer. Es wird angenommen, dass der Startpunkt die untere linke Ecke des Hauses ist.

    :param breite: die Breite der Tuer
    :param hoehe: die Hoehe der Tuer
    :param farbe: die gewuenschte Farbe fuer die Tuer
    """
    stift.setheading(0.0)
    stift.forward(50)
    male_rechteck(breite, hoehe, farbe)

    return None


def male_dach(dach_hoehe: float, farbe: str ="white"):
    """Male das Dach, abhaengig von der Breite und Hoehe des Hauses.

    :param dach_hoehe: die gewuenschte Dachhoehe
    :param farbe: gewuenschte Farbe fuer das Dach
    """
    mitte_des_daches = START_PUNKT_X + HAUS_BREITE / 2, HAUS_HOEHE + dach_hoehe
    stift.up()
    stift.goto(START_PUNKT_X, START_PUNKT_Y + HAUS_HOEHE)
    stift.down()
    stift.fillcolor(farbe)
    stift.begin_fill()
    stift.goto(mitte_des_daches)
    stift.goto(START_PUNKT_X + HAUS_BREITE, START_PUNKT_Y + HAUS_HOEHE)
    stift.end_fill()

    return None


def male_fenster(laenge: float, farbe: str ="white"):
    """Male zwei Fenster ins Haus. Beide haben die selbe Groesse.

    :param laenge: Fenstergroesse
    :param farbe: die gewuenschte Fensterfarbe
    """
    stift.up()
    linkes_fenster_x, linkes_fenster_y = START_PUNKT_X + 0.1 * HAUS_BREITE, START_PUNKT_Y + 0.75 * HAUS_HOEHE
    stift.goto(linkes_fenster_x, linkes_fenster_y)
    stift.down()
    male_quadrat(laenge, farbe)
    stift.up()
    rechtes_fenster_x, rechtes_fenster_y = START_PUNKT_X + HAUS_BREITE - 2 * laenge, linkes_fenster_y
    stift.goto(rechtes_fenster_x, rechtes_fenster_y)
    stift.down()
    male_quadrat(laenge, farbe)

    return None


if __name__ == '__main__':
    stift = turtle.Turtle("turtle")
    stift.getscreen()
    # hier koennt ihr die Geschwindigkeit der Schildkroete einstellen:
    # "slowest", "slow", "normal", "fast", "fastest"
    stift.speed("fast")
    # hier koennt ihr den Startpunkt des Hauses einstellen.
    # Beachtet: nicht zu hoch oder zu tief einstellen, sonst kann es zu komischen Effekten kommen.
    START_PUNKT_X, START_PUNKT_Y = -200, -200
    # hier koennt ihr die Hausbreite einstellen
    HAUS_BREITE, HAUS_HOEHE = 400, 350
    gehe_zum_startpunkt(START_PUNKT_X, START_PUNKT_Y)
    # ab hier faengt die Zeichnung an
    male_rechteck(HAUS_BREITE, HAUS_HOEHE)
    # Hier koennt ihr die Farbe der Tuer aendern indem ihr statt "brown" z.B. "blue" eintragt
    male_tuer(0.25 * HAUS_BREITE, 0.6 * HAUS_HOEHE, "brown")
    # Hier laesst sich die Hoehe und die Farbe des Daches aendern
    male_dach(dach_hoehe=20, farbe="red")
    # Hier laesst sich die Groesse und Farbe des Fensters aendern.
    male_fenster(40, "yellow")

