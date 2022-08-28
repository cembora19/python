import random
import turtle as t

tim=t.Turtle()
screen=t.Screen()
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color

angle=0
tim.speed("fastest")
while angle!=360:
    tim.color(random_color())
    tim.circle(100)
    tim.left(5)
    angle+=5

screen.exitonclick()