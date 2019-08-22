import random

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "x is: %s, y is %s" % (self.x, self.y)

    def move(self, dx, dy):
        """this is a placeholder"""
        self.x += dx
        self.y += dy

    def distance(self):
        return (self.x * self.x + self.y * self.y) ** 0.5

    def distance_from(self, any_other_point):
        distance_from_p = ((any_other_point.x - self.x) * (any_other_point.x - self.x) + (any_other_point.y - self.y) * (any_other_point.y - self.y)) ** 0.5
        return distance_from_p

    def area_between(self, another_point):
        return abs((another_point.x - self.x) * (another_point.y - self.y))


def test():
    print(type(Point))

    p = Point(3, 4) # initialization method by default

    print(p)

    print(p.distance())

    p.move(5, -20)

    print(p)
    print(p.distance())

    point_a = p
    point_b = Point(5, 4)

    d = point_a.distance_from(point_b)
    print(d)

    print(point_a.area_between(point_b))


def find_furthest_point_to_the_origin_from_a_random_generated_point_list():

    # preparations
        # prepare returned variables
        # prepare mid-result variables
        # prepare initialization/empty variables

    origin = Point(0, 0)
    furthest_distance = 0
    furthest_point = origin
    points = []

    # build a sample list
    for i in range(10):
        x, y = random.randint(-100, 100), random.randint(-100, 100)
        points += [Point(x, y)]

    # traverse the point list and find the max distance
    for point in points:
        if point.distance_from(origin) > furthest_distance:
            furthest_distance = point.distance_from(origin)
            furthest_point = point

    # return
    return furthest_point, furthest_distance



if __name__ == '__main__':
    print("This only executes when %s is executed rather than imported" % __file__)
    test()
    p, d = find_furthest_point_to_the_origin_from_a_random_generated_point_list()
    print(p)
    print(d)