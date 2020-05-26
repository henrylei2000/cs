def r_print_list(L):
    if len(L) == 0:
        return
    print(L[0])
    r_print_list(L[1:len(L)])  # change parameter


def get_int_input():
    finish = False
    while not finish:
        i = input("enter your integer: ")
        if i.isdigit():
            finish = True
    return int(i)


def get_int():
    i = input("enter your integer: ")
    if i.isdigit():
        return int(i)
    get_int()


def main():
    nums = [1, 2, 4, 5]
    r_print_list(nums)

    print(get_int_input())
    result = get_int()
    print(result)


main()