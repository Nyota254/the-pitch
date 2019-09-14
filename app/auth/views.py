from . import auth
from flask import render_template,redirect,url_for,flash,request
from .forms import RegistrationForm,LoginForm
from .. import db
from ..models import User 
from flask_login import login_user

@auth.route('/login',methods = ['POST','GET'])
def authentication():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,remember=login_form.remember.data)
        else:
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or password')
    title = 'authentication for the pitch'
    return render_template('auth/login.html',login_form = login_form,title = title)


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
