from decimal import *


def e_at_step(i):
    return (Decimal(1) + Decimal(1.0)/Decimal(i))**Decimal(i)


def test():
    print('calculate e...')
    i = 1
    while e_at_step(i + 1) - e_at_step(i) > 0.000000001:
        i = i + 1

    print("at step", i, "we get", e_at_step(i))


if __name__ == '__main__':
    test()
