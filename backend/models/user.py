from mongo_engine import db

class User(db.Document):
    name = db.StringField(required=True)
    mobile = db.StringField(required=True)