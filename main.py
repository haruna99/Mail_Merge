file_1 = open("./Input/Names/invited_names.txt", mode="r")
invited_names = file_1.readlines()


with open("./Input/Letters/starting_letter.txt") as file_2:
    letter = file_2.read()
    for name in invited_names:
        name = name.strip()
        new_letter = letter.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_file:
            new_file.write(new_letter)
