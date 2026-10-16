
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

    index=player["hand"].index(card)
    new_player={
            "name":player["name"],
            "hand":player["hand"][:index]+player["hand"][index+1:],
            "points":player["points"]       
        }
    return new_player