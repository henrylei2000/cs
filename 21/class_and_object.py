class Point:
    pass


print(type(Point))
p = Point()
print(type(p))


p.x = 3
p.y = 4
print(p.y)
print(p.x)
x = 4
print(x)


print("(%d, %d)" % (p.x, p.y))
distance_squared = p.x ** 2 + p.y ** 2
print(distance_squared)


# initialization method
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return ((self.x ** 2)+(self.y ** 2)) ** 0.5


p = Point(3, 4)
print(p.distance_from_origin())
r = Point()
print(r.x)


# instances as parameters
def print_point(p):
    print("(%s, %s)" % (str(p.x), str(p.y)))


print_point(p)


# exercises

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from(self, p):
        return ((p.x - self.x) ** 2 + (p.y - self.y) ** 2) ** 0.5


def distance(p1, p2):
    return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5


p = Point(0, 0)
q = Point(3, 4)

print(p.distance_from(q) + q.distance_from(p))
print(p.distance_from(p))

print("d is: %d" % distance(p, q))
