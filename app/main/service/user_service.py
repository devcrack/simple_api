import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    #https://kite.com/python/docs/sqlalchemy.orm.query.Query.filter_by
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()


"""
The above code within user_service.py does the following:

    line 8 through 29 creates a new user by first checking if the user already exists; it returns a success response_object if 
    the user doesn’t exist else it returns an error code 409 and a failure response_object.
    
    line 33 and 37 return a list of all registered users and a user object by providing the public_id respectively.
    
    line 40 to 42 commits the changes to database.

    No need to use jsonify for formatting an object to JSON, Flask-restplus does it automatically 
    """