from distutils.debug import DEBUG
import os
from tkinter import ON
class Config:

   UPLOADED_PHOTOS_DEST ='app/static/photos' 
   SECRET_KEY = ('fuad1234')
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fahadbasi:333@localhost/blog'  

#    email configurations
#    MAIL_SERVER = 'smtp.googlemail.com'
#    MAIL_PORT = 587
#    MAIL_USE_TLS = True
#    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
#    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
#    DEBUG = True


class ProdConfig(Config):
    
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fahadbasi:333@localhost/blog'
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fahadbasi:333@localhost/blog_test'
        


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}  