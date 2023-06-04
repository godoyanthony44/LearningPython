FONT = ("Courier", 24, "normal")
POSITION = -280,260
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(POSITION)
        self.color("black")
        self.write("Level: 0", font=FONT)
        self.level = 0

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level} ", font=FONT)

    def game_over(self):
        self.clear()
        self.setpos(-80,0)
        self.write("Game Over", font=FONT)

