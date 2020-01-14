class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.ranks[self.rank] + ' of ' + self.suits[self.suit]

    def __eq__(self, other):
        return (self.suit, self.rank) == (other.suit, other.rank)

    def __gt__(self, other):
        return (self.suit, self.rank) > (other.suit, other.rank)

    def __lt__(self, other):
        return (self.suit, self.rank) < (other.suit, other.rank)


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def print(self):
        for card in self.cards:
            print(card)


card1 = Card(2, 2)
print(card1)
card2 = Card(1, 11)
print(card2)
#card1.suits[1] = 'Swirly Whales'
#print(card1)
#print(card2)
print(card1 < card2)
d = Deck()
d.print()




