def question(x, y):
    output = ((x**2 * x**4) / (y**(-1) * y**(-3))) ** (-2)
    return output


def my_answer(x, y):
    output = (1 / (x**12 * y**8))
    return output


def stupid_answer(x, y):
    output = (y**8 / x**12)
    return output


def check_answer():
    """
     >>> stupid_answer(2 ,3) == question(2, 3)
     False
     >>> my_answer(2, 3) == question(2, 3)
     True
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()

