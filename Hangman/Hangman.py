import random,words,os,time

#Create all needed variables
clear = lambda: os.system('clear')  # on Linux System
word = random.choice(words.wordie)
guess = []
wordCheck = []
attempts = 6
game_over = False

#Print out the Hangman Logo
print(words.logo)
time.sleep(1)
clear()

#Main Game Mechanism
while game_over == False and (attempts != 0):

    #prints out the letter or _ depending on if its been guessed
    for n in word:
        if n in guess:
            wordCheck.append(n)
            print(n, end="", flush=True)
        else:
            wordCheck.append("_")
            print("_", end="", flush=True)

#Checks if the word has been guessed
    if "_" in wordCheck:
        game_over = False
    else:
        game_over = True

    wordCheck.clear()

#If the word has not been guessed
    if game_over == False:
        print("\n")

#Prints out the Hangman
        print(words.stages[attempts])
#Guess the letter
        guessed_letter = input("Try in a one letter guess: ")
        guess.append(guessed_letter)
#Check if the letter is in the word
        if guessed_letter not in word:
            attempts-=1
        elif guessed_letter in word:
            guessed_word = ''.join(guess)
#Clear the screen
    clear()

#After game has been finished print whether they won or lost!
if game_over == True:
    print("You Won Hooray")
else:
    print(words.stages[0])
    print("Game over!")