from celery import shared_task
from flask_mail import Mail, Message
from flask import current_app

@shared_task
def send_A_mail(recipient):
    mail = Mail(current_app)
    
    msg = Message('Calculo Finalizado HipCC', recipients=[recipient])
    
    msg.body = '{:.2%}'.format(60) +' de avanze en el desarrollo de microservicios para HipCC.\nEnviado desde Celery'
    mail.send(msg)
    return 'Mail sent' + recipient