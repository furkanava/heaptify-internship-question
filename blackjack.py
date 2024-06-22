import random

def create_deck():
    """Standart 52 kartlık bir deste oluşturur."""
    suits = ["Karo", "Maça", "Sinek", "Kupa"]
    ranks = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Vale", "Kız", "Papaz"]
    deck = [(rank, suit) for suit in suits for rank in ranks] * 4  
    random.shuffle(deck)
    return deck

def deal_card(deck):
    """Desteden bir kart çeker."""
    return deck.pop()

def calculate_hand_value(hand):
    """Elindeki kartların toplam değerini hesaplar."""
    value = 0
    num_aces = 0
    for card in hand:
        rank = card[0]
        if rank == "As":
            value += 11
            num_aces += 1
        elif rank in ["Vale", "Kız", "Papaz"]:
            value += 10
        else:
            value += int(rank)

    while num_aces > 0 and value > 21:
        value -= 10
        num_aces -= 1
    return value

def determine_winner(dealer_hand, player_hands, scores):
    """Kazananı belirler ve skorları günceller."""
    dealer_value = calculate_hand_value(dealer_hand)
    for i, hand in enumerate(player_hands):
        player_value = calculate_hand_value(hand)
        if player_value > 21:
            print(f"Oyuncu {i + 1} battı, dağıtıcı kazandı!")
            scores["Dağıtıcı"] += 1
        elif dealer_value > 21:
            print(f"Dağıtıcı battı, oyuncu {i + 1} kazandı!")
            scores[f"Oyuncu {i + 1}"] += 1
        elif player_value > dealer_value:
            print(f"Oyuncu {i + 1} kazandı!")
            scores[f"Oyuncu {i + 1}"] += 1
        elif player_value < dealer_value:
            print(f"Dağıtıcı kazandı, oyuncu {i + 1} kaybetti!")
            scores["Dağıtıcı"] += 1
        else:
            if len(hand) < len(dealer_hand):  
                print(f"Oyuncu {i + 1} kazandı (daha az kartla beraberlik)")
                scores[f"Oyuncu {i + 1}"] += 1
            else:
                print("Beraberlik!")

def play_round(deck, player_hands, dealer_hand, scores):
    """Bir tur Blackjack oynatır."""

 
    for i, hand in enumerate(player_hands):
        while calculate_hand_value(hand) < 17:
            hand.append(deal_card(deck))
            if calculate_hand_value(hand) > 21:
                print(f"Oyuncu {i + 1} battı!")
                break

    
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

    print("\n--- Sonuçlar ---")
    print(f"Dağıtıcının eli: {dealer_hand}, Toplam: {calculate_hand_value(dealer_hand)}")
    for i, hand in enumerate(player_hands):
        print(f"Oyuncu {i + 1} eli: {hand}, Toplam: {calculate_hand_value(hand)}")

    determine_winner(dealer_hand, player_hands, scores)

def blackjack():
    """Blackjack oyununu yönetir."""
    deck = create_deck()
    scores = {"Oyuncu 1": 0, "Oyuncu 2": 0, "Dağıtıcı": 0}
    round_num = 1

    while len(deck) > 10:  
        print(f"\n--- Round {round_num} ---")
        player_hands = [[deal_card(deck), deal_card(deck)] for _ in range(2)]
        dealer_hand = [deal_card(deck), deal_card(deck)]
        play_round(deck, player_hands, dealer_hand, scores)
        print("\nSkorlar:", scores)
        round_num += 1

    print("\n--- Final Skorlar ---")
    for player, score in sorted(scores.items(), key=lambda item: item[1], reverse=True):
        print(f"{player}: {score}")

blackjack()
