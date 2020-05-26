"""
Cat Class for Neko Atsume App

Name: Henry Lei
Date: 05/01
"""

from utils import *
import random
# TDD:
# list of features (class Cat)
#   get name of cat
#   get description of cat
#   get personality of cat
#   get visits of the cat
#   return random number of fishes
#   add one visit to cat

class Cat():


    def __init__(self, name, description, personality):
        """
        constructor for Item objects
        """
        super(Cat, self).__init__()
        self.name = name
        self.description = description
        self.personality = personality
        self.visits = 0


    def __str__(self):
        """
        purpose: should return string representation of object
        params:
        return (str): Rubber Ball:  60 fishes (toy)
        """
        return "%s (%s), visits: %d" \
               % (self.name, self.description, self.visits)

    #   get name of cat
    def getName(self):
        """
        purpose: get name of cat
        params: self (Cat)
        return (str): name
        """
        return self.name

    #   get description of cat
    def getDescription(self):
        """
        purpose: get description of cat
        params: self (Cat)
        return (str): cat
        """
        return self.description

    #   get personality of cat
    def getPersonality(self):
        """
        purpose: get personality of cat
        params: self (Cat)
        return (str): personality
        """
        return self.personality

    #   get visits of the cat
    def getVisits(self):
        """ 
        purpose: get number of visits
        params: self (Cat)
        return (int): number of visits
        """
        return self.visits


    #   return random number of fishes
    def getFishes(self):
        """
        purpose: get random number of fishes between 10 and 50
        params: self (Cat)
        return (int): number of fishes
        """
        fishes = random.randrange(10, 51)
        return fishes

    #   add one visit to cat
    def visited(self):
        """
        purpose: return number of visits of cat
        params: self (Cat)
        return (str): number of visits
        """
        self.visits += 1


# ------------------------------------------------ #
# Note: below is test code for the Cat class.
# You should look at it, but do not need to modify it.

def main():
    """test the cat class"""
    cats = loadCats("cats.txt")     # from utils.py
    for cat in cats:
        print(cat)                  # should print out all cat objs


    # more tests using a fake cat and assert statements.
    # info on asserts:  https://www.cs.swarthmore.edu/pyref/#_assert
    # no output from this means your Cat class works!
    # if you get an AssertionError, something in your class doesn't work
    # (probably because you haven't written the method yet)

    name = "ACat"
    desc = "Black"
    pers = "Nice"
    fakecat = Cat(name,desc,pers)
    assert(fakecat.getName()==name)
    assert(fakecat.getDescription()==desc)
    assert(fakecat.getPersonality()==pers)
    fishes = fakecat.getFishes()
    assert(fishes>=10 and fishes<=50)
    assert(fakecat.getVisits()==0)
    Nvisits = 5
    for i in range(Nvisits):
        fakecat.visited()
        assert(fakecat.getVisits()==i+1)

if __name__ == "__main__":
    main()
