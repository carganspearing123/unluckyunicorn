# Functions go here ...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        
        if response == "yes" or response == "y":
            # response = "yes"
            return "yes"

        elif response == "no" or response == "n":
            # respomse = "no"
            return "no"

        else:
            print("Please awnser yes / no")

# Main routine goes here ...
show_instructions = yes_no("Have you played the game before? ")

print("You chose {}".format (show_instructions))
print()
having_fun = yes_no("Are you having fun? ")
print("you said {} to having fun".format(having_fun))