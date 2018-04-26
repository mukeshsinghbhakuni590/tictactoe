from flask_restful import Resource
from flask import request
from bson import ObjectId
from dao.gameInstance import get_requested_game_instances
from dao.user import get_user_by_id
from views.gameInstance import multiple

class Requests (Resource):
    
    def get(self):
        params = request.args.to_dict()
        user_obj_id = ObjectId(params['user_id'])
        if not get_user_by_id(user_obj_id) :
            return {"response" : "User not found"}, 404
            
        return multiple (get_requested_game_instances(user_obj_id))
