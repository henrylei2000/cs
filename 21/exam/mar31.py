# for a given list of list
# sum item in list
# find item with greatest sum


def sum_list(list):
    """

    :param list: single dimension list
    :return (int):
    """
    total = 0

    for item in list:
        total += item

    return total


def find_greatest(list):
    """

    :param list: 2 dimension list
    :return (int):
    """
    max = sum_list(list[0])
    max_index = 0

    for i in range(len(list)):
        sum = sum_list(list[i])
        if sum > max:
            max = sum
            max_index = i

    return max_index


def main():
    list = [[11, 2, 3], [2, 3, 3], [1, 3, 3]]
    result = find_greatest(list)
    print(result)

main()