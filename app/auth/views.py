from . import auth
from flask import render_template

@auth.route('/auth')
def auth():
    title = 'authentication for the pitch'
    return render_template('auth/auth.html',title = title)