#Importing from website package the db object (db = SQLAlchemy())
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())

    #user.id can be lowercase because it isn't case sensitive in sql
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))




#User object is inheriting from the db model and user mixin
#All users have to look like this
class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))

    #puts notes id as like a list so we can access all the notes a user has
    #has to be capital Note here
    notes = db.relationship('Note')

