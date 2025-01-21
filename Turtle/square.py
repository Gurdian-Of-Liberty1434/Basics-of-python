import turtle

turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,400)

poly=turtle.Turtle()


for i in range(0,4):
    poly.forward(100)
    poly.right(90)

turtle.done()