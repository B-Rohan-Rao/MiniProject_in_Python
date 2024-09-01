from turtle import Turtle

YCOR = 0
WIDTH = 100
HEIGHT = 100


class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.x_cor = x_cor
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(self.x_cor, YCOR)

    def up(self):
        self.forward(20)

    def down(self):
        self.back(20)
