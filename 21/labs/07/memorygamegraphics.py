"""
Memory game (graphic version)

Henry Lei

03/27/2020
"""
from graphics import *
import random

# TDD: features

"""

Draw a playground

Setup the game (cards)

Flip the cards

Validate flips

Update the board (current cards status)

"""


def draw_background():
    """
    draw a background for the game
    :return: window
    """
    win = GraphWin("Memory Game", 1000, 800)
    win.setCoords(0, 0, 1000, 800)  # left-bottom as 0, 0
    return win


def setup(win):
    """
    :param win: window object
    :return: card images
    """

    # welcome message
    line1 = Text(Point(500, 750), "~ ~  Welcome to M*E*M*O*R*Y G*A*M*E v1.0 ~ ~")
    line2 = Text(Point(500, 735), "Pick two cards at a time and see if they match.")
    line3 = Text(Point(500, 720), "Keep picking pairs of cards until you match them all!")
    line1.draw(win)
    line2.draw(win)
    line3.draw(win)

    card_images = []
    for i in range(5):
        bird = Image(Point(200 + (i * 150), 600), "cards/cardBack.png")
        card_images.append(bird)
        bird.draw(win)

    for i in range(5):
        bird = Image(Point(200 + (i * 150), 400), "cards/cardBack.png")
        card_images.append(bird)
        bird.draw(win)

    return card_images


def shuffle_cards():
    """
    Purpose: shuffle cards
    Parameters: none
    Return (list of int): shuffled cards
    """

    shuffled = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]

    # make a random shuffle
    for i in range(10):  # shuffle 10 times
        number_one = random.randrange(len(shuffled))
        number_two = random.randrange(len(shuffled))
        temp = shuffled[number_one]
        shuffled[number_one] = shuffled[number_two]
        shuffled[number_two] = temp

    return shuffled


def pick_card(win, card_images):
    """
    :param win:
    :param card_images: list of image objects
    :return: card index (int)
    """
    click = win.getMouse()
    card = 0
    for image in card_images:
        if click_on_image(click, image):
            image.undraw()
            break
        card += 1
    return card


def click_on_image(point, image):
    """
    Purpose: check if a mouse click is on a given image
    Parameters:
        point(Point): the coords of a mouse click
        image(Image): the given image
    return: boolean
    """
    is_in_between = False

    center = image.getAnchor()

    # where is the mouse click
    x = point.getX()
    y = point.getY()

    # where are the coords of a button rectangle
    xi = center.getX()
    yi = center.getY()

    wi = image.getWidth()
    hi = image.getHeight()

    # when a click is in a the button
    x_is_in_between = (xi - wi / 2 < x < xi + wi / 2)
    y_is_in_between = (yi - hi / 2 < y < yi + hi / 2)

    clicked = x_is_in_between and y_is_in_between

    return clicked


def uncover_card(win, card_picked, cards):
    """
    purpose: to uncover the card picked
    :param win:
    :param card_picked: index (int)
    :param cards: list of int (indices)
    :return: none
    """
    if card_picked < 5:
        image = Image(Point(200 + (card_picked * 150), 600), "cards/card%d.png" % (cards[card_picked] + 1))
        image.draw(win)
    else:
        image = Image(Point(200 + ((card_picked - 5) * 150), 400), "cards/card%d.png" % (cards[card_picked] + 1))
        image.draw(win)


def cover_card(win, card_picked):
    """
    purpose: to hide the card picked
    :param win:
    :param card_picked: index (int)
    :return: none
    """
    if card_picked < 5:
        image = Image(Point(200 + (card_picked * 150), 600), "cards/cardBack.png")
        image.draw(win)
    else:
        image = Image(Point(200 + ((card_picked - 5) * 150), 400), "cards/cardBack.png")
        image.draw(win)


def flip_cards(win, status, card_images, cards, current_cards):
    """
    To receive two mouse clicks on cards and validate the match
    :param win: window
    :param status: status text bar
    :param card_images: list of image objects
    :param cards: list of int
    :param current_cards: current status of cards
    :return: matched or not (Boolean)
    """

    matching_cards = []

    while len(matching_cards) < 2: # always awaiting the second click
        card_picked = pick_card(win, card_images)

        if card_picked < 10:
            uncover_card(win, card_picked, cards)
            matching_cards.append(card_picked)
        else:  # no card picked
            pass

    match = cards[matching_cards[0]] == cards[matching_cards[1]] and matching_cards[0] != matching_cards[1]

    if not match:
        # click to continue
        status.undraw()
        status.setText("Not a match! Click to continue.")
        status.draw(win)
        win.getMouse()

        # cover the cards
        card_images[matching_cards[0]].undraw()
        cover_card(win, matching_cards[0])
        card_images[matching_cards[1]].undraw()
        cover_card(win, matching_cards[1])
    else:
        status.undraw()
        status.setText("A match! Keep going!")
        status.draw(win)
        current_cards[matching_cards[0]] = 1
        current_cards[matching_cards[1]] = 1

    return match


def is_all_matched(current_cards):
    """
    check if all cards matched
    :param current_cards: current status (list of int)
    :return: all matched or not (Boolean)
    """
    all_matched = True
    for card in current_cards:
        if card < 0:
            all_matched = False
            break
    return all_matched


def main():

    # draw background
    win = draw_background()

    # setup the game
    card_images = setup(win)

    # status bar
    status = Text(Point(500, 700), "READY")
    status.draw(win)

    # bottom bar
    num_matched = Text(Point(200, 50), "Num Matched: 0")
    num_matched.draw(win)
    num_turn = Text(Point(600, 50), "Num Turn: 0")
    num_turn.draw(win)

    # cards in play
    current_cards = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]  # -1 represents covered status

    # shuffle cards
    cards = shuffle_cards()

    finish = False
    turn = 0
    match = 0
    while not finish:
        turn += 1
        num_turn.undraw()
        num_turn.setText("Num Turn: %d" % turn)
        num_turn.draw(win)
        matched = flip_cards(win, status, card_images, cards, current_cards)

        if matched:
            match += 1
            num_matched.undraw()
            num_matched.setText("Num Matched: %d" % match)
            num_matched.draw(win)

            if is_all_matched(current_cards):
                status.undraw()
                status = Text(Point(500, 500), "ALL MATCHED!!!")
                status.setSize(36)
                status.setTextColor("red")
                status.draw(win)
                finish = True

    win.getMouse()
    win.close()


main()
