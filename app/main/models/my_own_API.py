
from flask_restful import Resource
#from ..models import users
from . import users


class User(Resource):
    def get(self, name):
        for user  in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 400
