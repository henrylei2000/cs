from sets_of_objects import Deck
from sets_of_objects import Card


class Hand(Deck):
    def __init__(self, name=""):
        self.cards = []
        self.name = name

    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            s = s + " is empty\n"
        else:
            s = s + " contains\n"
        return s + Deck.__str__(self)

    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                count += 1
                print('Hand %s: %s matches %s' % (self.name, card, match))
        return count

    def printHands(self):
        s = "Hand " + self.name
        if self.is_empty():
            s = s + " is empty\n"
        else:
            s = s + " contains\n"
        return s + Deck.__str__(self)

#deck = Deck()
#deck.shuffle()
#hand = Hand("Frank")
#deck.deal([hand], 5)
#print(hand)


class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.hands = []

class OldMaidHand(CardGame):

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count = count + hand.remove_matches()
        return count

    def find_neighbor(self, i):
        numHands = len(self.hands)
        for neighbor in range(1, numHands):
            if neighbor != i:
                if not self.hands[neighbor].is_empty():
                    return neighbor

    def play_one_turn(self, i):
        if self.hands[i].is_empty():
            return 0
        neighbor = self.find_neighbor(i)
        pickedCard = self.hands[neighbor].pop()
        self.hands[i].add(pickedCard)
        print("Hand %s picked %s" % (self.hands[i].name, pickedCard))
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def play(self, names):
        self.deck = Deck()
        # remove queen of clubs
        self.deck.remove(Card(0, 12))

        # make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(Hand(name))

        # deal the cards
        self.deck.deal(self.hands)
        print('---------- Cards have been dealt.')
        self.printHands()

        # remove initial matches
        matches = self.remove_all_matches()
        print("---------- Matches discarded, play begins.")
        self.printHands()

        # play until all 50 cards are matched
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            print('now the matches number is: %d \n' % matches)
            matches = matches + self.play_one_turn(turn)
            turn = (turn + 1) % num_hands

        print('---------- Game is over.')
        self.printHands()

    def printHands(self):
        for hand in self.hands:
            print(hand)

game = OldMaidHand()
#hand = OldMaidHand('Frank')
players = [Hand("Frank"), Hand("Tom"), Hand("Adam"), Hand("Fred")]
game.hands = players
game.deck.deal(players, 13)
for player in players:
    print(player)
game.remove_all_matches()

#game.play(["Tony", 'Shayla', 'Andy'])
