from decimal import *


def e_at_step(i):
    return (Decimal(1) + Decimal(1.0)/Decimal(i))**Decimal(i)


def test():
    print('calculate e...')
    i = 1
    while e_at_step(i + 1) - e_at_step(i) > 0.000000001:
        i = i + 1

    print("at step", i, "we get", e_at_step(i))


def recursive_e(i):
    try:
        e1 = (Decimal(1) + Decimal(1.0) / Decimal(i)) ** Decimal(i)
        e2 = (Decimal(1) + Decimal(1.0) / Decimal(i + 1)) ** Decimal(i + 1)
        if e2 - e1 < 0.01:
            print("we get %f, %f at %d" % (e1,e2, i))
        else:
            recursive_e(i + 1)
    except DivisionByZero:
        recursive_e(i + 1)



print("========")
recursive_e(0)
print("=======end====")


if __name__ == '__main__':
    test()
