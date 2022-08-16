import datetime
from app import db
from marshmallow import Schema, fields


class Orders(db.Model):
    __table_args__ = (db.UniqueConstraint("disk_id", "disk_amount_left"),)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    disk_id = db.Column(db.Integer, db.ForeignKey("disks.id"), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    disk_amount_left = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    customer = db.relationship("Customers")
    disk = db.relationship("Disks")

    def __init__(self, disk_id, customer_id, amount, disk_amount_left):
        self.disk_id = disk_id
        self.customer_id = customer_id
        self.amount = amount
        self.disk_amount_left = disk_amount_left


class OrdersSchema(Schema):
    id = fields.Int()
    disk_id = fields.Int(required=True)
    customer_id = fields.Int()
    amount = fields.Int(required=True)
    disk_amount_left = fields.Int()
    created_at = fields.DateTime()
    from_date = fields.Date()
    to_date = fields.Date()


order_schema = OrdersSchema()
order_filter_schema = OrdersSchema(
    exclude=("id", "created_at", "amount", "disk_id", "disk_amount_left"), partial=True
)
orders_schema = OrdersSchema(many=True)
