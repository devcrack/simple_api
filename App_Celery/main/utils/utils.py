from flask import request, session, render_template, flash, redirect
from flask import url_for
from flask_mail import Message
from .. import mail
from .. import app


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', email=session.get('email', ''))
    email = request.form['email']
    session['email'] = email

    # send the email
    msg = Message('Hello from Flask',
                  recipients=[request.form['email']])
    msg.body = 'This is a test email sent from a background Celery task.'
    if request.form['submit'] == 'Send':
        # send right away
        send_async_email.delay(msg)
        flash('Sending email to {0}'.format(email))
    else:
        # send in one minute
        send_async_email.apply_async(args=[msg], countdown=60)
        flash('An email will be sent to {0} in one minute'.format(email))

    return redirect(url_for('index'))