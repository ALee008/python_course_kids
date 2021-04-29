"""
In diesem Programm sollt ihr turtle benutzen um geometrische Figuren zu malen, also Dreiecke, Quadrate, Rechtecke
und so weiter. Diesmal sollt ihr jedoch Funktionen benutzen wie wir sie in der letzen Stunde eingeführt haben.
Ich gebe euch den Namen der Funktionen mit Parameter vor und schreibe hinzu was die Funktion noch können muss.
Die Funktion um ein Dreieck zu malen habe ich vorgegeben.
"""
import turtle
import math

stift = turtle.Turtle("turtle")


def male_rechtwinkliges_dreieck(grund_laenge, hoehe, farbe="yellow"):
    """Male ein rechtwinkliges Dreick mit der Grundlänge 'grund_laenge', Höhe 'hoehe' und Farbe 'farbe'.
    Wenn keine Farbe angegeben wird, dann ist das Dreick am Anfang gelb.
    """
    stift.fillcolor(farbe)
    stift.begin_fill()
    stift.forward(grund_laenge)
    stift.left(90)
    stift.forward(hoehe)
    stift.left(180)
    # ihr müsst nicht verstehen was in den nächsten zwei Zeilen passiert
    stift.right(math.atan(grund_laenge / hoehe) * 180 / math.pi)
    stift.forward(math.sqrt(grund_laenge ** 2 + hoehe ** 2))
    stift.end_fill()


def male_quadrat(seiten_laenge, farbe):
    """Male ein Quadrat mit der Seitenlänge 'seiten_laenge' und Farbe 'farbe'."""


def male_kreis(radius, farbe):
    """"""


def male_halb_kreis(radius, farbe):
    """Male ein Halbkreis mit Radius 'radius' und Farbe 'farbe'."""


def male_rechteck(breite, hoehe, farbe):
    """Male ein Rechteck mit der Breite 'breite', Höhe und Farbe 'farbe'."""


# Ab hier könnt ihr eure Figuren malen. Hier ein Beispiel. Ihr könnt es aber ändern!
male_rechtwinkliges_dreieck(100, 60)
stift.up()
stift.goto(0, 150)
stift.down()
male_rechtwinkliges_dreieck(80, 40, "green")
male_halb_kreis(40, "red")

