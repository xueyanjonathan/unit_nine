import card
import random


class Deck:

    def __init__(self):

        self.deck_of_card = []
        for rank in range(13):
            for suit in range(4):
                new_card = card.Card(rank, suit)
                self.deck_of_card.append(new_card)

    def draw_a_card(self):
        new_card = self.deck_of_card.pop()
        return new_card

    def shuffle(self):
        random.shuffle(self.deck_of_card)