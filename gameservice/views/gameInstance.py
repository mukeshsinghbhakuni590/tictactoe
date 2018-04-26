

def single(game_object):
    return { "game_id" : str(game_object["_id"]),
        "cstate" : game_object["cstate"],
        "winner" : str(game_object["winner"]),
        "status" : game_object["status"],
        "user2" :  str(game_object["user2"]), 
        "user1" : str(game_object["user1"]),
        "next_player" : str(game_object["next_player"]) 
    }

def multiple(game_objects):
    return [ single(game_object) for game_object in game_objects ]