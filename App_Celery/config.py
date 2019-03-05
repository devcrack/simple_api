# Flask-Email Configuration 
import os

dir_path = os.path.dirname(__file__)
base_dir = os.path.abspath(dir_path)


class BaseConfig:
    SECRET_KEY = os.urandom(24)
    SESSION_COOKIE_SECURE = True
    EMAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'jaha.devcrack@gmail.com'
    MAIL_PASSWORD = 'LINUX.06anime'
    MAIL_DEFAULT_SENDER = 'devcrack'
    #CELERY_BROKER_URL =  'amqp://devcrack:mientras123@192.168.100.5:5672'
    CELERY_BROKER_URL =  'amqp://guest@localhost//'
    CELERY_RESULT_BACKEND = 'mongodb://user:mientras123@ds157574.mlab.com:57574/connect_to_mongo'
    
class Development_Config(BaseConfig):
    DEBUG = True


