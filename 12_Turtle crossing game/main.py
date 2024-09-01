import time
from turtle import Screen
from cars import CarManager
from player import Player
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Collision with cars
    for car in car_manager.traffic:
        if car.distance(player) < 20:
            game_is_on = False

    # Detecting the crossing of finish line
    if player.is_at_finishline():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()
scoreboard.game_over()

screen.exitonclick()
