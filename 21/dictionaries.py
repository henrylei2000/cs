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
