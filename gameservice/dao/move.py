from pymongo import MongoClient
from bson import ObjectId
from utils import constants as gconst 

client = MongoClient()
db = client.game_engine

movehistorycltn = db.move_history


def make_move_entry(game_obj_id,user_obj_id,new_state):
    instance_object = {
        "game_id" : game_obj_id,
        "cstate" : new_state,
        "next_player" : user_obj_id
    }
    move_id = movehistorycltn.insert_one(instance_object)
    return move_id.inserted_id