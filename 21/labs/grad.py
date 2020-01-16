"""
 This is the first full program
 Henry Lei
 Spring 2020
"""


def main():
    current_year = input("Enter the current year: ")
    graduation_year = input("Enter your graduation year: ")
    gap = int(graduation_year) - int(current_year)
    print("You have %d year(s) until graduation." % gap)


main()
