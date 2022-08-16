import datetime
from app import db
from marshmallow import Schema, fields


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    document = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False, index=True)
    password = db.Column(db.String(200), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, default=True, index=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now()
    )

    def __init__(self, document, username, password, birth_date, name, email, phone):
        self.document = document
        self.username = username
        self.password = password
        self.birth_date = birth_date
        self.name = name
        self.email = email
        self.phone = phone


class CustomersSchema(Schema):
    id = fields.Int()
    document = fields.Str(required=True)
    birth_date = fields.Date(
        required=True,
        error_messages={"invalid": "Not a valid date with format yyyy-mm-dd"},
    )
    username = fields.Str(required=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)
    is_active = fields.Bool()
    password = fields.Str(required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


customer_schema = CustomersSchema()
customer_filter_schema = CustomersSchema(
    exclude=("id", "created_at", "updated_at", "password", "is_active", "birth_date"),
    partial=True,
)
customers_schema = CustomersSchema(many=True)
