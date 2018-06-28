import os
base_dir = os.path.abspath(os.path.dirname(__file__))

print('!!!')
print(__file__)
print(base_dir)

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