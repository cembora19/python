import random
from turtle import *#screen turtle
tim=Turtle()
screen=Screen()
tim.shape("turtle")
tim.color("medium purple")
tim.speed(7)
colours=["medium slate blue", "dark turquoise", "red", "blue", "green", "black", "yellow", "pink"]
angle=360
polygon=3
exterior_angle=0
while exterior_angle!=36:
    tim.color(random.choice(colours))
    exterior_angle=angle/polygon
    for i in range(polygon):
        tim.forward(100)
        tim.right(exterior_angle)
    polygon+=1
    
screen.exitonclick()