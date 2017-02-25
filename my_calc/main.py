import re

# Simple Calculator

print("Welocme ")
print("Please enter an equation")
print("Hit q to quit")

# Global variables
run = True
previous = 0
beenrun = False

# Calculation function

def perform_cal():

    global run
    global previous
    global beenrun
    equation = ""

    # Input previous or first
    if beenrun == False:
        equation = input("Enter an equation")
    else:
        equation = input(str(previous))

    if equation == 'q':
        print("Thank you, Have a good one")
        run = False
    else:
        equation = re.sub('[a-zA-z,:()" "%]', "" ,equation)

        if beenrun == False:
            previous = eval(equation)
            beenrun = True
        else:
            previous = eval(str(previous) + equation)

        print("Result: ",previous)


while run:
    perform_cal()

