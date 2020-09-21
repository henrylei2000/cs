"""
 To draw a frog face with grpahics module and objects concept
 Henry Lei
 Spring 2020
"""

from cs.graphics import *                                # import everything from the graphics library


def main():
    win_w = 600
    win_h = 600
    win = GraphWin("frog", win_w, win_h)
    win.setCoords(0, 0, 100, 100)
    # sky
    win.setBackground(color_rgb(143, 190, 235))
    # green
    green = Rectangle(Point(0,0), Point(100, 40))
    green.setFill(color_rgb(107, 212, 95))
    green.setWidth(0)
    green.draw(win)
    #ground
    ground = Rectangle(Point(0,0), Point(100, 10))
    ground.setFill(color_rgb(10, 10, 10))
    ground.setWidth(0)
    ground.draw(win)

    click_one = win.getMouse()
    # flower
    flower = Circle(click_one, 5)
    flower.setFill(color_rgb(200, 100, 100))
    flower.draw(win)

    click_two = win.getMouse()
    # flower
    line = Line(click_one, click_two)
    line.draw(win)
    flower.undraw()
    flower.draw(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
