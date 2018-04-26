from flask import Flask
from flask_restful import Resource, Api
from business_logic.serviceapis.ping import Ping
from business_logic.serviceapis.user import User
from business_logic.serviceapis.validation import UserValidation
from business_logic.serviceapis.gameInstance import GameInstance 
from business_logic.serviceapis.move import Move 
from business_logic.serviceapis.request import Requests

from flask import request 
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(Ping, '/gameservice/ping')
api.add_resource(User, '/gameservice/user','/gameservice/user/<string:user_id>')
api.add_resource(UserValidation, '/gameservice/uservalidation')
api.add_resource(GameInstance, '/gameservice/gameinstance')
api.add_resource(Requests, '/gameservice/requests')
api.add_resource(Move,'/gameservice/move')

 
if __name__ == '__main__':
    app.run(debug=True , port = 6756)
