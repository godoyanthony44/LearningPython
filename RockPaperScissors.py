import random
import hands

npc_value = random.randint(1,3)
person_value = int(input("1 for Rock, 2 for Paper, 3 for Scissors\n"))

print("Computer:")
if npc_value == 1:
    print(hands.rock)
elif npc_value == 2:
    print(hands.paper)
elif npc_value == 3:
    print(hands.scissors)

print("You:")

if person_value == 1:
    print(hands.rock)
elif person_value == 2:
    print(hands.paper)
elif person_value == 3:
    print(hands.scissors)


if person_value == npc_value:
    print("Draw!")
elif npc_value == 1 and person_value == 2:
    print("Player Wins")
elif npc_value == 2 and person_value == 3:
    print("Player Wins")
elif npc_value == 3 and person_value == 1:
    print("Player Wins")
elif person_value == 1 and npc_value == 2:
    print("Computer Wins")
elif person_value == 2 and npc_value == 3:
    print("Computer Wins")
elif person_value == 3 and npc_value == 1:
    print("Computer Wins")

#test comment to commit



