# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

name_file = open("./Input/Names/invited_names.txt")
old_names_list = name_file.readlines()

# Creates a list of people and removed the space
for index in range(len(old_names_list) - 1):
    name = old_names_list[index]
    new_name = name.strip("\n")
    old_names_list[index] = new_name

for name in old_names_list:
    with open("./Input/Letters/starting_letter.txt") as file:
        message = file.read()
        edited_message = message.replace("[name]", name)
    with open("./Output/ReadyToSend/letter_for_" + name+".txt", mode="w") as file:
        file.write(edited_message)
