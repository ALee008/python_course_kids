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


def male_quadrat(laenge: float):
    """Zeichne ein Quadrat mit den Seitenlaengen `laenge`.

    :param laenge: die Seitenlaenge des Quadrates
    """
    for _ in range(4):
        stift.forward(laenge)
        stift.left(90)

    return None


def male_rechteck(breite: float, hoehe: float):
    """Zeichne ein Rechteck mit den Seitenlaengen `breite` und `hoehe`.

    :param breite: die Breite des Rechtecks
    :param hoehe: die Hoehe des Rechtecks
    """
    for i in range(4):
        if i % 2 == 0:
            stift.forward(breite)
            stift.left(90)
        else:
            stift.forward(hoehe)
            stift.left(90)

    return None


def male_tuer(breite: float, hoehe: float):
    """Male die Tuer. Es wird angenommen, dass der Startpunkt die untere linke Ecke des Hauses ist.

    :param breite: die Breite der Tuer
    :param hoehe: die Hoehe der Tuer
    """
    stift.setheading(0.0)
    stift.forward(50)
    male_rechteck(breite, hoehe)

    return None


def male_dach(dach_hoehe: float):
    """Male das Dach, abhaengig von der Breite und Hoehe des Hauses.

    :param haus_breite: die y-Koordinate der Startposition des Hauses
    :param haus_hoehe: die x-Koordinate der Startposition des Hauses
    :param dach_hoehe: die gewuenschte Dachhoehe
    """
    mitte_des_daches = START_PUNKT_X + HAUS_BREITE / 2, -START_PUNKT_Y + dach_hoehe
    stift.up()
    stift.goto(START_PUNKT_X, START_PUNKT_Y + HAUS_HOEHE)
    stift.down()
    stift.goto(mitte_des_daches)
    stift.goto(START_PUNKT_X + HAUS_BREITE, START_PUNKT_Y + HAUS_HOEHE)

    return None


def male_fenster(laenge: float):
    """Male zwei Fenster ins Haus. Beide haben die selbe Groesse.

    :param laenge: Fenstergroesse
    """
    stift.up()
    linkes_fenster_x, linkes_fenster_y = START_PUNKT_X + 0.1 * HAUS_BREITE, START_PUNKT_Y + 0.75 * HAUS_HOEHE
    stift.goto(linkes_fenster_x, linkes_fenster_y)
    stift.down()
    male_quadrat(laenge)
    stift.up()
    rechtes_fenster_x, rechtes_fenster_y = -linkes_fenster_x - 0.1 * HAUS_BREITE, linkes_fenster_y
    stift.goto(rechtes_fenster_x, rechtes_fenster_y)
    stift.down()
    male_quadrat(laenge)

    return None


if __name__ == '__main__':
    stift = turtle.Turtle("turtle")
    stift.getscreen()
    stift.speed("slow")
    START_PUNKT_X, START_PUNKT_Y = -200, -200
    HAUS_BREITE, HAUS_HOEHE = 400, 350
    gehe_zum_startpunkt(START_PUNKT_X, START_PUNKT_Y)
    # ab hier faengt die Zeichnung an
    male_rechteck(HAUS_BREITE, HAUS_HOEHE)
    male_tuer(100, 200)
    male_dach(dach_hoehe=80)
    male_fenster(40)
    print()
