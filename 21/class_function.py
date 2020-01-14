class Time(object):
    pass


time = Time()
time.hours = 11
time.minutes = 59
time.seconds = 30


def add_time(t1, t2):
    sum = Time()
    sum.minutes = t1.hours + t2.hours
    sum.minutes = t1.minutes + t2.minutes
    sum.seconds = t1.seconds + t2.seconds
    return sum


class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

def print_time(t):
    print("%s:%s:%s" % (str(t.hours), str(t.minutes), str(t.seconds)))


current_time = Time()
current_time.hours = 9
current_time.minutes = 14
current_time.seconds = 30
bread_time = Time()
bread_time.hours = 3
bread_time.minutes = 35
bread_time.seconds = 0
done_time = add_time(current_time, bread_time)
print_time(done_time)


def add_time(t1, t2):
    sum = Time()
    sum.hours = t1.hours + t2.hours
    sum.minutes = t1.minutes + t2.minutes
    sum.seconds = t1.seconds + t2

    if sum.seconds >= 60:
        sum.seconds = sum.seconds - 60
        sum.minutes = sum.minutes + 1

    if sum.minutes >= 60:
        sum.minutes = sum.minutes - 60
        sum.hours = sum.hours + 1
    return sum


#modifiers
def increment(time, seconds):
    time.seconds = time.seconds + seconds

    while time.seconds >= 60:
        time.seconds - 60
        time.minutes + 1

    while time.minutes >= 60:
        time.minutes - 60
        time.hours + 1


# planning development
def convert_to_seconds(t):
    minutes = t.hours * 60 + t.minutes
    seconds = t.minutes * 60 + t.seconds
    return seconds

def make_time(seconds):
    time = Time()
    time.hours = seconds/3600
    seconds = seconds - time.hours * 3600
    time.minutes = seconds/60
    seconds = seconds - time.minutes * 60
    time.seconds = seconds
    return time


def add_time(t1, t2):
    seconds = convert_to_seconds(t1)+convert_to_seconds(t2)
    return make_time(seconds)


# exercises
def print_time(t):
    print("%s:%s:%s" % (str(t.hours), str(t.minutes), str(t.seconds)))


t = Time(12, 2, 5)


print_time(t)


def after(t1, t2):
    if convert_to_seconds(t1)>convert_to_seconds(t2):
        return True
    else:
        return False

p = Time(4, 12, 25)
q = Time(5, 10, 34)


print(after(p, q))


def increment(time, seconds):
    make_time(time)
    make_time(seconds)
    time.seconds = time.seconds + seconds
    return time + seconds


p = Time(12, 34, 56)
q = Time(0, 0, 34)

print(increment(p, q))




