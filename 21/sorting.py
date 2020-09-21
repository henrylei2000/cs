from packages.graphics import *
from random import *


def bubble_sort(array):
    """
       Graphics
       """
    background = color_rgb(0, 161, 241)

    window = GraphWin("graphics!", 700, 500)
    window.setBackground(background)
    window.setCoords(0, 0, 101, 100)

    width = 10
    pace = 1
    rects = []

    for i in range(len(array)):
        point1 = Point(pace + width * i, 0)
        point2 = Point(width * (i + 1), array[i])
        rect = Rectangle(point1, point2)
        rects.append(rect)
        rect.draw(window)
        deactivate(rect)

    print("after the graphic call")

    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            time.sleep(.5)
            activate(rects[j])
            activate(rects[j+1])
            time.sleep(.5)
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                c1 = rects[j].getCenter()
                c2 = rects[j+1].getCenter()
                rects[j].move(c2.getX() - c1.getX(), 0)
                rects[j+1].move(c1.getX() - c2.getX(), 0)
                array[j], array[j + 1] = array[j + 1], array[j]
                rects[j], rects[j + 1] = rects[j + 1], rects[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False
            time.sleep(.5)
            deactivate(rects[j])
            deactivate(rects[j + 1])
        complete(rects[j + 1])
        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        # if already_sorted:
            # break
    complete(rects[0])
    window.getMouse()
    time.sleep(.3)
    window.close()
    return array


def bubble(array):
    """
       Graphics
       """
    background = color_rgb(0, 161, 241)

    window = GraphWin("graphics!", 700, 700)
    window.setBackground(background)
    window.setCoords(0, 0, 100, 100)

    height = 9
    pace = 2
    bubbles = []

    for i in range(len(array)):
        center = Point(50, pace + height * (i+1))
        b = Circle(center, array[i] / 10)
        bubbles.append(b)
        b.draw(window)
        deactivate(b)

    print("after the graphic call")

    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            time.sleep(.5)
            activate(bubbles[j])
            activate(bubbles[j+1])
            time.sleep(.5)
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                c1 = bubbles[j].getCenter()
                c2 = bubbles[j+1].getCenter()
                bubbles[j].move(0, c2.getY() - c1.getY())
                bubbles[j+1].move(0, c1.getY() - c2.getY())
                array[j], array[j + 1] = array[j + 1], array[j]
                bubbles[j], bubbles[j + 1] = bubbles[j + 1], bubbles[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False
            time.sleep(.5)
            deactivate(bubbles[j])
            deactivate(bubbles[j + 1])
        complete(bubbles[j + 1])
        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        # if already_sorted:
            # break
    complete(bubbles[0])
    window.getMouse()
    time.sleep(.3)
    window.close()
    return array


def activate(obj):
    active = color_rgb(246, 83, 20)
    obj.setOutline(active)
    obj.setFill(active)


def deactivate(obj):
    bar = color_rgb(255, 187, 0)
    obj.setOutline(bar)
    obj.setFill(bar)


def complete(obj):
    done = color_rgb(124, 187, 0)
    obj.setOutline(done)
    obj.setFill(done)


def main():
    # Verify it works
    nums = []
    for j in range(10):
        nums.append(randrange(1, 100))
    bubble_sort(nums)
    print(nums)

    bnums = []
    for j in range(10):
        bnums.append(randrange(1, 50))
    bubble(bnums)





main()
