"""
 This is the first full program
 Henry Lei
 Spring 2020
"""
from math import pi, sin, cos, sqrt


def main():
    radius = int(input("Enter the radius of a circle: "))
    area = pi * radius ** 2
    print("The area of a circle of radius %d equals: %f" % (radius, area))


main()