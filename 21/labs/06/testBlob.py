"""
Program: testBlob.py

This program is used to debug the functions within blobillism.py

Henry Lei
03/01/2020
"""

from blobillism import *

def main():

    win = GraphWin("Testing Canvas", 500, 500)
    win.setCoords(0, 0, 1, 1) # left-bottom as 0, 0

    x = 0.05 # starting x
    for i in range(10):
        center = Point(x + i * 0.1, 0.5)
        circle = makeCircle(win, center, 0.05, "green")

    testing_button = makeTextButton(win, 0, 0, 1, 0.1, "testing") # "testing" button

    quit_button = makeTextButton(win, 0, 0.9, 0.5, 1, "quit") # "quit" button

    blue_button = makeColorButton(win, 0.5, 0.9, 1, 1, "blue") # blue button

    quit = False
    while not quit:
        click = win.getMouse()
        if clickInButton(click, quit_button): # quit?
            print("Quit pressed...")
            quit = True
        elif clickInButton(click, testing_button): # testing?
            print("Testing pressed")
        elif clickInButton(click, blue_button): # blue?
            print("Blue pressed")
        else:
            print("Clicked somewhere else...")


main()
