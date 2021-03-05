import os

SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY')
