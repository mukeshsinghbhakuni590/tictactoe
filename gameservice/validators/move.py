from jsonschema import validate
from utils.constants import final_status, accepted_status

schema0 = {
            "type" : "object",
            "properties" : {
                "gi_id" : {"type" : "string"},
                "cstate" : {"type" : [["string"]]},
                "curr_player" : {"type" : "string"}, 
                "next_player" : {"type" : "string"},
                "token" :  {"type" : "string"}
            }
        }

def validate_move_obj(payload):
    try:
        validate(payload,schema0)
        return True
    except:
        return False

def validate_move(proposed_state,next_player,game_instance):
    Goti = None
    count = 0
    if next_player == game_instance['user1'] :
        Goti = 'O' # user2 played
    else :
        Goti = 'X' # user1 played
    current_state = game_instance['cstate']
    for i in range(3):
        for j in range(3):
            if not (proposed_state[i][j] == current_state[i][j]) :
                count += 1
                if count > 1: # more than one change
                    return False
                if current_state[i][j]: # try to overwrite 
                    return False
                if not (proposed_state[i][j] == Goti): # not your move
                    return False
    return True


def get_winner(new_state,user1,user2):
    
    for i in range(3):
        if new_state[i][0] == new_state[i][1] == new_state[i][2]:
            if new_state[i][0] == 'X':
                return user1
            elif new_state[i][0] == 'O':
                return user2
        if new_state[0][i] == new_state[1][i] == new_state[2][i] :
            if new_state[0][i] == 'X':
                return user1
            elif new_state[0][i] == 'O':
                return user2

    if new_state[0][0] == new_state[1][1] == new_state[2][2]:
        if new_state[0][0] == 'X':
            return user1
        elif new_state[0][0] == 'O':
            return user2
    if new_state[0][2] == new_state[1][1] == new_state[2][0] :
        if new_state[0][2] == 'X':
            return user1
        elif new_state[0][2] == 'O':
            return user2  
    return None

                    
def check_status(new_state):
    for i in range(3):
        for j in range(3):
            if not new_state[i][j]:
                return accepted_status
    return final_status