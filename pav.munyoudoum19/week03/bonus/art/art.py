import turtle
import random

sides = int(input("Enter a number to see art: "))
turtle.tracer(0, 0)
wn = turtle.Screen()
wn.colormode(255)
turtle.speed(0)

def shape(size, sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(90)


for i in range(100):
    shape(5*i, sides)
    turtle.left(i)
wn.exitonclick()
