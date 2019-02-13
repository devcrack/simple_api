import os 

base_dir = os.path.abspath(__file__)

class Config:
    secret_key = os.getenv('SECRET_KEY', 'mientras123' )
    DEBUG = False

