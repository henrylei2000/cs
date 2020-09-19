"""
files: open, read, write, close
"""

import random


def read():
    # Passing "r" opens the file for reading
    file = open("henry.txt", "r")

    for line in file:
        token = line.split(",")
        name = token[0]
        quantity = int(token[1])
        print(name)
        print(quantity)

    file.close()


def write():
    # Passing "w" opens the file for writing
    # Watch out! This will overwrite the file's contents!
    file = open("test.txt", "w")

    for i in range(10):
        # write 10 random scores into test.txt
        score = random.randrange(20, 101)
        file.writelines(str(i) + " student, " + str(score) + "\n")

    file.close()


def average():

    file = open("test.txt", "r")
    count = 0
    total = 0

    for line in file:
        count += 1

        tokens = line.split(",")
        total += int(tokens[1])

    print(count)
    print(total)
    average = total / count

    file.close()
    return average


def main():
    read()
    write()
    answer = average()
    print(answer)


main()