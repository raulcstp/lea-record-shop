import datetime
from operator import length_hint
from app import db
from marshmallow import Schema, fields


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    disk_id = db.Column(db.Integer, db.ForeignKey("disks.id"), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    customer = db.relationship("Customers")
    disk = db.relationship("Disks")

    def __init__(self, disk_id, customer_id, quantity):
        self.disk_id = disk_id
        self.customer_id = customer_id
        self.quantity = quantity


class OrdersSchema(Schema):
    id = fields.Int()
    disk_id = fields.Int(required=True)
    customer_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    created_at = fields.DateTime()
    from_date = fields.Date()
    to_date = fields.Date()

order_schema = OrdersSchema()
order_filter_schema = OrdersSchema(exclude=("id", "created_at"))
orders_schema = OrdersSchema(many=True)
