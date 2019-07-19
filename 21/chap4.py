# conditionals: modulus operator
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
x == y # x equals y
x != y # x is not equal to y
x > y # greater than
x < y # less than
x >= y # greater than or equal to
x <= y # less than or equal to

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
        print(" %s is even" % (x))
    else:
        print(" %s is odd" % (x))
        print_parity(18)

# chained conditionals
if x < y:
    print(" %s is less than %s" % (x, y))
elif x > y:
    print(" %s is greater than %s" % (x, y))
else:
    print(" %s and %s are equal" % (x, y))

def function_a():
    pass

def function_b():
    pass

def function_c():
    pass

choice = 'a'
if choice == 'a':
    function_a()
elif choice == "b":
    function_b()
elif choice == "c":
    function_c()
else:
    print("Invalid choice.")

# Graphics
from graphics import *

window = GraphWin("graphics!", 700, 500)

window.setBackground(color_rgb(130, 0, 230))

circle = Circle(Point(200, 300), 60)
circle.setFill(color_rgb(230, 0, 130))
line = Line(Point(100, 100), Point(580, 300))
box = Rectangle(Point(400, 150), Point(520, 50))

circle.draw(window)
line.draw(window)
box.draw(window)

#window.getMouse()
time.sleep(1.4)
window.close()

print("after the graphic call")

# exercises
print(5 % 2)
print(5 % 2)
print(9 % 5)
print(15 % 12)
print(12 % 15)
print(6 % 6)
print(0 % 7)
print(7 % 1)

# wrap function
def compare(x, y):
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
expression = input("Enter a boolean expression in two variables, p and q: ")

print(" p   q   %s" % (expression))
length = len(" p   q   %s" % (expression))
print(length*"=")

for p in True, False:
    for q in True, False:
        print("%7s %7s %7s" % (p, q, eval(expression))) # no hypen between % and 7
