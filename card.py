# Jonathan Lin
# 11/30/2018
# Classes and Methods
# Creating classes to build the compare(war) card game


class Card:

    def __init__(self, rank, suit):
        """
        Construct a class which assigns ranks and suits to cards.
        :param rank: The very first factor used to use to compare cards.
        :param suit: The second thing to look at in the process of comparing, when cards have the same rank.
        """

        self.rank = rank  # Pass the ranks I want the cards to have to the rank parameter
        self.suit = suit  # Pass the suits I want the cards to have to the suit parameter
        self.ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                      "Ten", "Jack", "Queen", "King"]
        # Create the list of ranks
        self.suits = ["Diamonds", "Clubs", "Hearts", "Spades"]  # Create the list of suits

    def compared_to(self, other_card):
        """
        A method to compare two cards according to their ranks and suits.
        :param other_card: The card Player Two holds.
        :return: The card with the greater rank. If they share the same rank, return the card with the greater suit.
        """
        if self.rank > other_card.rank:
            return self
        elif other_card.rank > self.rank:
            return other_card
        else:
            if self.suit > other_card.suit:
                return self
            else:
                return other_card

    def __str__(self):
        """
        It also gives the cards a way to call themselves, in the form of "rank" of "suit".
        :return: The text value of the rank and suit.
        """
        new_card = self.ranks[self.rank] + " of " + self.suits[self.suit]
        return new_card
