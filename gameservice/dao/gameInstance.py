from pymongo import MongoClient
from bson import ObjectId
from utils import constants as gconst 

client = MongoClient()
db = client.game_engine
 
ginstancecltn = db.game_instance

def create_game_instance(user1_obj_id, user2_obj_id):
    instance_object = {
        "user1" : user1_obj_id,
        "user2" : user2_obj_id,
        "cstate" : gconst.default_state,
        "status" : gconst.default_start_status,
        "next_player" : user1_obj_id,
        "winner" : None
    }
    gi = ginstancecltn.insert_one(instance_object)
    return gi.inserted_id


def get_game_instance(game_obj_id):
    return ginstancecltn.find_one({"_id" : game_obj_id})

def get_game_by_user(user_id):
    l1 = list(ginstancecltn.find({"user1" : user_id}))
    l2 = list(ginstancecltn.find({"user2" : user_id}))
    return (l1+l2)

def accepted_game_instance(game_obj_id):
    ginstancecltn.update_one(
        {"_id" : game_obj_id}, 
        {"$set" : { "status" : gconst.accepted_status } })

def make_move(game_obj_id, new_state, next_player, new_status, winner = None):
    ginstancecltn.update_one(
        {"_id" : game_obj_id}, 
        {"$set" : 
            {  "cstate" : new_state,
               "status" : new_status,
               "next_player" : next_player,
               "winner" : winner}
        }
    )

def get_requested_game_instances(user_obj_id):
    return list(ginstancecltn.find({"user2" : user_obj_id , "status" : gconst.default_start_status}))
 