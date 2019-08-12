from graphics import *
from random import randint
from time import sleep

def main():
    window = GraphWin("Catch", 800, 600)
    window.setBackground("yellow")

    player_score = 0
    comp_score = 0

    player = Text(Point(110, 570), "Player: %d Points" % player_score)
    player.setSize(24)
    player.draw(window)
    computer = Text(Point(640, 570), "Computer: %d Points" % comp_score)
    computer.setSize(24)
    computer.draw(window)

    while player_score < 5 and comp_score < 5:
        sleep(1)
        winner = randint(0, 1)
        if winner == 1:
            player_score += 1
            player.setText("Player: %d Points" % (player_score))
        else:
            comp_score += 1
            computer.setText("Computer: %d Points" % (comp_score))

    if player_score == 5:
        result_text = "Player Wins!"
    else:
        result_text = "Computer Wins!"

    result = Text(Point(340, 290), result_text)
    result.setSize(32)
    result.draw(window)

    window.getMouse()
    window.close()

main()