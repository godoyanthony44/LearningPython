from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.setpos(STARTING_POSITION)

    def up(self):
        if self.ycor() <= FINISH_LINE_Y:
            self.sety(self.ycor()+MOVE_DISTANCE)
        else:
            self.setpos(STARTING_POSITION)



