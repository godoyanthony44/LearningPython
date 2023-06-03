from turtle import Screen
from time import sleep
from Snake import Snake

# Speed for the snake, increment as the score updates. game is on is true while the player has not collided
speed = .1
game_is_on = True

# Create screen and setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake...")
screen.tracer(0)

# Create snake and add a listener to the screen
snake = Snake()
screen.listen()

# Start game and listen for keys
while game_is_on:
  sleep(speed)
  screen.onkey(snake.up, "w")
  screen.onkey(snake.down, "s")
  screen.onkey(snake.left, "a")
  screen.onkey(snake.right, "d")
  snake.move()
  screen.update()

# Exit by clicking on the screen
screen.exitonclick()
