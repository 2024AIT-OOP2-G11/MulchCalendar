from peewee import SqliteDatabase
from .db import db
from .user import User

MODELS = [
    User,
]

# データベースの初期化関数
def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()