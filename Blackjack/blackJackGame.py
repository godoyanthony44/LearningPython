import os
import random

play_game = input("Do you want to play a game of Blackjack, 'y' or 'n': ")
player_cards = []
dealer_cards = []


def player_draw():
    if len(player_cards) == 0:
        for i in range(2):
            player_cards.append(random.randint(1,11))
        if player_cards[0] == 11 and player_cards[1] == 11:
            player_cards[0] = 1
    elif len(player_cards) < 5:
        player_cards.append(random.randint(1, 11))


def dealer_draw():
    if len(dealer_cards) == 0:
        for i in range(2):
            dealer_cards.append(random.randint(1,11))
        if dealer_cards[0] == 11 and dealer_cards[1] == 11:
            player_cards[0] = 1
    elif len(dealer_cards) < 5:
        dealer_cards.append(random.randint(1, 11))


def blackjack():
    print(f"Your cards: {player_cards}")
    print(f"Computer's first card: {dealer_cards[0]}")
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while len(player_cards) < 5:
        if another_card == 'y':
            player_draw()
            print(f"Your cards: {player_cards}, total: {sum(player_cards)}")
            if sum(player_cards) >= 21:
                break
            else:
                another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        elif another_card == 'n':
            break
    while sum(dealer_cards) < 17:
        dealer_draw()


def check_winner():
    player_total = sum(player_cards)
    dealer_total = sum(dealer_cards)

    def print_scores():
        print(f"Your cards were {player_cards} for a total of {player_total}")
        print(f"Dealer cards were {dealer_cards} for a total of {dealer_total}")

    if (player_total <= 21) and (dealer_total <= 21):
        if player_total > dealer_total:
            print(f"You Win!")
            print_scores()
        else:
            print(f"You Lost!")
            print_scores()
    elif player_total > 21:
        print(f"You Lost!")
        print_scores()
    elif dealer_total > 21:
        print(f"You Win! Yay dealer Busted!")
        print_scores()


while play_game == 'y':
    os.system('clear')
    player_draw()
    dealer_draw()
    blackjack()
    check_winner()
    play_game = input("Do you want to play another game of Blackjack, 'y' or 'n': ")
    if play_game == 'y':
        player_cards.clear()
        dealer_cards.clear()
