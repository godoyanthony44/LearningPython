import random
from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 40
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        starting_y = 280
        for i in range(12):
            self.cars.append(Turtle())
            self.cars[i].penup()
            self.cars[i].shape("square")
            self.cars[i].shapesize(stretch_len=2, stretch_wid=1)
            self.cars[i].color(choice(COLORS))
            self.cars[i].setpos(randint(-200, 280), starting_y)
            starting_y -= STARTING_MOVE_DISTANCE

    def move(self):
        random.shuffle(self.cars)
        for car in self.cars:
            if car.xcor() >= -300:
                car.setx(car.xcor()-MOVE_INCREMENT)
            elif car.xcor() < -300:
                car.setpos(randint(200,280), 280-(STARTING_MOVE_DISTANCE*self.cars.index(car)))

    def fast_movement(self):
        global MOVE_INCREMENT
        MOVE_INCREMENT += 5
