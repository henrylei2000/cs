"""
coding exercise on list
"""

from packages.sqtools import *

def our_past():
    horsemen = ["war", "famine", "pestilence", "death"]

    i = 0
    while i < 4:
        print(horsemen[i])
        i += 1


def test_range():
    print(len(range(-1)))
    if range(-1):
        print(range(0, -1))
    else:
        print("[]")


def convert_string_to_list(s):
    return s.split(" ")


def convert_list_to_string(l):
    output = l[0] + " " + l[1] + " " + l[2] + " " + l[3]
    return output

input = ['I', 'am', 'a', 'student.']


print(convert_list_to_string(input))


def list_to_string(l):
    return str(l)


def test(input):
    bucket = "" # container for final concatenated string result

    i = 0
    while i < len(input):
        bucket = bucket + input[i] + " "
        i += 1

    return bucket


def test_for_loop(x):
    bucket = ""
    for x in input:
        bucket = bucket + x + " "
    return bucket


def delete_from_list(list, index):
    """
    >>> delete_from_list(['I', 'am', 10], 0)
    ['am', 10]
    """
    the_list_after_deletion = []
    for element in list:
        if element != list[index]:
            the_list_after_deletion += [element]
        else:
            pass
    return the_list_after_deletion




list = ['I', 'am', 'a', 'good', 'student']

def delete_simple(incoming_list, index):
    """
    >>> delete_simple(['I', 'am', 10], 0)
    ['am', 10]
    """
    incoming_list = incoming_list[0:index] + incoming_list[index + 1:len(list)]
    return incoming_list


def delete_del(incoming_list, index):
    """
    >>> delete_simple(['I', 'am', 10], 0)
    ['am', 10]
    """
    del incoming_list[index]
    return incoming_list

print(delete_simple(list, 0))

print(list)

delete_from_list(['I', 'am', 10], 0)

print(test_for_loop(input))
print(test(input))


my_list = ['a', 'b', 'd', 'e']
def insert_to_list():
    print("insert ======")
    insert_in_middle('c', my_list)
insert_to_list()
print(my_list)


def objects_and_values():
    # a = "banana"
    # b = 'banana'
    a = [1, 2, 3]
    # b = [1, 2, 3]
    c = a[:]
    b = a
    print("==========")
    print(a is b)
    print(a is c)
    print(a == b)

    b[2] = -3
    print(b)
    print(a)

objects_and_values()

global_string = "good game"

def manipulate(s):
    s = '5'
    return s


print(manipulate(global_string))

print(global_string)

global_list = ["hi", "hello", "bye", "goodbye"]


def manipulate_list(s):
    s[1] = 100
    return s


print(manipulate_list(global_list))

print(global_list)


nested = [1, 2, 3, [1, 2, [1, 5]]]
print(nested[3][2][1])


def make_matrix(rows, columns):
    """
      >>> make_matrix(3, 5)
      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
      >>> make_matrix(4, 2)
      [[0, 0], [0, 0], [0, 0], [0, 0]]
      >>> make_matrix(1, 3)
      [[0, 0, 0]]
    """
    return [[0] * columns] * rows


if __name__ == '__main__':
    import doctest
    doctest.testmod()

