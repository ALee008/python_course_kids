"""In diesem Schachbrett-Programm werdet ihr folgendes lernen:

* Hilfsmittel einbinden um in Python zeichnen zu können
* Variablen optimal nutzen um Wiederholungen zu sparen
* Funktionen benutzen um Aufgaben zu trennen
"""
import turtle

# global constants
SCREEN_SIZE = 600
SQUARE_SIZE = 50
BOARD_SIZE = 8
ROTATION = 90
SPEED = "fastest"  # https://docs.python.org/3.7/library/turtle.html?highlight=speed#turtle.speed
COL1, COL2 = 'black', 'white'
# dynamic starting point
STARTING_POINT_X = -BOARD_SIZE * SQUARE_SIZE // 2
# create screen object
sc = turtle.Screen()

# create turtle object
pen = turtle.Turtle('turtle')


# method to draw square
def draw():
    for _ in range(4):
        pen.forward(SQUARE_SIZE)
        pen.left(ROTATION)
    pen.forward(SQUARE_SIZE)


if __name__ == "__main__":
    # set screen
    sc.setup(SCREEN_SIZE, SCREEN_SIZE)
    # set turtle object speed
    pen.speed(SPEED)
    # loops for board
    for i in range(BOARD_SIZE):
        # not ready to draw
        pen.up()
        x, y = STARTING_POINT_X, STARTING_POINT_X + SQUARE_SIZE * i
        pen.setpos(x, y)
        # ready to draw
        pen.down()
        # row
        for j in range(BOARD_SIZE):
            # conditions for alternative color
            if (i + j) % 2 == 0:
                col = COL1
            else:
                col = COL2
            # fill with given color
            pen.fillcolor(col)
            # start filling with colour
            pen.begin_fill()
            # call method
            draw()
            # stop filling
            pen.end_fill()
    # hide the turtle
    pen.hideturtle()

# This code is contributed by Deepanshu Rustagi.
