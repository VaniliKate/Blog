import os
class Config:
    SECRET_KEY='thisismysupersecretkey'
    MAIL_SERVER : 'smtp.googlemail.com'
    MAIL_PORT : 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME : os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD : os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER : os.environ.get('MAIL_USERNAME')
    QUOTE_API='https://quotes.rest/{}'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URI')
    DEBUG=True
   

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')

configuration_options ={
    'development': DevConfig,
    'production': ProdConfig
}
