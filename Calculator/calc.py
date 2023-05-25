print("Welcome to the Calculator!")
Calc_on = True
current_key = 0
results = {}

def calculate(firstNum,secondNumr,operat):
    if operator == "+":
        result = firstNum + secondNumr
    elif operator == "-":
        result = firstNum-secondNumr
    elif operator == "*":
        result = firstNum*secondNumr
    elif operator == "/":
        result = firstNum/secondNumr
    print(f"{firstNum} {operat} {secondNumr} = {result}")
    results.update({current_key:result})

def continue_calc(cont, curr, first):
    if cont == 'n':
        curr = 0
        results.clear()
    elif cont == 'y':
        curr+=1
        first = int(results.get(current_key))
    else:
        print("You did not input y or n, we will restart now! ")
    return first, curr


while Calc_on:
    if current_key == 0:
        first_number = int(input("Please input the first number: "))
    operator = input("Please input an operator: \n + \n - \n * \n / \n")
    second_number = int(input("Please input the second number: "))
    calculate(first_number,second_number,operator)
    cont_Calc = input(f"Enter 'y' to continue with {results.get(current_key)} or 'n' to start a new calculation: \n")
    first_number,current_key = continue_calc(cont_Calc,current_key,first_number)


