
def test_nested_loop():
    for i in range(2):
        for j in range(3):
            print("i = %d j = %d" % (i, j))


def smallest_of_index(L):
    """
    Inputs:  A list of values
    Returns: The index of the smallest item in the list, -1 if the list
    is empty
    Purpose: To find the location of the smallest item in the given list
    """
    # complete this function
    if len(L) == 0:
        return -1

    min_index = 0
    smallest = L[0]

    for i in range(len(L)):
        if L[i] < smallest:
            smallest = L[i]
            min_index = i

    return min_index


def one_loop(L):
    for j in range(len(L) - 1):
        if L[j] > L[j + 1]:
            tmp = L[j + 1]
            L[j + 1] = L[j]
            L[j] = tmp
            print(L)


def test_steps(N):
    counter = 0
    while N > 1:
        counter += 1
        print(N)
        N = N // 2
    print("There are %d steps" % counter)


def selection_sort(L):
    for j in range(len(L)):
        ios = j       # index of smallest item so far
        for i in range(j+1, len(L)):
            if L[i] < L[ios]:
                ios = i
        # swap them
        L[j], L[ios] = L[ios], L[j]
        print("step %d" % (j + 1))
        print(L)
        print("----------")


def main():
    nums = [12, 34, 54, 5, 54]
    L = [17, 4, 19, 3, 11, 8]
    nums = []
    small = smallest_of_index(nums)
    print(small)
    oneLoop(L)
    selection_sort(L)
    test_nested_loop()
    test_steps(1000000)


main()

