"""
conditionals: modulus operator
"""
from packages.graphics import *
from packages.truth_table import *

quotient = 7 // 3
print(quotient)
remainder = 7 % 3
print(remainder)

# boolean values and expressions
print(type(True))
print(type(True)) # capitalization matters
print(5 == 5)
5 == 6
# comparison operators
x = 1
y = 1
x == y  # x equals y
x != y  # x is not equal to y
x > y  # greater than
x < y  # less than
x >= y  # greater than or equal to
x <= y  # less than or equal to

# conditional execution
if x > 0:
    print('%s is positive' % (x))

# alternative execution
if x % 2 == 0:
    print(" %s is even" % (x))
else:
    print(" %s is odd" % (x)) # branches in the flow of execution


def print_parity(x):
    if x % 2 == 0:
        print(" %s is even" % x)
    else:
        print(" %s is odd" % x)
        print_parity(18)


"""
chained conditionals 
"""
if x < y:
    print(" %s is less than %s" % (x, y))
elif x > y:
    print(" %s is greater than %s" % (x, y))
else:
    print(" %s and %s are equal" % (x, y))




"""
wrap function
"""


def compare(x, y):
    """
     >>> compare(2, 3)
      2 is less than 3
     >>> compare(5, 1)
      5 is greater than 1
    """
    if x < y:
        print(" %s is less than %s" % (x, y))
    elif x > y:
        print(" %s is greater than %s" % (x, y))
    else:
        print(" %s and %s are equal" % (x, y))

compare(1, 2)
compare(2, 1)
compare(2, 2)

# boolean expressions
# expression = incoming_list("Enter a boolean expression in two variables, any_other_point and q: ")


for expression in "any_other_point or q", "not(any_other_point or q)", "any_other_point and q", "not(any_other_point and q)", "not(any_other_point) or not(q)", "not(any_other_point) and not(q)":
    print("\n")
    truth_table(expression)

for exp in 'True and True', 'True or False', 'True and False', 'not(False) and True', 'True or 7', 'False or 7', \
           'True and 0', 'False or 8', '"true" and False', '"happy" or "sad"', '"" and "sad"', '"happy" and ""':
    print(exp)
    if eval(exp):
        print("true")
    else:
        print("false")
    print('\n')




"""
Graphics
"""
window = GraphWin("graphics!", 700, 500)
window.setBackground(color_rgb(130, 0, 230))

circle = Circle(Point(200, 300), 60)
circle.setFill(color_rgb(230, 0, 130))
line = Line(Point(100, 100), Point(580, 300))
box = Rectangle(Point(400, 150), Point(520, 50))

circle.draw(window)
line.draw(window)
box.draw(window)

# window.getMouse()
time.sleep(.3)
window.close()

print("after the graphic call")
