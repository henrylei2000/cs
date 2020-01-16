"""
 This is the first loop program
 Henry Lei
 Spring 2020
"""


def tricky():
    for i in range(3):
        print("tricky")


def squares():
    for i in range(5):
        print((i+1)**2)


def three_squares():
    for i in range(3):
        n = int(input("Which number would you like to square: "))
        print(n*n)


def reverse_count():
    n = int(input("Which number would you like to reverse count: "))
    for i in range(n):
        print(n - i)


tricky()
squares()
three_squares()
reverse_count()
