from model import db, SongRetrieved

db.connect()
db.create_tables([SongRetrieved])

