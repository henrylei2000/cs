class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

    def __add__(self, other):
        time = Time()
        time.hours = self.hours + other.hours
        time.minutes = self.minutes + other.minutes
        time.seconds = self.seconds + other.seconds
        while time.seconds >= 60:
            time.seconds -= 60
            time.minutes += 1
        while time.minutes >= 60:
            time.minutes -= 60
            time.hours += 1
        return time

    def __sub__(self, other):
        time = Time()
        return "it's a joke"

    def __eq__(self, other):
        return (self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds)

    def __gt__(self, other):
        return (self.hours, self.minutes, self.seconds) > (other.hours, other.minutes, other.seconds)

    def __lt__(self, other):
        return (self.hours, self.minutes, self.seconds) < (other.hours, other.minutes, other.seconds)

    def after(self, other):
        return self > other

    def print(self):
        print(str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))

    def increment(self, seconds):
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1
        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1
        return self


zero_time = Time()
print(zero_time)
current_time = Time(9, 18, 23)
current_time.print()

current_time.increment(500).print()
doneTime = Time(10, 18, 23)
print(current_time + doneTime)
print(current_time - doneTime)

if doneTime.after(current_time):
    print("The bread will be done after it starts.")
else:
    print("oops")

