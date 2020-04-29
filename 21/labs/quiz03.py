"""
Please enter your grades below.
Enter a -1 when you are all done...

grade  1: 98
grade  2: 87
grade  3: 65
grade  4: 95
grade  5: 80
grade  6: -1

The average of those 5 grades is 85.000
"""

def main():

    finished = False
    count = 0
    total = 0.0
    while not finished:
        count += 1
        grade = float(input("grade " + str(count) + ": "))
        if grade == -1:
            finished = True
            count -= 1
        else:
            total += grade
    average = total / count
    print("%.3f" % average) # make sure to print the juicy thing at the end

main()