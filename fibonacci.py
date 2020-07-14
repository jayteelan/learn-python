# run this with $ python fibonacci.py

a, b = 0, 1  # multiple assignment of variables
# input() takes the user prompt as an argument; variables use snake_case
up_to = input("how far would you like to go? ")
while a < int(up_to):  # variables default to strings, therefore need to parse as int
    print(a, end=', ')  # "end" argument avoids line breaks at end of each loop
    a, b = b, a + b
