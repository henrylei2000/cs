"""
Given the current pandemic, businesses must limit the number of customers
in their establishment at one time so as to allow for social distancing.

Define a new class called Capacity that will track how many people are
in a store. This class should include the following methods.

1. constructor:   takes the limit for the store and also sets the current
                  number of customers to 0
2. string method: returns a string showing the current number in store, the
                  limit for the store, and how much room for more
3. setLimit:      takes in a new limit for the store
4. getLimit:      returns the limit for the store
5. getCurrent:    returns the current number of customers in the store
6. enter:         takes the number of customers that would like to enter,
                  prints a message about this request, updates current
                  if there is room, otherwise prints a message stating
                  how many spots are available
7. leave:         takes the number of customers leaving the store, prints
                  a message about this request, updates current

Below is a sample main program that uses this class and this is the
output that it should produce.

starting limit is 20
reset limit to 15
Current:  0 Limit: 15 Room for: 15
5 requesting to enter
Current:  5 Limit: 15 Room for: 10
4 requesting to enter
Current:  9 Limit: 15 Room for:  6
current number of customers: 9
7 requesting to enter
Sorry only room for 6 more
Current:  9 Limit: 15 Room for:  6
3 leaving
Current:  6 Limit: 15 Room for:  9
7 requesting to enter
Current: 13 Limit: 15 Room for:  2
"""


class Capacity():

    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __str__(self):
        return "Current: %3d Limit: %3d Room for: %3d" % (self.current, self.limit, (self.limit - self.current))

    def setLimit(self, limit):
        self.limit = limit

    def getLimit(self):
        return self.limit

    def getCurrent(self):
        return self.current

    def enter(self, customers):
        print("%d requesting to enter" % customers)
        room = self.limit - self.current
        if room >= customers:
            self.current += customers
        else:
            print("Sorry only room for %d more" % room)

    def leave(self, customers):
        print("%d leaving" % customers)
        if customers <= self.current:
            self.current -= customers
        else:
            print("There are only %d customers in the store" % self.current)


def main():
    store = Capacity(20)
    limit = store.getLimit()
    print("starting limit is", limit)
    store.setLimit(15)
    print("reset limit to 15")
    print(store)
    store.enter(5)
    print(store)
    store.enter(4)
    print(store)
    current = store.getCurrent()
    print("current number of customers:", current)
    store.enter(7)
    print(store)
    store.leave(3)
    print(store)
    store.enter(7)
    print(store)


main()
