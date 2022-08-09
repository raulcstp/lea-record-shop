import datetime

from app import db
from marshmallow import Schema, fields



class Disks(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    release_year = db.Column(db.String(4), nullable=False)
    artist = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    visibility_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now()
    )

    def __init__(
        self,
        name,
        genre,
        release_year,
        artist,
        quantity,
        visibility_date=datetime.datetime.now(),
    ):
        self.name = name
        self.genre = genre
        self.release_year = release_year
        self.artist = artist
        self.quantity = quantity
        self.visibility_date = visibility_date


class DisksSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    genre = fields.Str(required=True)
    release_year = fields.Str(required=True)
    artist = fields.Str(required=True)
    quantity = fields.Int(required=True)
    visibility_date = fields.DateTime(error_messages={
        "invalid": "Not a valid date with format yyyy-mm-ddThh:mm:ss"
    })
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

disk_schema = DisksSchema()
disk_filter_schema = DisksSchema(exclude=("id", "created_at", "updated_at", "visibility_date"))
disks_schema = DisksSchema(many=True)
