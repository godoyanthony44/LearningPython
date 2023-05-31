from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width = 500, height = 400)
bet_color = screen.textinput(title = "make your bet", prompt="Which turtle will win the race? Enter a color: ")
race_is_on = True
turtles = []
colors = ['red', 'blue', 'orange', 'purple', 'brown']
for i in range(5):
    turtles.append(Turtle())
    turtles[i].color(colors[i])
    turtles[i].shape('turtle')
    turtles[i].penup()
    turtles[i].goto(x=-240, y= (i*75)-140)

while race_is_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            highest_score = turtle.pencolor()
            race_is_on = False
        else:
            turtle.forward(randint(0,10))

if bet_color == highest_score:
    print(f"the winner is {highest_score} you were right!")
else:
    print(f"the winner is {highest_score} you were wrong!")






screen.exitonclick()