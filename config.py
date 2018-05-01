import os
base_dir = os.path.abspath(os.path.dirname(__file__))

print('!!!')
print(__file__)
print(base_dir)

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-never-will-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(base_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False