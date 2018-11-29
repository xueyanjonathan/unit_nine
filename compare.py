import deck


def main():
    deck_of_cards = deck.Deck()
    player_one = []
    player_two = []
    deck_of_cards.shuffle()
    for x in range(5):
        player_one.append(deck_of_cards.draw_a_card())
        player_two.append(deck_of_cards.draw_a_card())
    player_one_record = 0
    player_two_record = 0
    games = -1
    for rounds in range(5):
        games = games + 1
        print("Player One has " + str(player_one[games]) + ".")
        print("Player Two has " + str(player_two[games]) + ".")
        if player_one[games].rank > player_two[games].rank:
            print("Player One wins the round with " + str(player_one[games].compared_to(player_two[games])) + ".")
            player_one_record = player_one_record + 1
        elif player_two[games].rank > player_one[games].rank:
            print("Player Two wins the round with " + str(player_one[games].compared_to(player_two[games])) + ".")
            player_two_record = player_two_record + 1
        else:
            if player_one[games].suit > player_two[games].suit:
                print("Player One wins the round with " + str(player_one[games].compared_to(player_two[games])) + ".")
                player_one_record = player_one_record + 1
            else:
                print("Player Two wins the round with " + str(player_one[games].compared_to(player_two[games])) + ".")
                player_two_record = player_two_record + 1
        print("")
    if player_one_record > player_two_record:
        print("Player One wins the game by", player_one_record, "to " + str(player_two_record) + ".")
    else:
        print("Player Two wins the game by", player_two_record, "to " + str(player_one_record) + ".")


main()
