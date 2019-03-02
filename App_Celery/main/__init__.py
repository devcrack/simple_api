from flask import Flask 
from flask_mail import Mail
from celery import Celery 

app = Flask(__name__)
#We load configuration from config.Development_Config.. as we can see
app.config.from_object('config.Development_Config') 

#Create of mail object from flask_mail
mail = Mail(app)

#Create of celery object for app
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])

#celery.conf.update(app.config)

