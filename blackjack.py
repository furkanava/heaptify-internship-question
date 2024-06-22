import random

def create_deck():
    """Creates a standard deck of 52 cards."""
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    # Create all card combinations and multiply by 4 for a full deck
    deck = [(rank, suit) for suit in suits for rank in ranks] * 4 
    random.shuffle(deck)  # Randomize card order
    return deck

def deal_card(deck):
    """Draws a single card from the deck."""
    return deck.pop()

def calculate_hand_value(hand):
    """Calculates the total value of a hand."""
    value = 0
    num_aces = 0
    for card in hand:
        rank = card[0]
        if rank == "Ace":
            value += 11
            num_aces += 1
        elif rank in ["Jack", "Queen", "King"]:
            value += 10
        else:
            value += int(rank)

    # Adjust for Aces if the value exceeds 21
    while num_aces > 0 and value > 21:
        value -= 10
        num_aces -= 1
    return value

def determine_winner(dealer_hand, player_hands, scores):
    """Determines the winner of the round and updates scores."""
    dealer_value = calculate_hand_value(dealer_hand)
    for i, hand in enumerate(player_hands):
        player_value = calculate_hand_value(hand)

        if player_value > 21:
            print(f"Player {i + 1} busts, Dealer wins!")
            scores["Dealer"] += 1
        elif dealer_value > 21:
            print(f"Dealer busts, Player {i + 1} wins!")
            scores[f"Player {i + 1}"] += 1
        elif player_value > dealer_value:
            print(f"Player {i + 1} wins!")
            scores[f"Player {i + 1}"] += 1
        elif player_value < dealer_value:
            print(f"Dealer wins, Player {i + 1} loses!")
            scores["Dealer"] += 1
        else:  # Tie (push)
            if len(hand) < len(dealer_hand):  # Win on fewer cards
                print(f"Player {i + 1} wins (with fewer cards)")
                scores[f"Player {i + 1}"] += 1
            else:
                print("Push (tie)")

def play_round(deck, player_hands, dealer_hand, scores):
    """Plays a single round of Blackjack."""

    # Player turns
    for i, hand in enumerate(player_hands):
        while calculate_hand_value(hand) < 17:
            hand.append(deal_card(deck))
            if calculate_hand_value(hand) > 21:
                print(f"Player {i + 1} busts!")
                break  # Stop taking cards if busted
            
    # Dealer's turn
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

    # Results
    print("\n--- Results ---")
    print(f"Dealer's hand: {dealer_hand}, Total: {calculate_hand_value(dealer_hand)}")
    for i, hand in enumerate(player_hands):
        print(f"Player {i + 1} hand: {hand}, Total: {calculate_hand_value(hand)}")

    determine_winner(dealer_hand, player_hands, scores)


def blackjack():
    """Manages the Blackjack game."""
    deck = create_deck()
    scores = {"Player 1": 0, "Player 2": 0, "Dealer": 0}
    round_num = 1

    while len(deck) > 10:  # Enough cards for at least one more round 
        print(f"\n--- Round {round_num} ---")
        player_hands = [[deal_card(deck), deal_card(deck)] for _ in range(2)]
        dealer_hand = [deal_card(deck), deal_card(deck)]

        play_round(deck, player_hands, dealer_hand, scores)

        print("\nScores:", scores)
        round_num += 1
   
    print("\n--- Final Scores ---")
    for player, score in sorted(scores.items(), key=lambda item: item[1], reverse=True):
        print(f"{player}: {score}")

# Start the game!
blackjack()
