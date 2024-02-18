import sys
import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
marked_state = []


def set_state():
    if state not in marked_state:
        data_row = data[data.state == state]
        xcor = data_row.x.values[0]
        ycor = data_row.y.values[0]
        positions = (xcor, ycor)
        set_name(positions)
        marked_state.append(state)


def set_name(positions):
    timmy = Turtle()
    timmy.penup()
    timmy.goto(positions)
    timmy.hideturtle()
    timmy.write(f"{state}", align='center', font=('Arial', 10, 'normal'))


def write_data():
    missing_states = []
    for states in data.state.tolist():
        if states not in marked_state:
            missing_states.append(states)
    missing_data = pandas.DataFrame(missing_states)
    missing_data.to_csv()


is_game_on = True

while is_game_on:
    print(marked_state)
    if len(marked_state) <= 50:
        state = screen.textinput(title=f"{len(marked_state)}/50 State Correct", prompt="Enter State : ").title()
        if state in data.state.values:
            set_state()
        elif state == 'Exit':
            write_data()
            sys.exit()
    else:
        is_game_on = False
turtle.mainloop()
