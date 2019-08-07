
"""
exercises for conditionals / chapter 4 of cs21
"""


"""
exercise 1
"""
print(5 % 2)
print(5 % 2)
print(9 % 5)
print(15 % 12)
print(12 % 15)
print(6 % 6)
print(0 % 7)
print(7 % 1)

"""
exercise 2
"""


def function_a():
    print("function_a was called...")


def function_b():
    print("function_b was called...")


def function_c():
    print("function_c was called...")


def dispatch(choice):
    """
    >>> dispatch('a')
    function_a was called...
    >>> dispatch('b')
    function_b was called...
    >>> dispatch('c')
    function_c was called...
    """
    if choice == 'a':
        function_a()
    elif choice == "b":
        function_b()
    elif choice == "c":
        function_c()
    else:
        print("Invalid choice.")


def is_divisible_by_3(n):
    """
    exercise 3: if/else
      >>> is_divisible_by_3(7)
      False
      >>> is_divisible_by_3(9)
      True
    """
    if n % 3 == 0:
        return True
    else:
        return False


def is_m_divisible_by_n(m, n):
    """
    exercise 4: generalize the previous 'by_3', 'by_5'
      >>> is_m_divisible_by_n(21, 8)
      False
      >>> is_m_divisible_by_n(9, 3)
      True
    """
    if m % n == 0:
        return True
    else:
        return False


print("exercise 5")
if "Ni!":
    print('We are the Knights who say, "Ni!"')
else:
    print("Stop it! No more of this!")

if 0:
    print("And now for something completely different...")
else:
    print("What's all this, then?")

if __name__ == '__main__':
    import doctest
    doctest.testmod()