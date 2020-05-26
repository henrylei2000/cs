"""
memory game

Henry Lei
03/25/2020

"""

import random
import os


def set_number_of_cards():
    """
    Purpose: set number of cards
    Parameters: none
    Return (int): number of cards
    """
    finish = False
    number_of_cards = 10  # default

    while not finish:

        number_string = input("How many cards do you want to play? ")

        if alldigits(number_string):  # check if it's an integer
            number_of_cards = int(number_string)
            if 6 <= number_of_cards <= 20:  # check if it's in range
                if number_of_cards % 2 == 0:  # check if it's an even number
                    finish = True
                else:
                    print("Please enter an even integer from 6 to 20!")
            else:
                print("Please enter an integer from 6 to 20!")
        else:
            print("Please enter an integer!")

    return number_of_cards


def shuffle_cards(seeds, number_of_cards):
    """
    Purpose: shuffle cards
    Parameters:
        seeds: birds (list of string) from which a shuffled list is created
        number_of_cards: number of cards in total from which to play the game
    Return: shuffled cards (list of string)
    """

    if len(seeds) < number_of_cards / 2:
        seeds += ["hummingbird", "crow", "sparrow", "eagle", "albatross"]

    shuffled = []

    for i in range(int(number_of_cards / 2)):  # need 5 cards
        shuffled += [seeds[i], seeds[i]]

    # make a random shuffle
    for i in range(10):  # shuffle 10 times
        number_one = random.randrange(len(shuffled))
        number_two = random.randrange(len(shuffled))
        temp = shuffled[number_one]
        shuffled[number_one] = shuffled[number_two]
        shuffled[number_two] = temp

    return shuffled


def hide_cards(number_of_cards):
    """
    purpose: hide cards
    parameters:
        number_of_cards: number of cards in total from which to play the game
    return (list): initial card status
    """
    cards = []
    for i in range(number_of_cards):
        cards += ["===" + str(i) + "==="]
    return cards


def display_cards(current_cards):
    """
    Purpose: display cards
    Parameters:
        current_cards: a list of current cards, flipped and unflipped
    Return: none
    """
    print()
    print("========================================================================")

    length = len(current_cards)
    half_length = int(length / 2)

    if length <= 10:
        for item in current_cards:
            print(item, end=" ")
    else:  # longer than 10
        for i in range(half_length):
            print(current_cards[i], end=" ")

        print("\n")  # new line

        # print the rest (11th onwards)
        for i in range(half_length, length):
            print(current_cards[i], end=" ")

    print()


# check digits
def alldigits(word):
    """
    Purpose: detect if the string entered contains all integers
    Parameters:  word -- an input string (string)
    Returns: True if the string contains all integers and False otherwise
    (Boolean)
    """

    all_digits = True  # flag

    if len(word) == 0:  # empty string is not a digit
        all_digits = False

    for letter in word:
        if letter not in "0123456789":
            all_digits = False  # flag
            break  # stop the loop if non-digit is detected

    return all_digits


def validate_choice(current_cards):
    """
    Purpose: validate user input
    Parameters:
        current_cards (list)
    Return (int): user's choice
    """
    finish = False

    length = len(current_cards)

    while not finish:
        choice = input("card to flip> ")
        if alldigits(choice):
            if 0 <= int(choice) < length:
                if "===" + choice + "===" not in current_cards:  # already flipped
                    print("You already matched that card...")
                else:
                    finish = True
            else:
                print("Please enter a card from 0 to %d!" % (length - 1))
        elif choice == "q":
            choice = "1000"  # 100 is code for q
            finish = True

    return int(choice)


