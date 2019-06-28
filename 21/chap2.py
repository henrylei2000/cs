
# experiments for variable and type print
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
print(1,000,000)


# test True and False keywords
classes = 5
true = 3
print(True)
x = False
if(x):
    print(x)
print(1)
x = 2
print(x)
print(1 + 1)
cookies = 15
print(cookies/4)
print(cookies//4)
print(99.0/100)
print(15.0/4)
fruit = "banana"
baked_good = " nut bread"
print(fruit + baked_good)
print('fun' * 3)

name = input("Please enter your name: ")
print("Hi " + name + ", nice to meet you!")

age = input("please enter your age: ")
if int(age) >= 18:
    print("You're such a great young person!")
else:
    print("You're too young to play the game!")

print(age)



print(17 + 3)
#compute the percentage of the hour that has elapsed
#percentage = (minute * 100) // 60 #caution: integer division
for name in ["Alice", "Bjorn", "Cayman", "Duanphen", "esfir", "farah"]:
    print("I know " + name + ".")
    print("%s is a friend of mine." % (name))
print("Those are the people I know.")
