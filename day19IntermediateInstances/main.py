from turtle import Turtle, Screen
tim=Turtle()
screen=Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def move_left():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)
def move_right():
     new_heading=tim.heading()-10
     tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=clear, key="c")
screen.exitonclick()