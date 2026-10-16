
# Create a player with a name, a nr of points and an empty hand.
def create_player(name):
    player={
        "name":name,
        "hand":[],
        "points":0
    }
    return player


def add_cards(player, cards):
  #temp_list= player["hand"] + cards
    new_player={
        "name":player["name"],
        "hand":player["hand"] + cards,
        "points":player["points"]       
    }
    return new_player

def remove_card(player, card):
    """
    Return a new player without the specified card.

    The original player must remain unchanged.

    Parameters:
        player: Player dictionary.
        card: Card to remove.

    Returns:
        A new player dictionary.

    Requirements:
        - Remove exactly one matching card.
        - Preserve the order of the remaining cards.
        - Preserve the player's name and points.
        - Raise ValueError if the card is not in the hand.
    """
    #raise ValueError("quantity>length of deck")
    is_card_in_hand=False 
    for x in player["hand"]:
        if card in x:
            is_card_in_hand=True
            index=x
    if not is_card_in_hand:
        raise ValueError("card not in hand")
    
    new_player={
            "name":player["name"],
            "hand":player["hand"][:index]+player["hand"][index+1:],
            "points":player["points"]       
        }
    return new_player