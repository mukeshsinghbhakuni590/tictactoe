from flask_restful import Resource
from flask import request
from bson import ObjectId
from dao.gameInstance import get_game_instance ,create_game_instance ,accepted_game_instance ,get_game_by_user
from dao.user import get_user_by_id
from validators.gameInstance import validate_user_ids , validate_game_obj_id 
from dao.session import get_session
from views.gameInstance import multiple 
class GameInstance(Resource):


    def get(self):
        params = request.args.to_dict()
        user_id = ObjectId(params['user_id'])
        games = get_game_by_user(user_id)
        return multiple(games)


    def post(self):
        payload = request.json
        if not validate_user_ids(payload):
            return {"response" : "Bad request"}
            
        user1_obj_id = ObjectId(payload['user1'])
        user2_obj_id = ObjectId(payload['user2'])
        user_token = payload['token']

        if (not get_user_by_id(user1_obj_id)) or (not get_user_by_id(user2_obj_id)) :
            return {"response" : "User not found"}, 404

        user_session = get_session(user_token)
        if not user_session :
            return {"response" : "You Have To LogIn Again"}, 401

        if not (user_session["user"] == user1_obj_id):
            return {"response" : "Bad request"}, 401
        
        return {"response" : str(create_game_instance(user1_obj_id, user2_obj_id))}

    def put(self):
        payload = request.json
        if not validate_game_obj_id(payload):
            return {"response" : "Bad request"}, 401

        print (payload)
        user_obj_id = ObjectId(payload['user_id'])
        game_obj_id = ObjectId(payload['gi_id'])
        user_token = payload['token']

        if (not get_user_by_id(user_obj_id)):
            return {"response" : "User not found"}, 404

        user_session = get_session(user_token)
        if not user_session :
            return {"response" : "You Have To LogIn Again"}, 401

        if not (user_session["user"] == user_obj_id):
            return {"response" : "Bad request"}, 401
        
        game_instance = get_game_instance(game_obj_id)
        if not game_instance :
            return {"response" : "GameInstance not found"}, 404
        
        if not (user_obj_id == game_instance['user2']) :
            return {"response" : "Bad request"}, 401 # ******
        
        accepted_game_instance(game_obj_id)
        return str(get_game_instance(game_obj_id))

