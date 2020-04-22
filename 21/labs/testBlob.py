"""
Program: testBlob.py

This program is used to debug the functions within blobillism.py
"""

from blobillism import *

def main():
    # Add your testing code here
    win = GraphWin("test canvas", 500, 500)
    win.setCoords(0, 0, 1, 1)

    center = Point(0.5, 0.5)
    circle = makeCircle(win, center, 0.2, "green")

    win.getMouse()
    win.close() 



main()
