from cs.graphics import *                                # import everything from the graphics library


def draw_house(x, y, window):
    house = Rectangle(Point(x + 20, y + 580), Point(x + 120, y + 480))
    house.setFill(color_rgb(0, 0, 255)) # the house
    door = Rectangle(Point(x + 55, y + 580), Point(x + 85, y + 530))      # the door
    door.setFill(color_rgb(0, 128, 0))
    l_window = Rectangle(Point(x + 40, y + 520), Point(x + 60, y + 500))
    l_window.setFill(color_rgb(255, 255, 0)) # the left window
    r_window = Rectangle(Point(x + 80, y + 520), Point(x + 100, y + 500)) # the right window
    r_window.setFill(color_rgb(255, 255, 0))
    roof = Polygon(Point(x + 20, y + 480), Point(x + 70, y + 440), Point(x + 120, y + 480))
    roof.setFill(color_rgb(255, 0, 0))
    house.draw(window)   # draw each piece on the graphics window
    door.draw(window)
    l_window.draw(window)
    r_window.draw(window)
    roof.draw(window)


def main():
    win_w = 900
    win_h = 600

    win = GraphWin("house", win_w, win_h)                     # make a graphics window
    win.setBackground(color_rgb(0, 0, 0))

    # x_start = 100
    y_start = 0
    x_gap = 225
    y_gap = 150
    house_w = 100

    center = win_w / 2
    x_start = center - (house_w / 2 + x_gap)
    bottom = 3
    while bottom > 0:
        bottom -= 1
        draw_house(x_start + x_gap * bottom, y_start, win)

    x_start = center - (x_gap + house_w) / 2
    middle = 2
    while middle > 0:
        middle -= 1
        draw_house(x_start + x_gap * middle, y_start - y_gap, win)

    x_start = center - house_w / 2

    top = 1
    while top > 0:
        top -= 1
        draw_house(x_start + x_gap * top, y_start - 2 * y_gap, win) #top

    win.getMouse()  # keep the window open until the mouse is clicked
    win.close()  # close the graphics window (which would happen anyway
    # since the program ends here, but it is better to be
    # explicit and close it).


if __name__ == '__main__':
    main()
