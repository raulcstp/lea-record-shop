from app import app
from app.views import orders, helper


@app.route("/v1/orders", methods=["GET"])
def get_orders():
    return orders.get_orders()


@app.route("/v1/orders/<id>", methods=["GET"])
def get_order(id):
    return orders.get_order(id)


@app.route("/v1/orders", methods=["POST"])
@helper.token_required
def post_orders(current_customer):
    return orders.post_order(customer_id=current_customer.id)

