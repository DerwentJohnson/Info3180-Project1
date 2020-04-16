from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SECRET_KEY = "change this to be a more random key"
SQLALCHEMY_DATABASE_URI = 'postgresql://umtkumbfvedjlk:5dae1bc6c44a647841f8838351db9317ee2b8f5dcd38a8d0faf90d4ed7bba3a7@ec2-23-20-129-146.compute-1.amazonaws.com:5432/dckbe76c50r1ds'
SQLALCHEMY_TRACK_MODIFICATIONS = True # added just to suppress a warning
UPLOAD_FOLDER = './app/static/uploads'

app.config.from_object(__name__)

db = SQLAlchemy(app)

from app import views
