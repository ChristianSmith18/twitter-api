from app import db
import uuid,json
from sqlalchemy.sql import expression
from marshmallow import Schema,fields
import datetime
from sqlalchemy.dialects.postgresql import JSON

class Tweet(db.Model):
    __tablename__    = 'Tweet'
    Id                = db.Column(db.String(36), primary_key=True)
    TweetInfo         = db.Column(db.JSON)
    TweetTokenization = db.Column(db.JSON)

    def __repr__(self):
        info = 'Id: {} tweetInfo: {}>'
        return info.format(
            self.Id,
            self.TweetInfo
        )

class TweetSchema(Schema):
    Id                = fields.UUID()
    TweetInfo         = fields.Str()
    TweetTokenization = fields.Str()
