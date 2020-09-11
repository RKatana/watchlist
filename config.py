import os
class Config:
    '''Main configuration class
    '''
    MDB_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MDB_SEARCH_URL = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')

class DevConfig(Config):
    '''Configuration for development environment
    '''
    DEBUG = True
    

class ProdConfig(Config):
    '''Configurations for production environment
    '''
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig
}