import cfg 
from celery import Celery 
from flask import Flask,request, render_template, session
from flask import  flash, redirect, url_for, jsonify
from task_s.make_celery import make_celery
from task_s.mail_tasks import *

app = Flask(__name__)

app.config.from_object('cfg.Development_Config')


celery = make_celery(app)


#print(celery.conf)

@app.route('/send_mail', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', email=session.get('email', ''))
    email = request.form['email']
    session['email'] = email
    if request.form['submit'] == 'Send':
        print('Sending Mail')
        send_A_mail.delay(email)
        flash('Sending email to {0}'.format(email))
    else:
        print('Mail will be sent in one minute')
        send_A_mail.apply_async(args=[email], countdown=60)
        flash('Sending email to {0}'.format(email))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
