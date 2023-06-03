from turtle import Turtle

# Setting Constants for the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Creating Snake Class
class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()

    # Creating Create_Snake function to create the starting snake
    def create_snake(self):
        for i in STARTING_POSITIONS:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(i)
            self.snake_segments.append(snake)
        self.head = self.snake_segments[0]

    # Have the snake move with the Move function
    def move(self):
        for seg in range((len(self.snake_segments) - 1), 0, -1):
            x_cor = self.snake_segments[seg-1].xcor()
            y_cor = self.snake_segments[seg - 1].ycor()
            self.snake_segments[seg].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)

# The functions below are for movement in each direction.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
