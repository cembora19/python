import random
from turtle import *#screen turtle
tim=Turtle()
screen=Screen()
tim.shape("turtle")
tim.color("medium purple")
tim.speed(4)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw_shape(num_sides):
    angle=360/num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)
screen.exitonclick()