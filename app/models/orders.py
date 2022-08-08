from app import db, ma


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    disk_id = db.Column(db.Integer, db.ForeignKey("disks.id"), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    customer = db.relationship("Customers")
    disk = db.relationship("Disks")

    def __init__(self, disk_id, customer_id, quantity):
        self.disk_id = disk_id
        self.customer_id = customer_id
        self.quantity = quantity


class OrdersSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "description", "customer_id", "created_on")


order_schema = OrdersSchema()
orders_schema = OrdersSchema(many=True)
