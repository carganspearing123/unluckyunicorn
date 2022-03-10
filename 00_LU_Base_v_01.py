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
     print()
     print()
     print("**** How to Play ****")
     print()
     print()
     print("Choose a starting amount (minimum $1, maximum $10).")
     print()
     print("Then press <enter> to play. You will either get a horse, a zebra, a donkey or a unicorn")
     print()
     print("It costs $1 per round. Depending on your prize you might win some of the money back. Here's the payout amounts...")
     print("Unicorn: $5.00 (balance increases by $4)")
     print("Horse: $0.50 (balance decreases by $0.50)")
     print("Zebra : $0.50 (balance decreases by $0.50)")
     print("Donkey: $0.00 (balance decreases by $1)")
     print()
     print("Can you avoid the donkeys, get the unicorns and walk home with the money??")
     print()
     return""

def num_check(question, low, high):
    error = "Please enter a whole number between {} and {}".format(low, high)

    valid = False
    while not valid:
        try:
            # Ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response

            # output and error
            else:
                print(error)

        except ValueError:
            print(error)

def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# Main routine goes here ...

print()
print()
print("****Welcome to the Lucky Unicorn game****")
print()
print()

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
        chosen = "unicorn"
        decoration = "!"
        balance += 4    

        
    elif 6 <= chosen_num <= 36: 
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
         chosen = "horse"
         prize_decoration = "H"
        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = "You got a {}. Your balance is" \
          "${:.2f} ".format(chosen, balance)

    statement_generator(outcome, prize_decoration)


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