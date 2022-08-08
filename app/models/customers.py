import datetime
from app import db, ma


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    document = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    birth_date = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    is_active = db.Column(db.Boolean, default=True)
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


class CustomersSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "document",
            "birth_date",
            "phone",
            "username",
            "name",
            "email",
            "password",
            "created_at",
            "updated_at",
        )


customer_schema = CustomersSchema()
customers_schema = CustomersSchema(many=True)
