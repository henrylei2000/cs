
print('calculate e...')

from decimal import *

def e(i):
    return (Decimal(1) + Decimal(1.0)/Decimal(i))**Decimal(i)

i = 1

while (e(i+1) - e(i) > 0.000000001):
    i = i + 1

print("at step" , i, "we get", e(i))
