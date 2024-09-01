from turtle import Screen
import time
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(900, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Creating instances
r_paddle = Paddle(x_cor=400)
l_paddle = Paddle(x_cor=-400)
ball = Ball()
scoreboard = Scoreboard()

# Movements
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #  Detect collision with side walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #  Detect collision with both right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 370 or ball.distance(l_paddle) < 50 and ball.xcor() > -370:
        ball.bounce_x()

    #  Detect collision with the wall
    if ball.xcor() > 450:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -450:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
