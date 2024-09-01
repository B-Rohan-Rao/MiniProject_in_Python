from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.new_car = None
        self.traffic = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 8)
        if random_chance == 1:
            self.new_car = Turtle("square")
            self.new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.new_car.penup()
            self.new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            self.new_car.goto(300, random_y)
            self.traffic.append(self.new_car)

    def move_cars(self):
        for cars in self.traffic:
            cars.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
