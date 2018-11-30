import deck


def main():
    deck_of_cards = deck.Deck()  # Make a deck of cards
    player_one = []  # Player One's cards
    player_two = []  # Player Two's cards
    # At this point neither of the players draw, so they have no cards at hands.
    deck_of_cards.shuffle()
    for x in range(5):
        # Each of the player draws five cards to their hands.
        player_one.append(deck_of_cards.draw_a_card())
        player_two.append(deck_of_cards.draw_a_card())
    player_one_record = 0  # The rounds Player One wins
    player_two_record = 0  # The rounds Player Two wins
    # At this point they have not yet started the game, so both of them win 0 rounds.
    # The rounds will be used to determine which player will win the game.
    games = -1
    # The order of rounds. -1 means that the game has not yet started.
    # It also represents the order of cards. Depending on the order, the players will compare specific pair of cards.
    for rounds in range(5):
        games = games + 1  # After each round, the order increases by 1.
        print("Player One has " + str(player_one[games]) + ".")
        print("Player Two has " + str(player_two[games]) + ".")
        if player_one[games].rank > player_two[games].rank:
            # Compare the ranks first
            print("Player One wins the round with " + str(player_one[games].compared_to(player_two[games])) + ".")
            player_one_record = player_one_record + 1  # If Player One wins, a point will be added to his record.
        elif player_two[games].rank > player_one[games].rank:
            print("Player Two wins the round with " + str(player_one[games].compared_to(player_two[games])) + ".")
            player_two_record = player_two_record + 1  # If Player Two wins, a point will be added to his record.
        else:
            # If the ranks are the same between two cards, compare their suits.
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
