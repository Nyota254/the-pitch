class Config:
    '''
    Primary configurations for the application
    '''
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://kevin:1234@localhost/pitchesdb"
    SECRET_KEY = 'testkey'
class DevConfig(Config):
    '''
    Development Configuratons
    '''
    DEBUG = True
class ProdConfig(Config):
    '''
    Production Configurations
    '''
    pass

configurations = {
    'development':DevConfig,
    'production':ProdConfig
}