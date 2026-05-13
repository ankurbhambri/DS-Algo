# Design the data structures for a generic deck of cards. Explain how you would subclass the data structures to implement blackjack.

import random
from enum import Enum, IntEnum

class Suit(Enum):
    CLUBS = 1; DIAMONDS = 2; HEARTS = 3; SPADES = 4

class Rank(IntEnum):
    TWO = 2; THREE = 3; FOUR = 4; FIVE = 5; SIX = 6; SEVEN = 7; EIGHT = 8
    NINE = 9; TEN = 10; JACK = 11; QUEEN = 12; KING = 13; ACE = 14

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck:
    def __init__(self):
        # Create 52 cards using a list comprehension
        self.cards = [Card(s, r) for s in Suit for r in Rank]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop() if self.cards else None

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)


class BlackjackCard(Card):
    def value(self):
        if self.rank >= Rank.TEN and self.rank <= Rank.KING:
            return 10
        if self.rank == Rank.ACE:
            return 11 # We handle the 1 or 11 logic in the Hand class
        return self.rank.value

class BlackjackHand(Hand):
    def get_score(self):
        score = 0
        aces = 0
        
        for card in self.cards:
            score += card.value()
            if card.rank == Rank.ACE:
                aces += 1
        
        # If we are over 21, turn Aces from 11 into 1
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
        return score

    def is_busted(self):
        return self.get_score() > 21


# example usage
deck = Deck()
deck.shuffle()
hand = BlackjackHand()
hand.add_card(BlackjackCard(Suit.HEARTS, Rank.ACE))
hand.add_card(BlackjackCard(Suit.SPADES, Rank.KING))
print(f"Hand score: {hand.get_score()}")  # Should print 21