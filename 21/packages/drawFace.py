"""
 This is the program to draw an animal face with graphics module
 Henry Lei
 Spring 2020
"""

from graphics import *                                # import everything from the graphics library


def draw_face(x, y, window):
    """
     To draw a face on the window, center point is x, y
    """
    # face
    face = Oval(Point(20, 40), Point(80, 60))
    face.setFill(color_rgb(100, 250, 100))
    face.setWidth(0)
    face.draw(window)
    pass


def main():
    win_w = 800
    win_h = 800
    win = GraphWin("face", win_w, win_h)                    # make a graphics window
    win.setBackground(color_rgb(100, 150, 100))
    win.setCoords(0, 0, 100, 100)
    draw_face(50, 50, win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
