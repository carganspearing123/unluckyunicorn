from webbrowser import get


print("hello world")
get_name = input("Who are you? ")
print(get_name)

# Ask users for a number
get_number = int(input("Choose a number? "))

# Multiply the number by 5
times_five = get_number * 5

answer = "{} times five is equal to " \
     "{}".format(get_number, times_five)

# Output the result
print(answer)

name = ""
while name.lower() != "xxx":
     name = input("Who are you? ")
     print(name)


print()
print("We are done!")