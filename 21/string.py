"""
strings
"""


fruit = "banana"
letter = fruit[0]
print(letter)

print(len(fruit))


def last_character(s):
    length = len(s)
    last = s[length - 1]
    return last


print(last_character('test'))

print(int('10'))
print(bool(""))


for index in range(len(fruit)):
    letter = fruit[index]
    print(letter)


print("while loop output -----")

it = 0
while it < len(fruit):
    print(fruit[it])
    it += 1

for c in fruit:
    print(c)


prefixes = "JKLMNOPQ"
suffix = "ish preferred name"

preferred_name = "henry"

print("dear " + preferred_name[:])

if "1" < "":
    print("banana comes before zebra")
else:
    print("the latter comes before the former")


def remove_vowels(s):
    vowels = "aeiouAEIOU"
    s_without_vowels = ""
    for l in s:
        if l not in vowels:
            s_without_vowels += l
    return s_without_vowels


def find(strng, ch):
    index = 0
    while index < len(strng):
        if strng[index] == ch:
            return index
        index += 1
    return -1


fruit = "banana"


def count(bigstring, ch='a'):
    count = 0
    for char in bigstring:
        if char == ch:
            count += 1
    return count


print(count(fruit))

print(remove_vowels("Henry"))


for letter in prefixes:
    print(letter + suffix)

s = "Peter, Paul, and Mary"
print(s[0:446])


print('%(whatever)s has %(number)03d quote types.' % {'whatever': "Python", "number": 2})

print('%s' % "My name is...")
print('%30s' % "My name is...")

i = 1
print("i\ti**2\ti**3\ti**5\t\ti**10\ti**20")
while i <= 10:
    print("%d\t%6s\t%8d\t%8d\t%d\t%d" % (i, i**2, i**3, i**5, i**10, i**20))
    i += 1