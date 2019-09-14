from . import auth
from flask import render_template,redirect,url_for
from .forms import RegistrationForm
from .. import db
from ..models import User 

@auth.route('/login')
def authentication():
    title = 'authentication for the pitch'
    return render_template('auth/auth.html',title = title)


@auth.route('/registration', methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data,email = form.email.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.authentication'))
    title = 'New Account Registration'
    return render_template('auth/registration.html',title = title,registration_form = form)
