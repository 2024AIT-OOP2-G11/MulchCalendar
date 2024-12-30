from peewee import SqliteDatabase
from .db import db
from .user import User
from .event import Event

MODELS = [
    User,
    Event,
    
]

# データベースの初期化関数
def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()