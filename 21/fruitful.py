# return values
def area(radius):
    temp = 3.14159 * radius ** 2
    return temp
def area(radius):
    return 3.14159 * radius ** 2

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
def absolute_value(x):
    if x < 0:
        return -x
    return x

def absolute_value(x):
    if x < 0:
        return -x
    elif x > 0:
        return x
print(absolute_value(0)) # none
print(type(None)) # class "NoneType"

# program development: computing distance
def distance(x1, y1, x2, y2):
    return 0.0
print(distance(1, 2, 4, 6)) # use print around function call to get return value
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print("dx is", dx)
    print("dy is", dy)
distance(1, 2, 4, 6)
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared ** 0.5
    return result
print(distance(1, 2, 4, 6))

# composition (wrapping functions, recycling)
def area2(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result