def flip_cards(turn, current_cards, shuffled_cards):
    """
    Purpose: accept user input (flips)
    Parameters:
        turn (int): an integer to represent each round of guesses (two flips)
        current_cards (list of string): a list of current cards, flipped and unflipped
        shuffled_cards (list of string): a list of cards (the correct answer to be referenced)
    Return: flips (list of int), a list of flipped cards' indices
    """

    space_padding = " " * 20  # spacing to identify answer

    choice_one = -1  # initialization
    choice_two = -1  # initialization

    finish = False

    while not finish:
        # display current cards before flips
        display_cards(current_cards)
        # the first flip
        print("Turn #%s:" % turn)
        choice_one = validate_choice(current_cards)

        if choice_one == 1000:  # quit
            break

        print(space_padding + shuffled_cards[choice_one])
        # the second flip
        print("Turn #%s:" % turn)
        choice_two = validate_choice(current_cards)

        if choice_two == 1000:  # quit
            break

        print(space_padding + shuffled_cards[choice_two])

        if choice_one == choice_two:  # if guesses are the same, continue ask for input
            print("Duh...you can't flip the same card!")
        else:  # valid inputs, stop asking
            finish = True

    # prepare the list of indices
    flips = [choice_one, choice_two]
    return flips


def validate_flips(flips, current_cards, shuffled_cards):
    """
    Purpose: check if the two flipped cards match, update current cards accordingly
    Parameters:
        flips (list of int): a list of flipped cards' indices, two items
        current_cards (list of string): a list of current cards, flipped and unflipped
        shuffled_cards (list of string): a list of cards (the correct answer to be referenced)
    Return: none
    """
    choice_one = flips[0]
    choice_two = flips[1]

    if shuffled_cards[choice_one] == shuffled_cards[choice_two]:
        current_cards[choice_one] = shuffled_cards[choice_one]
        current_cards[choice_two] = shuffled_cards[choice_two]
        print("Correct!")
    else:
        print("Nope...")
    print()
    print()


def is_quit(flips):
    """
    Purpose: check if 'q' is entered for quit
    Parameters:
        flips (list of int): user's choice
    Return quit (Boolean): Boolean value of quit
    """
    quit = False
    for choice in flips:
        if choice == 1000:  # code for quit
            quit = True

    return quit


def is_finished(cards):
    """
    Purpose: check if all the cards have been matched
    Parameters:
        cards (list of string): current cards' status
    Return finished (Boolean): Boolean value of finished (all matched)
    """
    finished = True
    for i in range(len(cards)):
        if cards[i] == "===" + str(i) + "===":
            finished = False
    return finished


def grading(turn, number_of_cards):
    """
    Purpose: evaluate performance based on number of turns
    Parameters:
        turn (int): an integer to represent each round of guesses (two flips)
        number_of_cards (int): number of cards to play the game
    Return (str): message saying how well you performed

    """
    quickest = int(number_of_cards / 2)

    if turn <= quickest + 2:
        message = "super!"
    elif turn <= quickest * 2:
        message = "not bad."
    else:
        message = "Better luck next time."

    return message


def main():

    # welcome message
    print("""
~ ~  Welcome to M*E*M*O*R*Y G*A*M*E v1.0 ~ ~

Pick two cards at a time and see if they match.
Keep picking pairs of cards until you match them all!


    """)

    # set up the game
    number_of_cards = set_number_of_cards()

    # shuffle cards to get the referenced answer: shuffled
    birds = ["finch", "robin", "crane", "macaw", "stork", "egret", "raven"]  # seed cards

    shuffled = shuffle_cards(birds, number_of_cards)
    print(shuffled)  # TODO: remove

    # initialization
    current_cards = hide_cards(number_of_cards)

    # initialization for the game
    finish = False  # flag pattern
    quit = False
    turn = 0  # counter

    # game on!
    while not finish:

        # increase the turns
        turn += 1

        # accept user input to flip two cards in each turn
        flips = flip_cards(turn, current_cards, shuffled)

        if is_quit(flips):
            quit = True
            finish = True

        # validate guesses and update status of current cards
        if not quit:
            validate_flips(flips, current_cards, shuffled)

            # waiting for enter to clear screen
            input("Hit Enter to continue...")
            os.system('clear')

            # finish or not
            if is_finished(current_cards):
                finish = True

    # finished
    if not quit:
        display_cards(current_cards)

        # summary comment
        print()
        print("%d cards matched in %d turns." % (number_of_cards, turn))
        scores = grading(turn, number_of_cards)
        print(scores)
    else:
        print("Quitting...")


main()
