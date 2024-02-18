import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
marked_state_count = 0


def set_state(marked_state):
    if state in data.state.values:
        data_row = data[data.state == state]
        xcor = data_row.x.values[0]
        ycor = data_row.y.values[0]
        positions = (xcor, ycor)
        set_name(positions)
        marked_state += 1


def set_name(positions):
    timmy = Turtle()
    timmy.penup()
    timmy.goto(positions)
    timmy.hideturtle()
    timmy.write(f"{state}", align='center', font=('Arial', 10, 'normal'))


is_game_on = True
while is_game_on:
    print(marked_state_count)
    if marked_state_count <= 50:
        state = screen.textinput(title="US State Game", prompt="Enter State : ").capitalize()
        if state:
            set_state(marked_state_count)
        else:
            is_game_on = False
    else:
        is_game_on = False
turtle.mainloop()
