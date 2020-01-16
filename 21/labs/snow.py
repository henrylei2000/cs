"""
 This is the condition practice program
 Henry Lei
 Spring 2020
"""


def snow_depth():
    initial_depth = float(input("Enter today's snow depth in inches: "))
    track_days = int(input("Enter number of days to track: "))

    for day in range(track_days):
        print("Day " + str(day + 1) + ":")
        melting_depth = float(input("Amount of melting in inches: "))
        new_depth = float(input("Amount of new snow in inches: "))

        current_depth = initial_depth - melting_depth + new_depth
        # validation for unreasonable user input (negative depth)
        if current_depth < 0:
            current_depth = 0
        print("New snow depth: %f inches" % current_depth)


snow_depth()
