import json
import asyncio
from app import db
from sqlalchemy.sql import func
from flask import request, jsonify
from app.models.orders import (
    Orders,
    order_schema,
    order_filter_schema,
    orders_schema,
)
from app.models.disks import Disks


def get_orders():
    filters_json = json.loads(json.dumps(request.args))
    errors = order_filter_schema.validate(filters_json)

    if errors:
        return jsonify({"message": "Invalid request", "data": errors}), 400

    filters = order_filter_schema.load(filters_json)
    if filters:
        customer_id = filters.get("customer_id")
        from_date = filters.get("from_date")
        to_date = filters.get("to_date")
        filters = [
            Orders.customer_id == customer_id if customer_id else None,
            Orders.created_at.between(from_date, to_date)
            if from_date and to_date
            else None,
        ]
        filters = list(filter(lambda item: item is not None, filters))
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


async def post_order(customer_id):
    errors = order_schema.validate(request.json, partial=False)
    if errors:
        return jsonify({"message": "error validating fields", "data": errors}), 400

    request.json["customer_id"] = customer_id
    order_data = order_schema.load(request.json)

    tasks = (
        asyncio.create_task(
            get_disk_data(disk_id=order_data.get("disk_id"))
        ),
        asyncio.create_task(get_orders_amount(
            disk_id=order_data.get("disk_id")))
    )

    disk_data, orders_amount = await asyncio.gather(*tasks)

    if not disk_data:
        return jsonify({"message": "disk not found", "data": {}}), 404

    disk_amount_left = (
        disk_data.amount if not orders_amount else disk_data.amount - orders_amount
    )

    if not disk_amount_left:
        return (
            jsonify({"message": f"there are no more disks avaiable", "data": {}}),
            200,
        )
    elif order_data.get("amount") > disk_amount_left:
        return (
            jsonify(
                {
                    "message": f"there are only {disk_amount_left} disks avaiable",
                    "data": {},
                }
            ),
            200,
        )

    order_data.update({"disk_amount_left": disk_amount_left})
    order = Orders(**order_data)

    try:
        db.session.add(order)
        db.session.commit()
        result = order_schema.dump(order)
        return (
            jsonify({"message": "successfully created order", "data": result}),
            201,
        )
    except Exception as err:
        return jsonify({"message": "unable to create order", "data": {}}), 409


def order_by_username(username):
    try:
        return Orders.query.filter(Orders.username == username).one()
    except:
        return None


async def get_disk_data(disk_id):
    return Disks.query.filter(
        Disks.id == disk_id,
    ).first()


async def get_orders_amount(disk_id):
    return Orders.query.with_entities(func.sum(Orders.amount)).filter(Orders.disk_id == disk_id).one()[0]
