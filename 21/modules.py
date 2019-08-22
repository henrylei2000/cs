from packages.e import e_at_step
from packages.exponent import *

import mod1
import mod2

s = "henry"
print(s.upper())

print(e_at_step(3))
print(stupid_answer(2, 2))
print(mod1.question)
print(mod2.question)

try:
    myfile = open('packages/test123.dat', 'r')
    # myfile.write("Now is the time. - Henry\n")
    # myfile.write("line one\nline two\nline three\n")
    contents = myfile.read()
    print(contents)
    myfile.close()
except (FileNotFoundError, DivisionByZero):
    print("no file.")


print(ord('a'))

print(chr(97))
