def question(x, y):
    output = ((x**2 * x**4) / (y**(-1) * y**(-3))) ** (-2)
    return output


def my_answer(x, y):
    output = (1 / (x**12 * y**8))
    return output


def stupid_answer(x, y):
    output = (y**8 / x**12)
    return output


if my_answer(2, 3) == question(2, 3):
    print("I'm right!")
else:
    print("I'm wrong.")

if stupid_answer(2, 3) == question(2, 3):
    print("Stupid sometimes could be right!")
else:
    print("Stupid is stupid!!!")

