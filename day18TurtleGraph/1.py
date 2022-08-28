import random
from turtle import Screen, Turtle
tim=Turtle()
screen=Screen()
tim.shape("turtle")
tim.color("medium purple")
tim.speed(4)

for _ in range(4):
    tim.forward(100)
    tim.right(90)
tim.left(90)
tim.forward(10)
tim.right(90)
for _ in range(20):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
screen.exitonclick()