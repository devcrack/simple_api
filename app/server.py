from flask import Flask
from flask_restful import Api
from flask_restful import Resource 
from flask_restful import reqparse


app = Flask(__name__)
api = Api(app)

""" Stupid Source Data """
user = [
        {
            "name":"Roberto",
            "age":60,
            "occupation":"Electronic Technique"
        },
        {
            "name":"Jonas",
            "age":18,
            "occupation":"Nini"
        },
        {
            "name":"Aurelio",
            "age":26,
            "occupation":"Not know what the fuck do with his life"        
        }
    ]

