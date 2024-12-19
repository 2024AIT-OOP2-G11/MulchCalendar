from peewee import Model,CharField
from .db import db

class User(Model):
    user = CharField()
    color = CharField()
    
    class Meta:
        database = db