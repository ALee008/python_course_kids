import turtle

zeichnen = turtle.Turtle()
zeichnen.forward(100)
x, y = zeichnen.position()
print(x, y)
zeichnen.goto(0.5 * x, y)
zeichnen.left(90)
zeichnen.forward(300)
zeichnen.right(90)
zeichnen.forward(200)
zeichnen.right(90)
zeichnen.forward(100)
zeichnen.right(90)
zeichnen.circle(20)
x, y = zeichnen.position()
zeichnen.up()
zeichnen.goto(x, y - 40)
zeichnen.down()
zeichnen.left(90)
zeichnen.forward(30)
x, y = zeichnen.position()
zeichnen.right(45)
zeichnen.forward(20)
zeichnen.goto(x, y)
zeichnen.left(90)
zeichnen.forward(20)
zeichnen.goto(x, y)
zeichnen.right(45)
zeichnen.forward(30)
x, y = zeichnen.position()
zeichnen.right(45)
zeichnen.forward(30)
zeichnen.goto(x, y)
zeichnen.left(90)
zeichnen.forward(30)
