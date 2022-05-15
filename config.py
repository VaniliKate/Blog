import os


class Config:
    BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'        
    SECRET_KEY = 'lkjhgfdsa'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:psql@localhost/bloggy'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development': DevConfig,
'production': ProdConfig
}