from app import app
from app.views import customers


@app.route("/v1/customers", methods=["GET"])
def get_customers():
    return customers.get_customers()


@app.route("/v1/customers/<id>", methods=["GET"])
def get_customer(id):
    return customers.get_customer(id)


@app.route("/v1/customers", methods=["POST"])
def post_customers():
    return customers.post_customer()


@app.route("/v1/customers/<id>", methods=["DELETE"])
def delete_customers(id):
    return customers.delete_customer(id)


@app.route("/v1/customers/<id>", methods=["PUT"])
def update_customers(id):
    return customers.update_customer(id)
