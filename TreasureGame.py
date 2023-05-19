import treasure

print(treasure.treasure)

print("Welcome to the Treasure Trove.")
print("Your mission is to find the treasure")
first_action = input("You're at a cross road. Where do you want to go? 'left' or 'right'\n")
if first_action != "left":
    print("A crab ate you because why not yk")
else:
    second_action = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across\n")
    if second_action != 'wait':
        print("You died because you got exhausted in the water I mean come did you really think you could make it")
    else:
        third_action = input("You arrived at the island unharmed. There is a house with 3 doors. One red, One yellow and One blue. Which colour do you choose? \n")
        if third_action != 'blue':
            print("A tiger ate you becasue I mean yeah idk howdy tho! ")
        else:
            print("You managed to make it alive, Congrats, there is no treasure to be found AHAHHAHA ")