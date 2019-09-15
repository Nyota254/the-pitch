from . import main
from flask import render_template,redirect,url_for
from flask_login import login_required,current_user,login_user,logout_user
from .forms import PitchUploadForm
from .. import db
from ..models import Pitch,Comment,User

@main.route('/')
def index():
    pitch = Pitch.get_pitch('Product')
    interview_pitch = Pitch.get_pitch('Interview')
    promotion_pitch = Pitch.get_pitch('Promotion')
    pickup_pitch = Pitch.get_pitch('Pick-up')
    title='Welcome to the pitch'
    return render_template('index.html',title=title,pitches=pitch,interview_pitch=interview_pitch,promotion_pitch=promotion_pitch,pickup_pitch=pickup_pitch)

@main.route('/addpitch',methods = ['GET','POST'])
@login_required
def add_pitch():
    form = PitchUploadForm()
    if form.validate_on_submit():
        pitch = form.pitch.data
        category = form.category.data
        new_pitch = Pitch(pitch = pitch,category = category,user = current_user)
        new_pitch.save_pitch()
        return redirect(url_for('.index'))
    title = 'Add a pitch'
    return render_template('addpitch.html',title = title,pitchform = form)


@main.route('/pitchdiscussion/comment')
@login_required
def comment():
    title = 'Pitch Discussion'
    return render_template('pitchdiscussion.html',title = title)
