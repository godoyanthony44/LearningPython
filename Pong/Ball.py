from turtle import Turtle
from random import randint, choice


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.setpos(0, 0)
        self.ball_speed = .12

    # randomizes the start
    def random_start(self):
        heading = choice((randint(-45, 45), randint(120, 220)))
        self.setheading(heading)

    # function to push back when it hits a box
    def bounce_y(self):
        direction = self.heading()*-1
        self.setheading(direction)

    # function to push back when it hits a box
    def bounce_x(self):
        self.ball_speed *= .95
        direction = self.heading()
        if self.heading() < 90:
            direction = self.heading() + 180
        elif (self.heading() > 90) and (self.heading() < 180):
            direction = self.heading() + 90
        elif self.heading() > 180:
            direction = self.heading() - 190

        self.setheading(direction)

    # moving function and setting ball
    def move(self):
        if self.ycor() > 300 or self.ycor() < -300:
            self.bounce_y()
            self.forward(20)
        elif self.xcor() > 410 or self.xcor() < -410:
            self.restart()
        else:
            self.forward(20)

    # Restart function for when ball goes off
    def restart(self):
        self.setpos(0, 0)
        self.random_start()


