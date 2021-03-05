import os

from flask_sqlalchemy import SQLAlchemy
from googleapiclient.discovery import build

db = SQLAlchemy()
youtube = build('youtube',
                'v3',
                developerKey=os.environ.get('YOUTUBE_API_KEY'))
