"""
Friends in a party

Henry Lei
2/3/2020
"""


def total(number_of_friends):
    number = 0
    print("You invite " + str(number_of_friends) + " friends")
    for i in range(1, 8):
        more_friends = number_of_friends ** i
        number = number + more_friends
        print("Your friends invite " + str(more_friends) + " more people!")
    return number


def main():
    guest = int(input("Enter the number of close friends: "))
    friends = total(guest)
    print("You expect " + str(friends) + " people at your party!")


main()

