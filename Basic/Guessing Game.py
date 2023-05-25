import random
number = random.randint(1,100)
number_guessed = False


def attempt_count(challenge):
    if challenge == "easy":
        return 10
    if challenge == "hard":
        return 5


def is_number_guessed(guess):
    global number_guessed
    if guess > number:
        return "Too high. \n Guess again!"
    elif guess < number:
        return "Too low. \n Guess again!"
    else:
        number_guessed = True
        return "Correct!!"


print("Welcome to the Number Guessing Game! ")
print("Im thinking of a number between 1 - 100 ")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = attempt_count(difficulty)

while attempts != 0 and number_guessed == False:
    print(f"You have {attempts} attempts remaining to guess the number.")
    gus = int(input("Make a guess: "))
    print(is_number_guessed(gus))
    attempts -= 1




