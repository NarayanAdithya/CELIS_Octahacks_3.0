import os
basedir=os.path.abspath(os.path.dirname(__file__))

class config(object):
    SECRET_KEY= os.environ.get('SECRET_KEY') or '334nadnj&&89Ydau89YAd98adbszmdi3*&&923kln'
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or \
        'sqlite:///'+os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['narayanadithya1234@gmail.com','aravindharinarayanan111@gmail.com','sonusvareed@gmail.com']

