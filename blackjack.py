import random

# Global Variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10,
          'Ace': 11}

playing = True


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


# Prints card class
# print(Card('Hearts', 'Three'))


class Deck():
    def __init__(self):
        # Self.deck is used to create a default empty deck, self.deck was not passed as a parameter because we dont want the value of the
        # deck to change when we initialize the Deck class
        self.deck = []
        # Run the nested for loop to append the combination of suits and ranks
        for suit in suits:
            for rank in ranks:
                # TODO
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_composition = ''
        for card in self.deck:
            # card.__str__() calls the string representation of each card
            deck_composition += '\n' + card.__str__()
        return f'The deck has:  {deck_composition}'

    def shuffle_deck(self):
        # It does not start with return because the random.shuffle happens in place
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

# test_deck = Deck()
# test_deck.shuffle_deck()
# print(test_deck)

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card, ranks]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_ace(self):
        # This loop will check if the total value in the player hand is above 21 and the player has an ace
        # it will adjust the value of the ace, reducing its number by ten and subtracting 1 ace from the players hand
        # Note that self.aces == to True if the value is >= 1.
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():
    def __init__(self):
        self.balance = 100
        self.bet = 0

    def win_bet(self):
        self.balance += self.bet

    def lose_bet(self):
        self.balance -= self.bet


def take_bet(chips=None):
    while True:
        try:
            chips.bet = int(input('Enter your bet!'))
        except TypeError:
            print('Please ensure you are entering a number.')
        else:
            if chips.bet > chips.balance:
                print('You don\'t have enough balance ')
            else:
                break


def hit(deck, hand):
    pass
