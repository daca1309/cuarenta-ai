values = (1, 2, 3, 4, 5, 6, 7, "J", "Q", "K")

def create_deck():
    # Spades = 0; Hearts = 1; Diamonds = 2; Clubs = 3
    deck = []
    for suit in range(4):
        for value in values:
            card = (value, suit)
            deck.append(card)
    return deck
#print(create_deck())

def get_value(card):
    return card[0]

def get_sign(card):
    return card[1]

def same_value(card1, card2):
    return card1[0]==card2[0]

def same_card(card1, card2):
    if (card1[0]==card2[0] and card1[1]==card2[1]):
        return True
    return False

def validate_deck(deck):
    pass

def shuffle_deck(deck):
    pass


def deal_cards(deck, quantity):
    pass


def deal_two_players(deck):
    pass