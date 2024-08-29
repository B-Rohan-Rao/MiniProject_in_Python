from turtle import Turtle, Screen
import random

# Set up the screen
screen = Screen()
screen.setup(width=900, height=800)

# Set up turtles
colors = ["red", "blue", "green", "orange", "purple", "brown"]
names = ["Cruze", "Chick", "Lyla", "Walle", "McQueen", "Matter"]
turtles = []

# Creating turtles and setting up initial positions
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-400, y=-100 + index * 50)
    turtles.append(new_turtle)

# Ask the user to place a bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(f"You have placed your bet on: {user_bet}")

# Start the race
if user_bet:
    race_on = True
else:
    race_on = False

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 400:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations! The {winning_color} turtle is the winner!")
            else:
                print(f"Sorry, the {winning_color} turtle won the race.")
            break

        # Move the turtle forward by a random amount
        distance = random.randint(0, 10)
        turtle.forward(distance)

# Close the screen on click
screen.exitonclick()
