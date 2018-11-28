import card
import deck


def main():
    deck_of_cards = deck.Deck()
    player_one = []
    player_two = []
    deck_of_cards.shuffle()
    for x in range(5):
        player_one.append(deck_of_cards.draw_a_card())
        player_two.append(deck_of_cards.draw_a_card())
    games = -1
    for x in range(5):
        games = games + 1
        print(player_one[games].compared_to(player_two[games]))


main()
