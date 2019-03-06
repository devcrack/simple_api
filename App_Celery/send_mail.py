from flask import Flask 
from flask_mail import Mail, Message
import cfg

app = Flask(__name__)

app.config.from_object('cfg.Development_Config')


mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hello Bitch', recipients = ['aurelio.hdz.aguilar@gmail.com'])

    msg.body = 'Esta madre esta media perra\npero que cojones tio'
    mail.send(msg)
    return 'Message Sent'

if __name__ == '__main__':
    app.run(debug=True)