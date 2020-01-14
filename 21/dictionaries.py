d = {'a': 1, "b": 2}
print(d.keys())
print(d.items())

alias = d
copy = d.copy()


s = 'string s'

a = s

b = 'string s'

def change_string(s):
    s = 'another one'
    print(s)

change_string(a)

print(a)

t1 = 2, 3

t2 = t1 # alias
t3 = 2, 3

print(t1 is t2)
print(t1 is t3)

print(a is s)
print(s is b)


print(alias is d)
print(copy is d)
print(alias == d)
print(copy == d)

matrix = [[0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 2, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 3, 0]]

eng2fr = {}
eng2fr["one"]="un"
eng2fr["two"]="deux"
print(eng2fr)

eng2fr = {"one": "un", "two": "deux", "three": "trois"}
print(eng2fr["two"])

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print(inventory)

del inventory["pears"]
print(inventory)

inventory["pears"] = 0
print(inventory)

print(len(inventory))

print(list(eng2fr.keys()))
print(list(eng2fr.values()))
print(list(eng2fr.items()))

print("one" in eng2fr)


#aliasing and copying
opposites = {"up": "down", "skinny": "fat"}
alias = opposites
copy = opposites.copy()

alias["skinny"] = "obese"
print(opposites["skinny"])
print(copy["skinny"])

letter_counts = {}
for letter in "The Mississippi River is three thousand seven hundred seventy eight kilometers long":
    letter_counts[letter.lower()] = letter_counts.get(letter, 0) + 1

print(letter_counts)
del letter_counts[" "]
print(letter_counts)

letter_items = list(letter_counts.items())
letter_items.sort()
print(letter_items)
print(str(letter_items))
