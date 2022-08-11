from app import app
from flask import jsonify
from app.views import helper


@app.route("/v1", methods=["GET"])
@helper.token_required
def home(current_customer):
    return jsonify({"message": f"Hello {current_customer.name}"})
