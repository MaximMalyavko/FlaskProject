import os
from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, '.env'))

print('!!!')
print(__file__)
print(base_dir)
print('sqlite:///' + os.path.join(base_dir, 'app.db'))

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-never-will-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(base_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # ADMINS = ['my-email@example.com']
    ADMINS = ['malyavko.maxim84@gmail.com']
    # SECRET_KEY = 'secret_key_for_token'

    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'es', 'ru']
    #JA_TRANSLATOR_KEY = 'trnsl.1.1.20180705T095444Z.66a0258d85f2d5ca.78e397866c88434e90954aabd9447d27646d8d60'
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
	LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')