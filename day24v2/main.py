PLACEHOLDER="[name]"

NAME_PATH="\\Users\\cembora\\Desktop\\python\\day24v2\\Input\\Names\\invited_names.txt"

LETTER_PATH="\\Users\\cembora\\Desktop\\python\\day24v2\\Input\\Letters\\starting_letter.txt"

SEND_PATH="\\Users\\cembora\\Desktop\\python\\day24v2\\Output\\ReadyToSend\\"

with open(f"{NAME_PATH}") as names_file:
    names=names_file.readlines()
    
with open(f"{LETTER_PATH}") as letter_file:
    letter_contents=letter_file.read()

    for name in names:
        stripped_name=name.strip()
        new_letter=letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"{SEND_PATH}letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)  
        
