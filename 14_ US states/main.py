import turtle
import pandas as pd

screen = turtle.Screen()
letters = turtle.Turtle()
letters.hideturtle()
letters.penup()
screen.title("Us State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load the data
data = pd.read_csv("50_states.csv")
guessed_state = []
states_to_learn = []

while len(guessed_state) <= 50:
    answer = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="Guess the state's name:").title()
    if answer == "Exit":
        break

    if answer in data.state.values and answer not in guessed_state:
        guessed_state.append(answer)
        state_names = data[data.state == answer]
        letters.goto(int(state_names.x), int(state_names.y))
        letters.write(answer)

for states_left in data.state.values:
    if states_left not in guessed_state:
        states_to_learn.append(states_left)
        state_data = data[data.state == states_left]
        letters.goto(int(state_data.x), int(state_data.y))
        letters.write(states_left)

states_to_learn = pd.DataFrame(states_to_learn, columns=["State"])
states_to_learn.to_csv('states_to_learn.csv', index=True)

screen.exitonclick()
