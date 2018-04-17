from flask import Flask

app = Flask(__name__)

from app import routes

print('Home 1 commit')
