letter_location = ""
names_location = ""
finished_letter_location = ""
with open(letter_location) as letter:
    letter_data = letter.read()

with open(names_location) as names:
    names_data = names.read()
    names = names_data.split("\n")

for name in names:
    with open(f"{finished_letter_location}", mode='w')as letters:
        letters.write(letter_data.replace("[name]", f"{name}"))



