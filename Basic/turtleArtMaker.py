import random
from turtle import *


colors = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

matrix_size = int(input("what is the ideal size of an art piece in dots (1-10): "))
tomBrady = Turtle()
tomBrady.setheading(230)
tomBrady.penup()
tomBrady.hideturtle()
tomBrady.forward(40*matrix_size)
init_x = tomBrady.xcor()
tomBrady.setheading(0)

colormode(255)
for _ in range(matrix_size):
    for n in range(matrix_size):
        tomBrady.dot(matrix_size*5, tuple(random.choice(colors)))
        tomBrady.forward(5 * matrix_size)
    tomBrady.sety((tomBrady.ycor()+(matrix_size*5)))
    tomBrady.setx(init_x)






