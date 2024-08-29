from turtle import Turtle,Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(12)
tim.speed(0)

colors = ["cornflower blue", "lime green", "orange", "maroon", "hot pink", "purple", "blue violet", "black"]
direction = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(25)
    tim.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()

