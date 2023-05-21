import random
import string

print("Welcome to the Py Pass Generator!")
Website = input("Give me a website for this account ")
username = input("Give me a username for this account ")

letters = int(input("Give me a number of letters for the password\n"))
numbers = int(input("Give me a number of numbers for the password\n"))
symbols = int(input("Give me a number of symbols for your password\n"))


password = []
for i in range(letters):
    password.append(random.choice(string.ascii_letters))
for i in range(numbers):
    password.append(random.choice(string.digits))
for i in range(symbols):
    password.append(random.choice(string.punctuation))

random.shuffle(password)
new_password = ''.join(password)

print(Website, username + " " + new_password)


