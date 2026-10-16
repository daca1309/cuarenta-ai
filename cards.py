import random
values = (1, 2, 3, 4, 5, 6, 7, "J", "Q", "K")

#crear una baraja completa de Cuarenta.
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

#determinar si dos cartas tienen el mismo valor, independientemente de su palo.
def same_value(card1, card2):
    return card1[0]==card2[0]

#determinar si dos cartas son exactamente iguales, incluyendo valor y palo.
def same_card(card1, card2):
    if (card1[0]==card2[0] and card1[1]==card2[1]):
        return True
    return False

#mezclar aleatoriamente las cartas.
def shuffle_deck(deck):
    baraja=deck[:]
    random.shuffle(baraja)
    return baraja

#extraer una cantidad determinada de cartas.
def split_deck(deck, quantity):
    if quantity>len(deck):
        raise ValueError("quantity>length of deck")
        #return (len(deck), quantity)
    elif (quantity*(-1))>len(deck):
        raise ValueError("negative quantity>length of deck")
    first_slice=deck[:quantity]
    second_slice=deck[quantity:]
    return (first_slice, second_slice)

