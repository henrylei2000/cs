"""
Slow Program
Henry Lei
Spring 2020
"""


def convert(a):
    a[0] = 0
    a.append(143)
    return a


def convert_string(x):
    x = "lei"
    return x


def convert_int(y):
    y = y + 1
    return y


def xmain():
    nums = [12, -4]
    s = "henry"
    y = 6
    b = convert(nums)
    c = convert_string(s)
    d = convert_int(y)

    print(b)
    print(nums)
    print(c)
    print(s)
    print(d)
    print(y)


def divide(x, y):
    print("in function...")
    # Q3
    return x / y


def main():
    a = 17
    b = 5
    print("in main...")
    result = divide(a, b)
    print(result)


if __name__ == "__main__":
    main()
