from turtle import Turtle,Screen
import random

tim = Turtle()
tim.shape("turtle")

colors = ["cornflower blue", "lime green", "orange", "maroon", "hot pink", "purple", "blue violet", "black"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.left(angle)

for shape_side_n in range(3, 100):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)        

screen = Screen()
screen.exitonclick()
