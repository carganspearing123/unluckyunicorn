# Functions go here ...
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
how_much = num_check("How much would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))