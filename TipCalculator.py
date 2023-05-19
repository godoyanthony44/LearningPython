print("Welcome to the Tip Calculator")
bill_Total = int(input("What was the bill total? "))
tip_Percentage = int(input("What percentage would you like to give? 10, 12, or 15? "))
people_Split = int(input("How many people to split the bill? "))

split_total = bill_Total / people_Split * (1 + (tip_Percentage / 100))

final_amount = str(round(split_total,2))
print("Each person should pay: " + final_amount)


