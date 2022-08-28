import random
from turtle import *#screen turtle
import turtle as t
tim=Turtle()
screen=Screen()
tim.shape("turtle")
# tim.color("medium purple")
tim.speed(8)
tim.pensize(15)
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
    
angle=[0,90,180,270]

def random_walk(walk_time): 
    for i in range(walk_time):
        tim.color(random_color())
        tim.forward(40)
        tim.right(random.choice(angle))

random_walk(200)
screen.exitonclick()