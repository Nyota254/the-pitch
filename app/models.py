from . import db

class User(db.Model):
    '''
    This class will contain database schema for users
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,unique = True,nullable = False)
    email = db.Column(db.String,unique = True,nullable = False)
    password_hash = db.Column(db.String,nullable=False)
    bio = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

class Pitch(db.Model):
    '''
    This class will contain the database schema for picthes table
    '''
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.String)
    category = db.Column(db.String)
    users = db.relationship('User',backref='pitch',lazy = 'dynamic')
