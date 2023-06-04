from turtle import Turtle


class CenterLine(Turtle):

    # Create center line and init score
    def __init__(self):
        super().__init__()
        self.color("white")
        self.setheading(90)
        self.penup()
        self.setpos(0, -292)
        for i in range(21):
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)
