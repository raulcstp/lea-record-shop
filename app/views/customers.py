from app import db
from flask import request, jsonify
from werkzeug.security import generate_password_hash
from app.models.customers import Customers, customer_schema, customers_schema
from app.utils.sql import create_filters


def get_customers():
    filters = {
        "name": request.args.get("name"),
        "birth_date": request.args.get("birth_date"),
        "document": request.args.get("document"),
        "email": request.args.get("email"),
        "phone": request.args.get("phone"),
        "username": request.args.get("username"),
    }
    filters = {key: value for key, value in filters.items() if value}
    if filters:
        filters = create_filters(model=Customers, filters=filters)
        customers = Customers.query.filter(*filters).all()
    else:
        customers = Customers.query.all()
    if customers:
        result = customers_schema.dump(customers)
        return jsonify({"message": "successfully fetched", "data": result})

    return jsonify({"message": "nothing found", "data": {}})


def get_customer(id):
    customer = Customers.query.get(id)
    if customer:
        result = customer_schema.dump(customer)
        return jsonify({"message": "successfully fetched", "data": result}), 201

    return jsonify({"message": "customer don't exist", "data": {}}), 404


def post_customer():
    username = request.json["username"]
    password = request.json["password"]
    name = request.json["name"]
    email = request.json["email"]
    document = request.json["document"]
    birth_date = request.json["birth_date"]
    phone = request.json["phone"]

    customer = customer_by_username(username)
    if customer:
        result = customer_schema.dump(customer)
        return jsonify({"message": "customer already exists", "data": {}})

    pass_hash = generate_password_hash(password)
    customer = Customers(
        username=username,
        password=pass_hash,
        name=name,
        email=email,
        document=document,
        birth_date=birth_date,
        phone=phone,
    )

    try:
        db.session.add(customer)
        db.session.commit()
        result = customer_schema.dump(customer)
        return jsonify({"message": "successfully registered", "data": result}), 201
    except Exception:
        return jsonify({"message": "unable to create", "data": {}}), 500


def update_customer(id):
    username = request.json["username"]
    password = request.json["password"]
    name = request.json["name"]
    email = request.json["email"]
    customer = Customers.query.get(id)

    if not customer:
        return jsonify({"message": "customer doesn't exist", "data": {}}), 404

    pass_hash = generate_password_hash(password)

    if customer:
        try:
            customer.username = username
            customer.password = pass_hash
            customer.name = name
            customer.email = email
            db.session.commit()
            result = customer_schema.dump(customer)
            return jsonify({"message": "successfully updated", "data": result}), 201
        except Exception:
            return jsonify({"message": "unable to update", "data": {}}), 500


def delete_customer(id):
    customer = Customers.query.get(id)
    if not customer:
        return jsonify({"message": "customer don't exist", "data": {}}), 404

    if customer:
        try:
            customer.is_active = False
            db.session.commit()
            result = customer_schema.dump(customer)
            return jsonify({"message": "successfully deleted", "data": result}), 200
        except Exception:
            return jsonify({"message": "unable to delete", "data": {}}), 500


def customer_by_username(username):
    try:
        return Customers.query.filter(Customers.username == username).one()
    except:
        return None
