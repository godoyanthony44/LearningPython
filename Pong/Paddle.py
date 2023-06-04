from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        for i in range(2):
            self.goto(x_position,0)
            self.shape("square")
            self.color("white")
            self.setheading(90)
            self.shapesize(stretch_wid=1, stretch_len=5)
            self.penup()

    def up(self):
        if self.ycor() < 280:
            self.forward(50)

    def down(self):
        if self.ycor() > -280:
            self.backward(50)



