import os
class Config:
    '''
    Primary configurations for the application
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
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