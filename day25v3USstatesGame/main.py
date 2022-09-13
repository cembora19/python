from pprint import pp
import pandas
import turtle
PATH="day25v3USstatesGame\\50_states.csv"

screen=turtle.Screen()
screen.title("U.S. States Games")
image="day25v3USstatesGame\\blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data=pandas.read_csv(PATH)
all_states=data.state.to_list()

guessed_states=[]
game_is_on=True

while len(guessed_states)<50:
    answer_state=turtle.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)