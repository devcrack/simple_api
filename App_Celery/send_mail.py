from flask import Flask, request, render_template, session
from flask import  flash, redirect, url_for
from flask_mail import Mail, Message
import cfg

app = Flask(__name__)

app.config.from_object('cfg.Development_Config')


mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    #Aqui entra por cuenta del navegador web
    if request.method == 'GET':
        return render_template('index.html', email=session.get('email', ''))
    #Aqui entra por cuenta de la accion del Formulario    
    email = request.form['email']
    session['email'] = email
    
    msg = Message('Hello from Flask, coming soon in HipCC', recipients=[request.form['email']])
    #msg = Message('Hello Bitch', recipients = ['aurelio.hdz.aguilar@gmail.com']) ##Version Antigua
    msg.body = 'Esto es una simple prueba de Flask Mail\nCaracteristica proximamente en HipCC'
    if request.form['submit'] == 'Send':
        mail.send(msg)
        flash('Sending email to {0}'.format(email))
        #return 'Message Sent'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)