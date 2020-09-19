
def search(x, list):
    '''
    purpose: given a sorted list, return the index of x in the list
    :param x: (int)
    :param list:
    :return: (Bool) True if item is in list
    '''
    low = 0
    high = len(list) - 1

    while low <= high:

        mid = int((low + high) / 2)
        print("low: %d mid: %d high: %d" % (low, mid, high))
        if x > list[mid]:
            low = mid + 1
        elif x < list[mid]:
            high = mid - 1
        else:
            return mid  # index of integer in list



    return -1


def main():
    nums = [1, 3, 5, 7, 9, 13]
    result = search(0, nums)

    L = ["do", "fa", "la", "mi", "re", "so", "ti"]
    result = search("xu", L)
    print(result)


main()