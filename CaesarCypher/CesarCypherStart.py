from ceaserrrr import ceaserCypher


print("Welcome to the Ceaser Cypher")

code_choice = '0'
while code_choice != '1':
    code_choice = input("would you like to 'encode' or 'decode' or 1 to exit: ")
    if code_choice != '1':
        message = input("Type your message: ")
        shift_number = int(input("Type the shift number: "))
        new_shift = ceaserCypher(code_choice,message,shift_number)
        print(new_shift)




