import random

class Card:
    """ A class that represents a single playing card """
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ['Narf', 'Ace', '2', '3', '4', '5', '6', '7', '8',
             '9', '10', "Jack", "Queen", "King" ]



    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{0} of {1}".format(self.ranks[self.rank], self.suits[self.suit])

    def cmp(self, other):
        # Check suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # Check ranks

        # Aces higher than kings hardcheck
        if self.rank == "Ace" and other.rank == "Ace":
            return 0

        if self.rank == "Ace":
            return 1

        if other.rank == "Ace":
            return -1

        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # they're equal
        return 0

    # Mathemematical operators overloading extraordinarie
    # Should be pretty obvious which is which
    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0

class Deck:
    """ Represents a deck of Card objects """

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"

        return s

    def shuffle(self):
        """ Shuffles the deck using the built-in random function
        It's pretty random... """

        rng = random.Random()
        rng.shuffle(self.cards)

    def remove(self, card):
        """ Takes in a Card object, check for deep equality, and removes
        if true """

        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        """ Removes the card at the bottom of the deck """
        return self.cards.pop()

    def is_empty(self):
        return self.cards == []

    def deal(self, hands, num_cards=999):
        """ Deals a set of cards, generic enough for many
        types of games """
        num_hands = len(hands)

        for i in range(num_cards):
            if self.is_empty():
                break

            # Takes the top card, deals it to whose turn it is
            card = self.pop()
            hand = hands[i % num_hands]
            hand.add(card)

class Hand(Deck):
    """ Represents a hand that can be used for many types of games """

    def __init__(self, name=""):
        self.cards = []
        self.name = name

    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains\n"

        return s + Deck.__str__(self)

class OldMaidHand(Hand):
    """ Contains the specific rules for a hand playing 'old maid' """

    def remove_matches(self):
        """ Removes both cards from hand if two cards match """
        count = 0
        original_cards = self.cards[:]

        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)

                print("Hand {0}: {1} matches {2}".
                        format(self.name, card, match))
                count += 1

        return count

class CardGame:
    """ Contains some features needed for making general sorts of card games """

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

class OldMaidGame(CardGame):
    """ Contains the game logic for playing the Old Maid's Game """

    def play(self, names):
        self.names = names

        # Remove queen of clubs
        self.deck.remove(Card(0, 12))

        # Make a hand for each player
        self.hands = []
        for name in self.names:
            self.hands.append(OldMaidHand(name))

        # Deal the cards
        self.deck.deal(self.hands)
        print("-" * 8 + " cards have been dealt.")
        self.print_hands()

        # Remove initial matches
        matches = self.remove_all_matches()
        print("-" * 8 + "all matches removed, ready to play.")
        self.print_hands()

        # Play until 50 cards are matched
        turn = 0
        num_hands = len(self.hands)

        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands

        print("-" * 8, " Game is over...")
        self.print_hands()

    def play_one_turn(self, i):
        """ A single player plays a single turn """
        if self.hands[i].is_empty():
            return 0

        # Changes the cards
        neighbor = self.find_neighbor(i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)

        # Removes matches and randomises
        print("Hand", self.hands[i].name, "picked", picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()

        return count

    def find_neighbor(self, i):
        """ Picks a suitable person to get a card from """
        num_hands = len(self.hands)
        for next in range(1,num_hands):
            neighbor = (i + next) % num_hands

            if not self.hands[neighbor].is_empty():
                return neighbor

    def print_hands(self):
        for num, j in enumerate(self.names):
            print(self.hands[num].__str__())

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()

        return count

if __name__ == "__main__":

    game = OldMaidGame()
    game.play(["John", "Ben", "Chris"])

    """
    card1 = Card(1, 2)
    card2 = Card(1, 2)

    print(card1)
    print(card1 > card2)

    hand1 = Hand("John")
    hand1.add(card1)

    print(hand1)

    red_deck = Deck()

    red_deck.remove(card1)
    red_deck.pop()
    red_deck.is_empty()
    #red_deck.shuffle()
    print(red_deck)
    """
