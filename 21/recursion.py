def recursive_sum(nested_num_list):
    sum = 0
    for element in nested_num_list:
        if type(element) == type([]):
            sum = sum + recursive_sum(element)
        else:
            sum = sum + element
    return sum


total = recursive_sum([1, 4, [5, -5], 5])


print(total)


# recursive function
def initialize_largest(nested_num_list):
    """
      >>> initialize_largest([2, 9, [1, 13], 8, 6])
      2
      >>> initialize_largest([2, [[100, 7], 90], [1, 13], 8, 6])
      2
      >>> initialize_largest([2, [[13, 7], 90], [1, 100], 8, 6])
      2
      >>> initialize_largest([[[13, 7], 90], 2, [1, 100], 8, 6])
      13
    """
    largest = nested_num_list[0] # core!!!
    if type(largest) == type([]):
        largest = initialize_largest(largest)

    return largest


def recursive_max(nested_num_list):
    """
      >>> recursive_max([2, 9, [1, 13], 8, 6])
      13
      >>> recursive_max([2, [[100, 7], 90], [1, 13], 8, 6])
      100
      >>> recursive_max([2, [[13, 7], 90], [1, 100], 8, 6])
      100
      >>> recursive_max([[[13, 7], 90], 2, [1, 100], 8, 6])
      100
    """
    largest = initialize_largest(nested_num_list) # starting point

    for element in nested_num_list:
        if type(element) == type([]):
            max_of_elem = recursive_max(element)
            if largest < max_of_elem:
                largest = max_of_elem
        else:                           # element is not a list
            if largest < element:
                largest = element

    return largest


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)



if __name__ == '__main__':
    import doctest
    doctest.testmod()