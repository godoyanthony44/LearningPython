import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
car_garage = CarManager()
player = Player()
score = Scoreboard()



game_is_on = True
while game_is_on:
    screen.onkey(player.up, 'w')
    car_garage.move()
    for cars in car_garage.cars:
        if player.distance(cars) < 25:
            score.game_over()
            game_is_on = False
    if player.ycor() == 280:
        score.update_score()
        car_garage.fast_movement()
    time.sleep(0.1)
    screen.update()


screen.exitonclick()
