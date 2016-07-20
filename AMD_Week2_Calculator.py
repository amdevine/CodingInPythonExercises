#!/usr/bin/env python3

print('''~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
        SUPER MATH MACHINE
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~''')

username = input("\nWhat is your name? ")
print("\nHi, {user}! We are going to do math today. Please input two numbers.\n".format(
    user=username))

addmore = True
while addmore:

    while True:
        try:
            n1 = float(input("Number 1: "))
            print()
            break
        except ValueError:
            print("Not a number! Please try again!")

    while True:
        try:
            n2 = float(input("Number 2: "))
            print()
            break
        except ValueError:
            print("Not a number! Please try again!")

    while True:
        opn = input("Operation (enter +, -, *, or /): ")
        if opn in ["+", "-", "*", "/"]:
            print()
            break
        else:
            print("Not a valid choice! Please try again!")

    if opn == "+":
        answer = n1 + n2
    elif opn == "-":
        answer = n1 - n2
    elif opn == "*":
        answer = n1 * n2
    elif opn == "/":
        answer = n1 / n2
    
    print("\t{n1} {opn} {n2} = {answer}\n".format(n1=n1, opn=opn, n2=n2, answer=answer))

    while addmore:
        a = input("Would you like to do more math (enter Y or N)? ")
        if a in ["n", "N", "no", "No", "NO"]:
            addmore = False
            break
        elif a not in ["y", "n", "Y", "N", "Yes", "No", "yes", "no", "YES", "NO"]:
            print("{choice} was not a choice!".format(choice=a))
        else:
            print()
            break

print("\nBye, {name}! Thanks for doing math today!!!!".format(name=username))
