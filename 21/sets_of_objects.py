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
        self.rank[1] > other.rank
        return (self.suit, self.rank) > (other.suit, other.rank)

    def __lt__(self, other):
        return (self.suit, self.rank) < (other.suit, other.rank)


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        output = ''
        count = 1
        for card in self.cards:
            output += ' ' * count + str(card) + '\n'
            count += 1
        return output

    def print(self):
        for card in self.cards:
            print(card)

    def shuffle(self):
        import random
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = random.randrange(i, num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
        return self

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return len(self.cards) == 0

    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break
            card = self.pop()
            hand = hands[i % num_hands]
            hand.add(card)


card1 = Card(1, 1)
print(card1)
card2 = Card(1, 13)
print(card2)
#card1.suits[1] = 'Swirly Whales'
#print(card1)
#print(card2)
print(card1 < card2)
d = Deck()
d.print()
d.shuffle().print()
print(d.remove(Card(2, 2)))
print(card1 < card2)



