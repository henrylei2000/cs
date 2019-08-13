from graphics import *
from time import sleep
from random import randint

"""
Step 1
"""


def ground():
    window = GraphWin("Catch", 800, 600)
    window.setBackground("yellow")
    return window

"""
Step 2
"""


def ball():
    window = ground()

    ball_x = 200
    ball_y = 300
    center = Point(ball_x, ball_y)
    ball = Circle(center, 10)
    ball.setFill("black")
    ball.draw(window)

    mitt_x = 760
    mitt_y = 300
    mitt = Circle(Point(mitt_x, mitt_y), 20)

    mitt.draw(window)
    window.getMouse()
    dy = randint(-5, 5)
    while ball_x < 760:
        ball.move(10, dy)
        ball_x += 10
    window.getMouse()
    window.close()


"""
Step 3
"""


def mitt():
    window = ground()
    mitt_x = 780
    mitt_y = 300
    mitt = Circle(Point(mitt_x, mitt_y), 20)
    mitt.draw(window)
    window.getMouse()
    window.close()


"""
Step 4
"""


def move():
    window = GraphWin("Catch", 800, 600)
    window.setBackground("yellow")

    ball_x = 200
    ball_y = 300
    center = Point(ball_x, ball_y)
    ball = Circle(center, 10)
    ball.setFill("black")

    ball.draw(window)
    dx = 4
    dy = randint(-4, 4)

    while ball_x < 810:
        if ball_y >= 590 or ball_y <= 10:
            dy *= -1
        ball.move(dx, dy)
        ball_x += dx
        ball_y += dy
        sleep(1/100)

    window.getMouse()
    window.close()


"""
Step 5
"""


def run():
    window = GraphWin("Catch", 800, 600)
    window.setBackground("yellow")

    mitt_x = 760
    mitt_y = 300
    mitt = Circle(Point(mitt_x, mitt_y), 20)

    mitt.draw(window)
    pressed_escape = False  # a flag variable to indicate that Escape was pressed

    while not pressed_escape:
        key_pressed = window.checkKey()
        if key_pressed == 'a' and mitt_y <= 580:
            dy += 5
        elif key_pressed == 's' and mitt_y >= 20:
            dy -= 5
        elif key_pressed == 'Escape':
            pressed_escape = True
        else:
            dy = 0

        mitt.move(0, dy)
        mitt_y += dy

    window.close()



"""
definition of a catch
"""


def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


def collision(x1, y1, x2, y2):
    if distance(x1, y1, x2, y2) < 20:
        return True
    else:
        return False


def play():
    window = GraphWin("Catch", 800, 600)
    window.setBackground("yellow")
    diamond = Image(Point(350, 250), "../images/diamond.gif")
    diamond.draw(window)
    for number_of_round in range(0, 3):
        ball_x = 10
        ball_y = 300
        ball = Image(Point(ball_x, ball_y), "../images/ball.png")
        dx = 4
        dy = randint(-4, 4)
        ball.draw(window)

        mitt_x = 790
        mitt_y = 300
        mitt_dy = 0
        mitt = Image(Point(mitt_x, mitt_y), "../images/trump-1.png")
        mitt.draw(window)

        # the game is over if the user presses Escape, misses the ball,
        # or catches the ball.

        game_over = False

        while not game_over:
            #move the ball
            if ball_y >= 590 or ball_y < 10:
                dy *= -1
            ball_x += dx
            ball_y += dy
            ball.move(dx, dy)
            if ball_x > 800:
                mitt.undraw()
                game_over = True  # the ball went past the paddle

            #check the mitt
            key_pressed = window.checkKey()
            if key_pressed == 'k' and mitt_y <= 580:
                mitt_dy += 5
            elif key_pressed == 'j' and mitt_y >= 20:
                mitt_dy -= 5
            elif key_pressed == 'Escape':
                game_over = True  # the user pressed Escape
            else:
                mitt_dy = 0

            if not game_over:
              mitt_y += mitt_dy
              mitt.move(0, mitt_dy)

              #check if we caught the ball
              if collision(ball_x, ball_y, mitt_x, mitt_y):
                  mitt = Image(Point(mitt_x, mitt_y), "../images/trump-3.png")
                  mitt.draw(window)
                  game_over = True
              else:
                  sleep(1/120)

    window.getMouse()
    window.close()

play()

def decorate():

    # mitt = Image(Point(mitt_x, mitt_y), "trump-1.png")
    # ball = Image(Point(ball_x, ball_y), "ball.png")
    pass

