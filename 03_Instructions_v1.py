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


def instructions():
     print("**** How to Play ****")
     print()
     print("The rules of the game go here")
     print()
     return""

# Main routine goes here ...
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print("Program continues")