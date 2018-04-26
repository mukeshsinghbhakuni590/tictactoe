from pymongo import MongoClient
from bson import ObjectId

client = MongoClient()
db = client.game_engine

sessioncltn = db.sessions


def create_user_session(user_obj_id, token):
    sessioncltn.insert_one(
        { "_id" : token,
          "user" : user_obj_id, 
          "token" : token})

def get_session(token):
    return sessioncltn.find_one({"_id" : token})

def get_session_by_userid(user_id):
    return sessioncltn.find_one({"user" : user_id})

def expire_session(token):
    sessioncltn.remove({"_id" : token})