from flask_restful import Resource
from flask import request
from bson import ObjectId
from dao.gameInstance import get_game_instance , make_move
from dao.user import get_user_by_id
from dao.move import make_move_entry
from validators.move import validate_move_obj , validate_move, get_winner ,check_status
from utils.constants import final_status
from dao.session import get_session
from views.gameInstance import single

class Move(Resource):
    
    def get(self):
        params = request.args.to_dict()
        game_obj_id = ObjectId(params["gi_id"])
        return single(get_game_instance(game_obj_id))
    
    def post(self):
        payload = request.json
        #if not validate_move_obj(payload):
            #return {"response" : "Bad request"}, 401
        game_obj_id = ObjectId(payload['gi_id'])
        curr_player = ObjectId(payload['curr_player'])
        next_player = ObjectId(payload['next_player'])
        proposed_state = payload['cstate']
        user_token = payload['token']

        if not (get_user_by_id(next_player) or get_user_by_id(curr_player)) :
            return {"response" : "User not found"}, 404

        user_session = get_session(user_token)
        if not user_session :
            return {"response" : "You Have To LogIn Again"}, 401

        if not (user_session["user"] == curr_player):
            return {"response" : "Bad request"}, 401
        
        game_instance = get_game_instance(game_obj_id)

        if not (curr_player == game_instance["next_player"]):
            return {"response" : "Not Your Turn"}, 401
        if not game_instance :
            return {"response" : "GameInstance not found"}, 404
        
        if not (next_player == game_instance['user1'] or next_player == game_instance['user2']) :
            return {"response" : "Bad request"}, 401 # ******

        if not validate_move(proposed_state,next_player,game_instance) :
            return {"response" : "Invalid Move"}, 401
        
        make_move_entry(game_obj_id,next_player,proposed_state)

        winner = get_winner(proposed_state,game_instance['user1'],game_instance['user2'])
        if not winner:
            make_move(game_obj_id,proposed_state,next_player,check_status(proposed_state)) 
        else:
            make_move(game_obj_id,proposed_state,next_player,final_status,winner)

        return single(get_game_instance(game_obj_id)) 

