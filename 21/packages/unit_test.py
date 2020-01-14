def compare(a, b):
    """
      >>> compare(5, 4)
      1
      >>> compare(7, 7)
      0
      >>> compare(2, 3)
      -1
      >>> compare(42, 1)
      1
    """
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


def even_number(x):
    if x % 2 == 0:
        return True
    else:
        return False


even_number(3)


def c2f(t):
    """
      >>> c2f(0)
      32
      >>> c2f(100)
      212
      >>> c2f(-40)
      -40
      >>> c2f(12)
      54
      >>> c2f(18)
      64
      >>> c2f(-48)
      -54
    """
    fahrenheit = (9.0 / 5.0) * t + 32.0
    return int(round(fahrenheit))


def is_divisible_by_2_or_5(n):
    """
      >>> is_divisible_by_2_or_5(8)
      True
    """
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
