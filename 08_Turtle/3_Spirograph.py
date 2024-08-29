from turtle import Turtle, Screen
import random

tim = Turtle()

# Set the color mode to 255 (for RGB colors)
screen = Screen()
screen.colormode(255)

tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(10)

screen.exitonclick()
