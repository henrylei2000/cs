# Function definitions and order of execution
def urmom(arg):
    pass
def new_line():
    print("")
print("First Line.")
new_line()
print("Second Line.")
print("First Line.")
new_line()
new_line()
new_line()
print("Second Line.")
def three_lines():
    new_line()
    new_line()
    new_line()
print("First Line.")
three_lines()
print("Second Line.")

# built-in python functions
abs(5)
abs(-5)
pow(2, 3)
pow(7, 4)
max(7, 11)
max(4, 1, 17, 2, 12)
max(3 * 11, 5**3 ,512-9, 1024**0)

def print_twice(param):
    print(param)
    print(param)

from chap3 import *

print_twice("Spam")
print_twice(5)
print_twice(3.14)
print_twice("spam" * 4)

# Composition
print_twice(abs(-7))
print_twice(max(3, 1, abs(-11), 7))
sval = "Maddie, the big boy."
print_twice(sval)

# local variable
def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)
chant1 = "Pie Jesu domine, "
chant2 = "Dona eis requiem."
cat_twice(chant1, chant2)

#print(cat) # when cat_twice terminates, the variable cat is destroyed

# stack diagrams (hierarchy of function)
def print_twice(param):
    print(param)
    print(param)
#    print(cat)

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

chant1 = "Pie Jesu domine, "
chant2 = "Dona eis requim."
cat_twice(chant1, chant2)
