import random

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

def num_check(question, low, high):
      valid = False
      while not valid:
        try:
            # Ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                    return response

            #output and error
            
        except ValueError:
         print("Please enter a whole number between 1 and 10")

# Main routine goes here ...
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print()

# ask the user how much they want to play with

how_much = num_check("How much would you like to play with? ", 0, 10)

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":
    
    #increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    print("*** Rounds #{} ***".format(rounds_played))
  
    chosen_num = random.randint(1, 100)
   
    #adjust balance
    if 1 <= chosen_num <= 5:
        chosen == "unicorn"
        balance += 4    

        
    elif 6 <= chosen_num <= 36: 
        chosen == "donkey"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
         chosen = "horse"
        else:
            chosen = "zebra"
        balance -= 0.5

    print("You got a {}. Your balance is"
          "${:.2f} ".format(chosen, balance))


    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
     play_again = input("Please Enter to play again "
                        "or 'xxx' to quit")
print()
print("Final balance", balance)


print()

print("You will be spending ${}".format(how_much))

print()

print("Program continues")
print()