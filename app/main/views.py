from . import main
from flask import render_template
from flask_login import login_required

@main.route('/')
def index():
    title='Welcome to the pitch'
    return render_template('index.html',title=title)