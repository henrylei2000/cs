"""
neko atsume cat game

Name: Henry Lei
Date: 05/01/2020
"""

from utils import *
from cat import *
from item import *
from yard import *
from store import *
from random import *

#
# TDD: list of features
#
#  display(yard)
#  fishes = shop(store,yard,fishes)
#  show(album)
#  fishes = update(yard,cats,album,fishes)
#



def main():
    cats = loadCats("cats.txt")
    items = loadItems("items.txt")
    store = Store(items)
    yard = Yard(5)
    album = []
    fishes = 200
    opts = ["see yard","shop","cat album", "quit"]
    done = False
    while not done:
        print("="*40)
        print("You've got %d fishes..." % (fishes))
        pick = menu(opts)
        if pick == 1:
            display(yard)
        elif pick == 2:
            if yard.full():
                print("Your yard is already full...")
            else:
                fishes = shop(store,yard,fishes)
        elif pick == 3:
            show(album)
        elif pick == 4:
            done = True
        fishes = update(yard,cats,album,fishes)
    print("\nMeow....\n")


#
# write your functions here
#
#  display(yard)
def display(yard):
    """
    purpose: display contents of the yard
    """
    print('-' * 20 + 'YARD' * 10 + '-' * 20)
    print(yard)
    print('-' * 20 + 'YARD' * 10 + '-' * 20)


#  fishes = shop(store,yard,fishes)
def shop(store, yard, fishes):
    """
    purpose: buy items from the store using fishes
    :param store:
    :param yard:
    :param fishes:
    :return (int): fishes remaining
    """
    print("-" * 20 + " Welcome to the cat store! " + "-" * 20)
    print()
    print(store)

    num_item = getInt("Which item do you want to buy? [0 to cancel]")

    if num_item == 0:
        return fishes
    elif 0 < num_item <= len(store.items):
        # money talks
        cost = store.getItemCost(num_item)

        # does the user have enough fishes? if yes, use the store
        # method buyItem(number) to "buy" the item. if no, tell
        # the user they don't have enough fishes
        if fishes >= cost:
            item = store.buyItem(num_item)
            yard.addItem(item)
            fishes -= cost
        else:
            print("You don't have enough fishes.")

    return fishes


#  show(album)
def show(album):
    """
    display album
    :param album: list of cats
    :return: none
    """
    print("." * 20 + "Cat Album" + "." * 20)
    print()
    if len(album):
        for cat in album:
            print(cat)
    else:
        print("No cats have visited. :(")
        print("Try putting out some food or toys!")
    print()
    print("." * 48)


#  fishes = update(yard,cats,album,fishes)
def update(yard,cats,album,fishes):
    """
    update the yard (cats, foods, fishes)
    :param yard:
    :param cats:
    :param album:
    :param fishes:
    :return:
    """
    if not yard.empty():

        # available items
        if yard.itemAvailable():
            # chance for a cat coming
            if randrange(100) < 70:
                coming = randrange(len(cats))
                yard.addCat(cats[coming])
                cats[coming].visited()
                if cats[coming] not in album:
                    album.append(cats[coming])

        # for paired foods and cats
        fishes += yard.updateFood()

        # for cats without foods
        if yard.numCats():
            # chance for a cat leaving
            if randrange(100) < 50:
                cats_in_yard = yard.getCats()
                leaving = randrange(len(cats_in_yard))
                fishes += yard.removeCat(cats_in_yard[leaving])

    return fishes
#



main()
