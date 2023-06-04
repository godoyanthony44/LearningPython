from turtle import Screen
from time import sleep
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

# Speed for the snake, increment as the score updates. game is on is true while the player has not collided
SPEED = .1
game_is_on = True

# Create screen and setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake...")
screen.tracer(0)

# Create snake and add a listener to the screen
score = Scoreboard()
snake = Snake()
food = Food()
screen.listen()

# Start game and listen for keys
while game_is_on:
    sleep(SPEED)
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    snake.move()
    screen.update()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        score.update_score()
        snake.create_segment()
        food.refresh()
    # Detect Collision with Wall
    elif (snake.head.xcor() > 280) or (snake.head.xcor() < -280) or (snake.head.ycor() > 280) or (
            snake.head.ycor() < -280):
        score.resets()
        snake.resets()

    # Detect Collision with self
    for segment in snake.snake_segments[1:]:
      if snake.head.distance(segment) < 15:
        score.resets()
        snake.resets()

# Exit by clicking on the screen
screen.exitonclick()
