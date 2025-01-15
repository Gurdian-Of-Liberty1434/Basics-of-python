#Write a program to draw a square inside a square?

import turtle

turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(300, 400)

spir=turtle.Turtle()

size=0

while True:
    for i in range(4):
        spir.forward(size+1)
        spir.right(90)
        size=size-5

    size=size+1

turtle.done()