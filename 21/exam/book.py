"""
final quiz review book class
"""
"""
TDD: a Book class
- store information about book (title, author, etc.) - (__init__) properties
- getters and setters
- display gracefully (__str__)
- allows user to update current edition
"""
class Book(object):
    """
    constructor

    """
    def __init__(self, title, author, edition=1):  # optional argument
        self.title = title
        self.author = author
        self.current_ed = edition

    def __str__(self):
        return "title: %s \nauthor: %s \ncurrent edition: %s" % (self.title, self.author, self.current_ed)

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_current_ed(self):
        return self.current_ed

    def update_edition(self):
        self.current_ed += 1
        return self.current_ed


def main():
    harry_potter = Book("Harry Potter", "JK Rowling", edition=5)
    tale_of_two_cities = Book("Two Cities", "Charles Dickens")
    print(harry_potter)
    print(tale_of_two_cities)
    harry_potter.update_edition()
    print(harry_potter.get_author())
    print(harry_potter.get_title())
    print(harry_potter.get_current_ed())
    print(harry_potter)


main()


