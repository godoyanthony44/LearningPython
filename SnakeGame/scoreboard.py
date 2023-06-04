from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(0, 270)
        with open("score.txt") as file:
            contents = file.read()
            self.high_score = int(contents)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", move=False, align='center', font=('Arial', 20, 'normal'))

    def update_score(self):
        self.score += 1
        self.write_score()

    def resets(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode='w') as file:
                file.write(f"{self.score}")

        self.score = 0
        self.write_score()

