from flask import Flask
from flask_restful import Api
from flask_restful import Resource 
from flask_restful import reqparse
from app.main.models.my_own_API import User

app = Flask(__name__)
api = Api(app)

api.add_resource(User, "/user/<string:name>")

app.run(debug=True)