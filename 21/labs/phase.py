"""
 This is the condition practice program
 Henry Lei
 Spring 2020
"""


def water_state():
    temp = int(input("Enter a temp in °C: "))
    if temp >= 100:
        print("At %dC, water is a gas" % temp)
    elif temp >= 0:
        print("At %dC, water is a liquid" % temp)
    else:
        print("At %dC, water is a solid" % temp)


water_state()