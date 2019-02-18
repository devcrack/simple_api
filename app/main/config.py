import os 

dir_path = os.path.dirname(__file__)
base_dir = os.path.abspath(dir_path)

class Config:
    secret_key = os.getenv('SECRET_KEY', 'mientras123' )
    DEBUG = False

class Development_Config(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'flask_boilerplate_main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Testing_Config(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Production_Config(Config):
    DEBUG = False

config_by_name = dict(
    dev = Development_Config,
    test = Testing_Config,
    prod = Production_Config
)

