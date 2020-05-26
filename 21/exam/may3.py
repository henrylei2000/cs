"""Practice for recursion and classes"""

from random import *

def rblastoff(n):
    """
    start at a integer n and print downwards to n
    :param n:
        (int) value to be counted
    :return:
    """
    if n == 0:
        print("blastoff!")  # base case and exit
    else:
        print(n)
        rblastoff((n - 1))


def headsinflips(n):
    """
    purpose: for a given number of coin tosses, return the number of heads
    param:
        (int) number of times coin is tossed
    :return (int): number of heads
    """
    num_heads = 0

    if n == 0:
        return num_heads
    else:
        if randrange(2) == 0:  # heads
            # recursive accumulator pattern
            num_heads += 1 + headsinflips((n - 1))
        else:  # tails
            num_heads += headsinflips((n - 1))

    return num_heads

def fixlistrecursive(list, LB, UB):
    """
    purpose: built a filtered list with values within interval
    params:
        (list)
        (int)
        (int)
    :return (list);
    """
    filtered = []

    if len(list) == 0:
        return filtered
    else:
        if LB <= list[0] <= UB:
            # recursively accumulating a list
            filtered += [list[0]] + fixlistrecursive(list[1:], LB, UB)
        else:
            filtered += fixlistrecursive(list[1:], LB, UB)

        return filtered

def fixlistiterative(L, LB, UB):
    """
    1. split and combine the list
    2. filter with LB and UB
    :param list:
    :param LB:
    :param UB:
    :return (list):
    """
    filtered = []
    for item in L:
        if LB <= item <= UB:
            filtered.append(item)

    return filtered

def main():
    # rblastoff(10)
    print(headsinflips(100))
    print(fixlistrecursive([3, 5, 7, 50, 678], 0, 1000))
    print(fixlistiterative([3, 5, 7, 50, 678], 20, 1000))

main()
