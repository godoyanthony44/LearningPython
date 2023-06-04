from turtle import Turtle


class Scoreboard(Turtle):

    # Create center line and init score
    def __init__(self):
        super().__init__()
        self.color("white")
        self.setheading(90)
        self.penup()
        self.hideturtle()
        self.setpos(0, 200)
        self.l_score = 0
        self.r_score = 0

        # Create scorecard
    def update_score(self, person):
        if person == 'left':
            self.r_score += 1
        if person == 'right':
            self.l_score += 1
        self.clear()
        self.write(f" {self.l_score}   {self.r_score} ",font=('Arial', 80, 'normal'), align="center")
