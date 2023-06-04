import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
text = turtle.Turtle('circle')
text.color("black")
text.shapesize(stretch_len=.5,stretch_wid=.5)
text.penup()
game_is_on = True
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
states_guessed = 0
FONT = ("Courier", 8, "normal")


while game_is_on:
    answer_state = screen.textinput(title=f"Guess the state {states_guessed}/50", prompt="What's another states name? ").title()
    if answer_state in states:
        states_guessed += 1
        state_location_x = data.x[answer_state == data.state].to_dict()
        state_location_y = data.y[answer_state == data.state].to_dict()
        for key in state_location_x:
            key_x = key
        for key in state_location_x:
            key_y = key
        text.setpos(state_location_x[key_x], state_location_y[key_y])
        text.write(f"{answer_state}", font=FONT)

turtle.mainloop()

