"""
 To draw a frog face with grpahics module and objects concept
 Henry Lei
 Spring 2020
"""

from graphics import *                                # import everything from the graphics library


def draw_face(x, y, window):
    # face
    o = Oval(Point(x - 49, y - 25), Point(x + 49, y + 25))
    o.setWidth(0)
    o.setFill(color_rgb(0, 200, 0))
    o.draw(window)

    # eyes
    c = Circle(Point(x - 25, y + 25), 13)
    c.setWidth(0)
    c.setFill(color_rgb(0, 200, 0))
    c.draw(window)
    w = Circle(Point(x - 25, y + 25), 8)
    w.setWidth(0)
    w.setFill(color_rgb(255, 255, 255))
    w.draw(window)
    b = Circle(Point(x - 25, y + 25), 5)
    b.setFill(color_rgb(0, 0, 0))
    b.draw(window)

    p = Polygon(w.getCenter(), Point(w.getCenter().getX() - 6, w.getCenter().getY()), Point(w.getCenter().getX() - 6, w.getCenter().getY() + 2))
    p.setWidth(0)
    p.setFill(color_rgb(255, 255, 255))
    p.setOutline(color_rgb(255, 255, 255))
    p.draw(window)

    c2 = c.clone()
    c2.move(50, 0)
    c2.draw(window)
    w2 = w.clone()
    w2.move(50, 0)
    w2.draw(window)
    b2 = b.clone()
    b2.move(50, 0)
    b2.draw(window)

    p2 = p.clone()
    p2.move(50, 0)
    p2.draw(window)
    #nose
    n = Circle(Point(x - 3, y + 10), 2)
    n.setWidth(0)
    n.setFill(color_rgb(150, 250, 150))
    n.draw(window)
    n2 = n.clone()
    n2.move(6, 0)
    n2.draw(window)
    #mouth
    l = Line(Point(x - 49, y), Point(x + 49, y))
    l.setWidth(3)
    l.setFill(color_rgb(80, 80, 80))
    l.draw(window)
    #tounge
    r = Polygon(Point(80, 50), Point(83, 52), Point(90, 52), Point(87, 50))
    r.setOutline(color_rgb(200, 0, 0))
    r.setFill(color_rgb(200, 0, 0))
    r.draw(window)

def main():
    win_w = 800
    win_h = 800
    win = GraphWin("frog", win_w, win_h)                     # make a graphics window
    win.setCoords(0, 0, 100, 100)
    win.setBackground(color_rgb(150, 200, 150))
    draw_face(50, 50, win)
    win.getMouse()  # keep the window open until the mouse is clicked
    win.close()  # close the graphics window (which would happen anyway
    # since the program ends here, but it is better to be
    # explicit and close it).

if __name__ == '__main__':
    main()
