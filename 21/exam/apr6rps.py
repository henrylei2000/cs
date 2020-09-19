import random


def get_pick():

    finish = False

    while not finish:

        choice = input("r,p,s: ")
        if choice in "rps":
            finish = True
        else:
            print("Please enter r, p, or s!")

    if choice == "r":
        return "rock"
    elif choice == "p":
        return "paper"
    elif choice == "s":
        return "scissors"


def winner(user, comp):

    print("I chose %s" % user)
    if user == comp:
        return "tie"
    elif (user == "rock" and comp == "paper") or (user == "scissors" and comp == "rock") or (user == "paper" and comp == "scissors"):
        return "comp"
    elif (user == "rock" and comp == "scissors") or (user == "scissors" and comp == "paper") or (user == "paper" and comp == "rock"):
        return "user"


def main():
    user = get_pick()
    comp = random.choice(["rock", "paper", "scissors"])
    result = winner(user, comp)

    if result == "user":
        print("I WIN!")
    elif result == "tie":
        print("tie...")
    else:
        print("you lose :(")


main()

