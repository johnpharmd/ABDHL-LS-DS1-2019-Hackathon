import os
from peewee import Model, CharField
from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))


class SongRetrieved(Model):
    code = CharField(max_length=255, unique=True)
    # value = IntegerField()
    
    class Meta():
        database = db

