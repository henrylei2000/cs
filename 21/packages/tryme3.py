def one_line():
    print("")


def three_lines():
    one_line()
    one_line()
    one_line()


def nine_lines():
    three_lines()
    three_lines()
    three_lines()


nine_lines()


def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    one_line()


clear_screen() # function call must occur after its definition


def cat_n_times(s, n):
    print(s * n)


cat_n_times("Spam", 7)


