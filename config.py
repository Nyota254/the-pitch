class Config:
    '''
    Primary configurations for the application
    '''
    pass
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