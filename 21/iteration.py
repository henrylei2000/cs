"""
multiple assignment
"""


def multiple_assignment():
    bruce = 5
    print(bruce)
    bruce = 7
    print(bruce)


def countdown(n):
    while n > 0:
        print(n)
        n -= 10
    print("Blastoff!")


countdown(50)


def count_up(n):
    while n <= 100:
        print(n)
        n += 10
    print("Blastoff!")


count_up(10)


def num_digits(n):
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10
    return count


def number_of_digits(n):
    # n > 0
    # n // 10 == 0 means 1 digit
    # iteration: n // 10 // 10 == 0: 2 digits

    # count the times of "// 10": total number of digits
    number = 1  # initial value
    while n // 10 > 0:
        number += 1
        n //= 10
    return number


def number_of_digits_another_way(n):
    return len(str(n))


def number_of_digits_alternative(n):
    minimum = 0
    maximum = 10
    digits = 1
    if n < minimum:
        return "invalid input"
    while n >= maximum:
        maximum *= 10
        digits += 1
    return digits


print(number_of_digits(210))
print(number_of_digits_alternative(1500))
print(number_of_digits_another_way(40340))


x = 1
while x < 13:
    print('%(first)03d\t%(second)04d\t%(third)05d' % {"first": x, "second": 2**x, "third": 3**x})
    x += 1

x = 1
while x <= 6:
    print("%d " % (x))
    x += 1

x = 1
output = ""
while x <= 6:
  output += str(x) + "\t" * 2
  x += 1
print(output)

i = 1
output = ""
while i <= 6:
  output += str(2*i) + "\t"
  i += 1
print(output)


