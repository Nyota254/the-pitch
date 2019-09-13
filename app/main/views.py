from . import main
from flask import render_template

@main.route('/')
def index():
    title='Welcome to the pitch'
    return render_template('index.html',title=title)