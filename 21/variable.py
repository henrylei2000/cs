"""
experiments for variable and type print
"""

import sys

print(4)
print("hello, world!")
message = "What's up, Doc?"
n = 17
pi = 3.14159
print(type(message))
print(type(n))
print(type(pi))
print(message)
print(n)
print(pi)

print(type("hello, world!"))
print(type(17))

# single quote vs double quote
print("tom's friend")
print('tom\'s friend')

# number format
print(1, 000, 000)

# test True and False keywords
classes = 5
true = 3
print(True)
x = False
if (x):
    print(x)
print(1)
x = 2
print(x)
print(1 + 1)
cookies = 15
print(cookies / 4)
print(cookies // 4)
print(99.0 / 100)
print(15.0 / 4)
fruit = "banana"
baked_good = " nut bread"
print(fruit + baked_good)
print('fun' * 3)


def io():
    """
    incoming_list and output
    :return:
    """
    input_name = input("Please enter your name: ")
    print("Hi " + input_name + ", nice to meet you!")
    age = input("please enter your age: ")
    if int(age) >= 18:
        print("You're such a great young person!")
    else:
        print("You're too young to play the game!")
    print(age)
    n = input("Please enter your name: ")
    print("Hello,", n)


io()

str_seconds = input("Please enter the number of seconds you wish to convert")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60
print(17 + 3)
# compute the percentage of the hour that has elapsed
# percentage = (minute * 100) // 60 #caution: integer division

# for loop
for name in ["Alice", "Bjorn", "Cayman", "Duanphen", "esfir", "farah"]:
    print("I know " + name + ".")
    print("%s is a friend of mine." % (name))
print("Those are the people I know.")

# the range function
# script mode - no evaluation & print
range(0, 10)


print(sys.version_info)
print(type(range(0, 10)))
print(list(range(0, 10)))  # convert to a list
print(list(range(2, 3)))  # convert to a list, includes 2 but not 3
for number in range(0, 10):
    print(number)
print(list(range(5)))
print(list(range(0, 20, 2)))

# range and int
total_str = input("How many numbers should I print? ")
total = int(total_str)
for number in range(0, total):
    print(number)

start = int(input("Which number should I print first? "))
stop = int(input("Which number should make the loop stop? "))
for number in range(start, stop):
    print(number)

# Accumulators
last_number_str = input("Sum up to what number? ")
last_number = int(last_number_str)
total = 0  # this is our accumulator
for number in list(range(0, last_number + 1)):
    total = total + number
print("The sum of those numbers is: %d" % (total))  # +1 to include last_number itself

# REPL mode; command line mode; Python Prompt + Evaluation and print