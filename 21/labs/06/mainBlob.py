"""
Program: mainBlob.py

This program uses the functions in blobillism.py to create a drawing
application.

Henry Lei
03/01/2020
"""

from blobillism import *

def main():

    win = GraphWin("Blobillist Masterpiece by Henry Lei", 500, 500)
    win.setCoords(0, 0, 1, 1) # left-bottom as 0, 0

    # canvas section
    canvas = makeColorButton(win, 0, 0.2, 1, 1, "grey")

    # control section
    # color palette
    rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    palette = []
    width = 0.07  # 0.07 * 7 = 0.49
    height = 0.2  # one fifth
    for i in range(len(rainbow)):
        palette.append(makeColorButton(win, width * i, 0, width * (i + 1), height, rainbow[i]))

    # size control
    size_plus = makeTextButton(win, 0.49, 0.13, 0.75, 0.2, "size+")
    size_minus = makeTextButton(win, 0.49, 0.07, 0.75, 0.13, "size-")

    # quit control
    quit_button = makeTextButton(win, 0.49, 0, 0.75, 0.07, "quit")  # "quit" button

    # example blob
    panel = makeColorButton(win, 0.75, 0, 1, 0.2, "white")  # example blob
    panel_center = Point(0.875, 0.1)

    # start drawing!

    blob_color = "red"  # default color
    blob_radius = 0.03  # default size
    blob_active = makeCircle(win, panel_center, blob_radius, blob_color)  # default blob

    quit = False
    while not quit:
        click = win.getMouse()
        if clickInButton(click, quit_button):  # quit?
            quit = True
            print("Quit...")
        elif clickInButton(click, canvas):  # draw!
            if click.getY() - blob_radius > height:
                makeCircle(win, click, blob_radius, blob_color)
                print("Drawing...")
            else:
                print("Too close to the control section!")
        elif clickInButton(click, size_plus):  # size+
            blob_radius += 0.01
            if blob_radius >= 0.1:
                blob_radius = 0.03
            blob_active.undraw()
            blob_active = makeCircle(win, panel_center, blob_radius, blob_color)
            print("Size increased.")
        elif clickInButton(click, size_minus):  # size-
            if blob_radius < 0.01:
                blob_radius = 0.03
            blob_radius -= 0.01
            blob_active.undraw()
            blob_active = makeCircle(win, panel_center, blob_radius, blob_color)
            print("Size decreased.")
        else:  # color palette
            for i in range(len(rainbow)):
                if clickInButton(click, palette[i]):
                    blob_color = rainbow[i]
                    blob_active.undraw()
                    blob_active = makeCircle(win, panel_center, blob_radius, blob_color)
                    print(blob_color, "selected.")


main()
