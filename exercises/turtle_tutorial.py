"""Turtle Drawing Game."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
bob: Turtle = Turtle()

bob.penup()
bob.goto(-150, -100)
bob.pendown()
bob.speed(100)
colormode(23)

leo.penup()
leo.goto(-150, -100)
leo.pendown()
leo.pencolor("maroon")
leo.fillcolor("pink")
leo.speed(50)
leo.hideturtle()

leo.begin_fill()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1

leo.end_fill()

side_length: float = 300

while (i < 50):
    bob.forward(side_length)
    bob.left(124)
    side_length = side_length * 1.04
    i += 1


done()