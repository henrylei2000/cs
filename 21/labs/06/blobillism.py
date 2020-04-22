"""
Program: blobillism.py

A library of functions for use in a blob drawing application.

Henry Lei
03/01/2020
"""

from graphics import *


def makeCircle(win, center, radius, color):
    """
    Purpose: draw a circle
    Parameters:
        win(GraphWin): a Graphwin object to draw a circle
        center(Point): the center of the circle
        radius(int): radius of the circle
        color(str): color
    Return: Circle object
    """

    circle = Circle(center, radius)
    circle.setOutline(color) # outline shares the same color
    circle.setFill(color) # backfill color
    circle.draw(win)

    return circle


def makeTextButton(win, xll, yll, xur, yur, label):
    """
    Purpose: draw a rectangle button with a label
    Parameters:
        win(GraphWin): a Graphwin object to draw a button
        xll(int): x coordinate of low-left corner of the button
        yll(int): y coordinate of low-left corner of the button
        xur(int): x coordinate of up-right corner of the button
        yur(int): y coordinate of up-right corner of the button
        label(str): label of the button
    Return: Rectangle object
    """
    pll = Point(xll, yll)
    pur = Point(xur, yur)
    rectangle = Rectangle(pll, pur)
    rectangle.setFill("black")
    rectangle.setOutline("white")
    rectangle.draw(win)

    # calculate the coordinates for label
    x = xll + (xur - xll) / 2
    y = yll + (yur - yll) / 2
    label_center = Point(x, y)
    label = Text(label_center, label)
    label.setTextColor("white")
    label.draw(win)

    return rectangle


def makeColorButton(win, xll, yll, xur, yur, color):
    """
    Purpose: draw a rectangle button with a color
    Parameters:
        win(GraphWin): a Graphwin object to draw a button
        xll(int): x coordinate of low-left corner of the button
        yll(int): y coordinate of low-left corner of the button
        xur(int): x coordinate of up-right corner of the button
        yur(int): y coordinate of up-right corner of the button
        color(str): the color of the button
    Return: Rectangle object
    """
    pll = Point(xll, yll)
    pur = Point(xur, yur)
    rectangle = Rectangle(pll, pur)
    rectangle.setFill(color)
    rectangle.setOutline("white")
    rectangle.draw(win)

    return rectangle


def clickInButton(point, button):
    """
    Purpose: check if a mouse click is in a given button
    Parameters:
        point(Point): the coords of a mouse click
        button(Rectangle): the given button
    return: boolean
    """
    is_in_between = False

    # where is the mouse click
    x = point.getX()
    y = point.getY()

    # where are the coords of a button rectangle
    ll = button.getP1()
    ur = button.getP2()

    xll = ll.getX()
    yll = ll.getY()
    xur = ur.getX()
    yur = ur.getY()

    # when a click is in a the button
    x_is_in_between = (x >= xll and x <= xur)
    y_is_in_between = (y >= yll and y <= yur)

    is_in_between = x_is_in_between and y_is_in_between

    return is_in_between
