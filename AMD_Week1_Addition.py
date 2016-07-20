#!/usr/bin/env python3

print('''~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
        SUPER MATH MACHINE
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~''')

username = input("\nWhat is your name? ")
print("\nHi, {user}! We are going to do addition today!!! Please input two integers.\n".format(
    user=username))

addmore = True
while addmore:

    while True:
        try:
            n1 = int(input("Integer 1: "))
            print()
            break
        except ValueError:
            print("Not an integer! Please try again!")

    while True:
        try:
            n2 = int(input("Integer 2: "))
            print()
            break
        except ValueError:
            print("Not an integer! Please try again!")

    print(
        "The sum of {n1} + {n2} is {ans}!\n".format(n1=n1, n2=n2, ans=n1 + n2))

    while addmore:
        a = input("Would you like to add more numbers? (y/n) ")
        if a in ["n", "N", "no", "No", "NO"]:
            addmore = False
            break
        elif a not in ["y", "n", "Y", "N", "Yes", "No", "yes", "no", "YES", "NO"]:
            print("{choice} was not a choice!".format(choice=a))
        else:
            print()
            break

print("\nThanks for adding today!!!!")
