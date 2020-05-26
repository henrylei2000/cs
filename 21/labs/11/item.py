"""
Item Class for Neko Atsume App

Name: Henry Lei
Date: 04/30
"""

from utils import *

# TDD:
# list of features (class Item)
#   get name of item
#   get cost of item
#   get type of item
#   set cost of item
#   check if item has type toy
#   check if item has type food

#
# add your Item class here
#
class Item():
    """items can be either food or toys"""

    def __init__(self, name, cost, itype):
        """
        constructor for Item objects
        """
        super(Item, self).__init__()
        self.name = name
        self.cost = cost
        self.itype = itype

    def __str__(self):
        """
        purpose: should return string representation of object
        params:
        return (str): Frisky Bitz (food) $ 30 fishes
        """
        return "%20s (%4s) $%3d fishes" % (self.name, self.itype, self.cost)

    #   get name of item
    def getName(self):
        """
        purpose: get name of item
        params: self (Item)
        return (str): name
        """
        return self.name

    #   get cost of item
    def getCost(self):
        """
        purpose: get cost of item
        params: self (Item)
        return (int): cost
        """
        return self.cost

    #   get type of item
    def getItemType(self):
        """
        purpose: get type of item
        params: self (Item)
        return (str): type
        """
        return self.itype

    #   set cost of item
    def setCost(self, cost):
        """
        purpose: set or change the cost of the item
        params:
            self (Item)
            cost (int)
        return: none
        """
        self.cost = cost

    #   check if item has type toy
    def isToy(self):
        """
        purpose: check if item has type toy
        params:
            self (Item)
        return (bool)
        """
        if self.itype == "toy":
            return True
        else:
            return False

    #   check if item has type food
    def isFood(self):
        """
        purpose: check if item has type food
        params:
            self (Item)
        return (bool)
        """
        if self.itype == "food":
            return True
        else:
            return False


# ------------------------------------------------ #
# Note: below is test code for the Item class.
# You should look at it, but do not need to modify it.

def main():
    """test the item class"""
    items = loadItems("items.txt")   # from utils.py
    for item in items:
        print(item)                  # should just show all items


    # more tests using a fake item and assert statements.
    # info on asserts:  https://www.cs.swarthmore.edu/pyref/#_assert
    # no output from this means your Item class works!
    # if you get an AssertionError, something in your class doesn't work
    # (probably because you haven't written the method yet)

    name = "AnItem"
    cost = 100
    itype = "toy"
    fakeitem = Item(name,cost,itype)
    assert(fakeitem.getName()==name)
    assert(fakeitem.getCost()==cost)
    assert(fakeitem.getItemType()==itype)
    assert(fakeitem.isToy()==True)
    assert(fakeitem.isFood()==False)
    fakeitem.setCost(cost*2)
    assert(fakeitem.getCost()==cost*2)


if __name__ == "__main__":
    main()
