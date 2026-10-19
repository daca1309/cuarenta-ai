import players

def create_game(nr_of_players):
    if nr_of_players != 2 and nr_of_players!=4:
        raise ValueError("invalid nr of players")
    pl1=players.create_player("Player1")
    pl2=players.create_player("Player2")
    team1=[]
    team2=[]
    order=(pl1,pl2)
    move_nr=0
    table=[]
    team1.append(pl1)
    team2.append(pl2)
    if nr_of_players==4:
        pl3=players.create_player("Player3")
        pl4=players.create_player("Player4")
        team1.append(pl3)
        team2.append(pl4)

        temp=(pl3, pl4)
        order+=temp

    game={
        "team1":team1,
        "team2":team2,
        #"nr_of_players": nr_of_players, usa len(game["order"]) instead
        "table":table,
        "move_nr":move_nr,
        "order": order
    }
    return game
   


def get_who_is_playing(game):
    #0=pl1, 1=pl2, 2=pl3, 3=pl4
    x=game["move_nr"]%len(game["order"])
    return game["order"][x]
   

def next_turn(game):
    new_game=game.copy()
    new_game["move_nr"]+=1
    return new_game
   
