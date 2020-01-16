"""
 This is the string practice program
 Henry Lei
 Spring 2020
"""


def task():
    print("Task 1")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    print("Welcome " + first_name + " " + last_name)

    print("Task 2")
    print("There are %d characters in your name" % len(first_name + last_name))

    print("Task 3")
    print("Initials: " + first_name[0] + "." + last_name[0] + ".")

    print("BONUS")
    print("Last initials: " + first_name[len(first_name) - 1] + "." + last_name[len(last_name) - 1] + ".")

    print("Task 4")
    for c in first_name:
        print(c)

task()
