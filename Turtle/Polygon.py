#Write a program to set screen size, colour for turtle graphics and draw a polygon using turtle?

import turtle

turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,400)

poly=turtle.Turtle()


num_sides=6
sidelength=70
p=360/num_sides

for i in range(num_sides):
    poly.forward(sidelength)
    poly.right(p)

turtle.done()