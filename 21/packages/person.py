import random
import string


class Person:
    """Person class for storing Person information and behaviors."""

    def __init__(self, name="Henry", gender="male", age=0, year=2019, major="Undecided"):
        self.name = name
        self.gender = gender
        self.age = age
        self.year = year
        self.major = major

    def change_major(self, major):
        self.major = major

    def describe(self):
        return {"name": self.name, "gender": self.gender, "age":self.age, "year":self.year, "major":self.major}


def main():
    students = []

    for i in range(871):
        name = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(4, 8))).capitalize()
        if random.randint(0, 1) > 0:
            gender = 'female'
        else:
            gender = 'male'
        age = random.randint(15, 22)
        year = random.randint(0, 3) + 2016
        majors = ["ECON", "MATH", "PHYS", "CS", "HIST", "ENGR", "CHEM", "BIOL", "ENGL", "FREN", "POLI", "ENVN"]
        students += [Person(name, gender, age, year, majors[random.randint(0, 10)])]

#    print(students[random.randint(0, 870)])

#   statistics
    total = 0
    for student in students:
        if student.major == "HIST" and student.year == 2019:
            total += 1
            print(student.describe())

    print("total student: %d" % total)

    print("sample student =======")
    s = students[800]
    print(s.describe())
    s.change_major("ECON")
    print(s.describe())



if __name__ == '__main__':
    print("This only executes when %s is executed rather than imported" % __file__)
    main()