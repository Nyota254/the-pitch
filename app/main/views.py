from . import main
from flask import render_template,redirect,url_for
from flask_login import login_required,current_user,login_user,logout_user
from .forms import PitchUploadForm,CommentsForm
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


@main.route('/pitchdiscussion/<int:pitch_id>/comment',methods=['POST','GET'])
@login_required
def comment(pitch_id):
    comment = CommentsForm()
    current_pitch = Pitch.query.filter_by(id = pitch_id).first()
    if comment.validate_on_submit():
        comment = comment.comment.data
        new_comment = Comment(comment = comment,user = current_user,pitch = current_pitch)
        db.session.add(new_comment)
        db.session.commit()
        # return redirect(url_for('.comment'))
    pitch = Pitch.query.get_or_404(pitch_id)
    comments = Comment.get_comments(pitch_id)
    # comments = Comment.query.all()
    title = 'Pitch Discussion'
    return render_template('pitchdiscussion.html',title = title,pitch = pitch,comment_form = comment,comments=comments)
