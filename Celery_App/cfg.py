import os

dir_path = os.path.dirname(__file__)
base_dir = os.path.abspath(dir_path)

class BaseConfig:
    SECRET_KEY = os.urandom(24)
    SESSION_COOKIE_SECURE = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'jaha.devcrack@gmail.com'
    MAIL_PASSWORD = 'LINUX.06anime'
    MAIL_DEFAULT_SENDER = 'devcrack'
    CELERY_BROKER_URL =  'amqp://guest@localhost//'
    CELERY_RESULT_BACKEND = 'mongodb://user:mientras123@ds157574.mlab.com:57574/connect_to_mongo'
    CELERY_INCLUDE = ['task_s.mail_tasks']   

class Development_Config(BaseConfig):
    DEBUG = True