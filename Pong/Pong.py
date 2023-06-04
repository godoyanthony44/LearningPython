from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from time import sleep
from scoreboard import Scoreboard
from CenterLine import CenterLine

# Assign the variables
game_is_on = True
screen = Screen()
# Screen setup
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# More variables and ball and paddles
score = Scoreboard()
l_paddle = Paddle(-350)
r_paddle = Paddle(350)
ball = Ball()
centerLine = CenterLine()

# Get letter pushes and make it move
screen.listen()

ball.random_start()

# Game starting method
while game_is_on:

    screen.onkey(l_paddle.up, 'w')
    screen.onkey(l_paddle.down, 's')
    screen.onkey(r_paddle.up, 'Up')
    screen.onkey(r_paddle.down, 'Down')

    if (ball.distance(l_paddle) < 60 or ball.distance(r_paddle) < 60) and (ball.xcor() < -338 or ball.xcor() > 338):
        ball.bounce_x()
    if ball.xcor() > 410:
        score.update_score('left')
    elif ball.xcor() < -410:
        score.update_score('right')

    screen.update()
    ball.move()
    sleep(ball.ball_speed)

    if score.l_score == 7 or score.r_score == 7:
        score.clear()
        ball.clear()
        centerLine.clear()

        if score.l_score > score.r_score:
            score.write("Right Player wins with a score of 7", font=('Arial', 30, 'normal'), align="center")

        elif score.r_score > score.l_score:
            score.write("Left Player wins with a score of 7", font=('Arial', 30, 'normal'), align="center")
        game_is_on = False


screen.exitonclick()
