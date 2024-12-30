from peewee import Model,CharField,DateTimeField,ForeignKeyField
from .user import User
from .db import db

class Event(Model):
    title = CharField()
    start = DateTimeField()
    end = DateTimeField()
    user = ForeignKeyField(User, backref='events')
    
    class Meta:
        database = db