# Jonathan Lin
# 11/30/2018
# Classes and Methods
# Creating classes to build the compare(war) card game
import card   # Import the card class therefore being able to build a deck.
import random


class Deck:

    def __init__(self):
        """
        Construct a deck with 52 different cards.
        """

        self.deck_of_card = []  # The deck.
        for rank in range(13):
            for suit in range(4):
                new_card = card.Card(rank, suit)  # The form of cards. They have a specific rank and a certain suit.
                self.deck_of_card.append(new_card)

    def draw_a_card(self):
        """
        Add a card to a player's hand from the deck.
        :return: The card that is drawn.
        """
        new_card = self.deck_of_card.pop()
        return new_card

    def shuffle(self):
        """
        Shuffle the deck
        :return: No
        """
        random.shuffle(self.deck_of_card)
