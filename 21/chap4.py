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
time.sleep(.3)
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
#expression = input("Enter a boolean expression in two variables, p and q: ")


from p_and_q import truth_table
for expression in "p or q", "not(p or q)", "p and q", "not(p and q)", "not(p) or not(q)", "not(p) and not(q)":
    print("\n")
    truth_table(expression)

for exp in 'True and True', 'True or False','True and False','not(False) and True','True or 7','False or 7','True and 0','False or 8','"true" and False','"happy" or "sad"','"" and "sad"','"happy" and ""':
    print(exp)
    if(eval(exp)):
    	print("true")
    else:
    	print("false")
    print('\n')


from ch04e05 import *
dispatch('b')
