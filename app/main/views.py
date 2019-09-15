from . import main
from flask import render_template,redirect,url_for
from flask_login import login_required
from .forms import PitchUploadForm
from .. import db
from ..models import Pitch,Comment

@main.route('/')
def index():
    pitch = Pitch.get_pitch('Product')
    title='Welcome to the pitch'
    return render_template('index.html',title=title,pitches=pitch)

@main.route('/addpitch',methods = ['GET','POST'])
# @login_required
def add_pitch():
    form = PitchUploadForm()
    if form.validate_on_submit():
        pitch = form.pitch.data
        category = form.category.data
        new_pitch = Pitch(pitch = pitch,category = category)
        new_pitch.save_pitch()
        return redirect(url_for('.index'))
    title = 'Add a pitch'
    return render_template('addpitch.html',title = title,pitchform = form)


@main.route('/pitchdiscussion/comment')
@login_required
def comment():
    title = 'Pitch Discussion'
    return render_template('pitchdiscussion.html',title = title)
