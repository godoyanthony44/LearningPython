import random
from gameData import *
from os import system as sys
score = 0
first_person = 0
second_person = 0
game_running = True


def random_data():
    personData = random.choice(data)
    return personData


def compare_data(first, second, decision, points):
    global game_running

    first_followers = int(first['follower_count'])
    second_followers = int(second['follower_count'])

    if (decision == 'A' or decision == 'a') and (first_followers > second_followers):
        return points+1
    elif (decision == 'B' or decision == 'b') and (first_followers < second_followers):
        return points+1
    else:
        sys('clear')
        print(logo)
        print(f"your choice was wrong, final score: {points}")
        game_running = False
        return points


while game_running:
    sys('clear')
    first_person = random_data()
    second_person = random_data()
    print(logo)
    print(f"Current Score: {score}")
    print(f"Compare A: {first_person['name']}, {first_person['description']}, from {first_person['country']}")
    print(vs)
    print(f"Against B: {second_person['name']}, {second_person['description']}, from {second_person['country']}")
    choice = input("Who has more followers? Type 'A' or 'B': ")
    score = compare_data(first_person, second_person, choice, score)








