import json

from app import db
from flask import request, jsonify
from app.models.orders import (
    Orders,
    order_schema,
    order_filter_schema,
    orders_schema,
)
from app.utils.sql import create_like_filters



def get_orders():
    filters_json = json.loads(json.dumps(request.args))
    errors = order_filter_schema.validate(filters_json)

    if errors:
        return jsonify({"message": "Invalid request", "data": errors}), 400

    filters = order_filter_schema.load(json.loads(json.dumps(request.args)))
    if filters:
        filters = create_like_filters(model=Orders, filters=filters)
        orders = Orders.query.filter(*filters).all()
    else:
        orders = Orders.query.all()
    if orders:
        result = orders_schema.dump(orders)
        return jsonify({"message": "successfully fetched", "data": result})

    return jsonify({"message": "nothing found", "data": {}})


def get_order(id):
    order = Orders.query.get(id)
    if order:
        result = order_schema.dump(order)
        return jsonify({"message": "successfully fetched", "data": result}), 201

    return jsonify({"message": "order doesn't exist", "data": {}}), 404

def post_order(customer_id):
    errors = order_schema.validate(request.json, partial=False)

    if errors:
        return jsonify({"message": "missing fields", "data": errors}), 400

    order_data = order_schema.load(request.json)

    order = order_by_username(request.json.get("username"))

    if order:
        result = order_schema.dump(order)
        return jsonify({"message": "A costumer with this username already exists", "data": {}})

    order = Orders(**order_data)

    try:
        db.session.add(order)
        db.session.commit()
        result = order_schema.dump(order)
        return jsonify({"message": "successfully registered", "data": result}), 201
    except Exception as err:
        return jsonify({"message": "unable to create", "data": {}}), 500


def order_by_username(username):
    try:
        return Orders.query.filter(Orders.username == username).one()
    except:
        return None
