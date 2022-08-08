import datetime

from app import db, ma


class Disks(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    release_year = db.Column(db.String(4), nullable=False)
    artist = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    visibility_date = db.Column(db.DateTime)
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


class DisksSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "name",
            "genre",
            "release_year",
            "artist",
            "quantity",
            "visibility_date",
            "created_at",
            "updated_at",
        )


disk_schema = DisksSchema()
disks_schema = DisksSchema(many=True)
