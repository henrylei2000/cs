
class Restaurant:

    # Constructor
    # To call this method: obj = <ClassName>(<arg1>,<arg2>,...,<argN>)
    # There can be any number of parameters (even zero!)
    # All code to initialize the data in our object goes here!
    def __init__(self, name, style, location, price, rating):
        """
        Constructor
        Parameters:
            name (str) -
            style (str)
            location (str)
            price (int)
            rating (float) -
        Return (Restaurant) - implicitly returns a new object with style Restaurant
        """
        self.name = name
        self.style = style
        self.location = location
        self.price = price
        self.rating = rating

    # any number of methods can be created
    # Every method has to have `self` as the first parameter!
    # Methods can have any number of additional parameters
    # Members can have a return style (or not!)
    def get_name(self):
        """
        Accessor
        Parameters: None
        Return (string): name of restaurant
        Side effects: None
        """
        return self.name

    def get_style(self):
        """
        Accessor
        Parameters: None
        Return (string): the cuisine style of the restaurant
        Side effects: None
        """
        return self.style

    def get_location(self):
        """
        Accessor
        Parameters: None
        Return (string): the location of the restaurant
        Side effects: None
        """
        return self.location

    def get_price(self):
        """
        Accessor
        Parameters: None
        Return (int): the price range of the restaurant
        Side effects: None
        """
        return self.price

    def get_rating(self):
        """
        Accessor
        Parameters: None
        Return (int): the rating of the restaurant
        Side effects: None
        """
        return self.rating

    def introduce(self):
        print()
        print("The restaurant name is %s." % (self.get_name()))
        print("We cook %s food." % (self.get_style()))
        print("We are in %s." % (self.get_location()))
        print("Our average price is %d dollars." % (self.get_price()))
        print("Customers rate us at %.1f out of 10.0!" % (self.get_rating()))


def get_best_rated(restaurants):
    highest = 0
    highest_index = 0

    for i in range(len(restaurants)):
        rank = restaurants[i].get_rating()
        if rank > highest:
            highest = rank
            highest_index = i

    return restaurants[highest_index]


def main():
    restaurants = []
    mcdonalds = Restaurant("McDonalds", "Fast-food", "Calgary", 10, 6.7)
    restaurants.append(mcdonalds)

    chef_lei = Restaurant("Chef Lei", "Chinese", "Vancouver", 20, 8.6)
    restaurants.append(chef_lei)

    white_spot = Restaurant("White Spot", "Western", "San Francisco", 30, 8.2)
    restaurants.append(white_spot)

    wendys = Restaurant("Wendy's", "Fast-food", "San Diego", 15, 7.7)
    restaurants.append(wendys)

    print("There are %d restaurants in our database." % len(restaurants))

    print("======== WINNER OF 2020 =========")
    best = get_best_rated(restaurants)
    best.introduce()

    print("======== RECOMMEND =========")
    for i in range(len(restaurants)):
        restaurant = restaurants[i]
        if restaurant.get_rating() > 7.0:
            restaurant.introduce()


main()
