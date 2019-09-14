from . import main
from flask_wtf import FlaskForm
from wtforms.fields import SubmitField,StringField,TextAreaField,SelectField
from wtforms.validators import Required

def PitchUploadForm(FlaskForm):
    pitch = StringField('Pitch',validators=[Required()])
    category = SelectField('')