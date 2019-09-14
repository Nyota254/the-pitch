from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

class User(UserMixin,db.Model):
    '''
    This class will contain database schema for users
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,unique = True,nullable = False)
    email = db.Column(db.String,unique = True,nullable = False)
    bio = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    password_hash = db.Column(db.String,nullable=False)
    @property
    def password(self):
        '''
        Raises error when someone trys to read the password
        '''
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        '''
        Generates password hash
        '''
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        '''
        confirms password equal to the password hash during login
        '''
        check_password_hash(self.password_hash,password)

class Pitch(db.Model):
    '''
    This class will contain the database schema for picthes table
    '''
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.String)
    category = db.Column(db.String)
    users = db.relationship('User',backref='pitch',lazy = 'dynamic')\

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
