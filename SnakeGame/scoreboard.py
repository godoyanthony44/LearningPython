from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(0, 270)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align='center', font=('Arial', 20, 'normal'))

