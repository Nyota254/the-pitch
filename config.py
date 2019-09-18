import os
class Config:
    '''
    Primary configurations for the application
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
class DevConfig(Config):
    '''
    Development Configuratons
    '''
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://kevin:1234@localhost/pitchesdb"
    DEBUG = True
class ProdConfig(Config):
    '''
    Production Configurations
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestConfig(Config):
    '''
    Test configurations
    '''
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://kevin:1234@localhost/pitchesdb_test"


configurations = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}