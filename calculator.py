"""Calculator. After user provides two integer numbers and an operator
program will perform simple mathematic calculations. If user instead
of number provides letter (from english alphabet) then program will exit.
"""


__version__ = 0.1
__author__ = "Michal Doniec"


import sys


alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q",\
            "r","s","t","u","w","x","y","z")

operations = ("+","-","*","/")


def isinteger(s):
    """Determines whether user's input is an integer."""
    try:
        int(s)
    except ValueError:
        return False


def operators(s,a,c):
    """Determines operant and performs algorythmic operation."""
    if s == "+":
        total = int(a) + int(c)
        print("Result: " + str(total))

    elif s == "-":
        total = int(a) - int(c)
        print("Result: " + str(total))

    elif s == "*":
        total = int(a) * int(c)
        print("Result: " + str(total))

    else:
        total = int(a) / int(c)
        print("Result: " + str(total))


a = input("Enter a number (integer) or a letter to exit: ")

while isinteger(a) == False and a.lower() not in alphabet:
    print("Invalid sign.")
    a = input("Enter a number (integer) or a letter to exit: ")

while a.lower() not in alphabet:
    b = input("Enter an operator (+, -, * or /): ")
    while b not in operations:
        print("Invalid sign.")
        b = input("Enter an operation (+, -, * or /): ")

    else:
        c = input("Enter another number (integer): ")
        while isinteger(c) == False:
            print("Invalid sign.")
            c = input("Enter another number (integer): ")

        else:
            operators(b,a,c)
            a = input("Enter a number (integer) or a letter to exit: ")
            while isinteger(a) == False and a.lower() not in alphabet:
                print("Invalid sign.")
                a = input("Enter a number (integer) or a letter to exit: ")

else:
    sys.exit("Goodbye!")
