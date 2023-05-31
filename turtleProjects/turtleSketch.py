from turtle import Turtle, Screen

tomberry = Turtle()
screen = Screen()
screen.listen()



def move():
    tomberry.forward(10)


def move_left():
    tomberry.left(10)


def move_right():
    tomberry.right(10)


def move_back():
    tomberry.back(10)


screen.onkey(key='w', fun=move)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='c', fun=tomberry.clear)

screen.exitonclick()
