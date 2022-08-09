import json
from datetime import datetime
from app import db
from flask import request, jsonify
from app.models.disks import Disks, disk_schema, disk_filter_schema, disks_schema
from app.utils.sql import create_like_filters


def get_disks():
    filters_json = json.loads(json.dumps(request.args))
    errors = disk_filter_schema.validate(filters_json)

    if errors:
        return jsonify({"message": "Invalid request", "data": errors}), 400

    filters = disk_filter_schema.load(json.loads(json.dumps(request.args)))
    if filters:
        filters = create_like_filters(model=Disks, filters=filters)
        disks = Disks.query.filter(*filters).all()
    else:
        disks = Disks.query.filter(Disks.visibility_date <= datetime.now()).all()

    if disks:
        result = disks_schema.dump(disks)
        return jsonify({"message": "successfully fetched", "data": result})

    return jsonify({"message": "nothing found", "data": {}})


def get_disk(id):
    disk = Disks.query.get(id)
    if disk:
        result = disk_schema.dump(disk)
        return jsonify({"message": "successfully fetched", "data": result}), 201

    return jsonify({"message": "disk don't exist", "data": {}}), 404


def post_disk():
    errors = disk_schema.validate(request.json, partial=False)

    if errors:
        return jsonify({"message": "missing fields", "data": errors}), 400

    disk_data = disk_schema.load(request.json)

    disk = disk_by_name(disk_data.get("name"))

    if disk:
        result = disk_schema.dump(disk)
        return jsonify({"message": "disk already exists", "data": result})

    disk = Disks(**disk_data)

    try:
        db.session.add(disk)
        db.session.commit()
        result = disk_schema.dump(disk)
        return jsonify({"message": "successfully registered", "data": result}), 201
    except Exception:
        return jsonify({"message": "unable to create", "data": {}}), 500


def update_disk(id):
    errors = disk_schema.validate(request.json, partial=True)

    if errors:
        return jsonify({"message": "missing fields", "data": errors}), 400

    disk_data = disk_schema.load(request.json, partial=True)
    
    if disk_data:
        disk = Disks.query.get(id)

        if not disk:
            return jsonify({"message": "disk doesn't exist", "data": {}}), 404

        try:
            for attribute, value in disk_data.items():
                setattr(disk, attribute, value)
            db.session.commit()
            result = disk_schema.dump(disk)
            return jsonify({"message": "successfully updated", "data": result}), 201
        except Exception:
            return jsonify({"message": "unable to update", "data": {}}), 500
    
    return jsonify({"message": "no data to update", "data": {}}), 200


def delete_disk(id):
    disk = Disks.query.get(id)
    if not disk:
        return jsonify({"message": "disk don't exist", "data": {}}), 404

    try:
        db.session.delete(id)
        db.session.commit()
        result = disk_schema.dump(disk)
        return jsonify({"message": "successfully deleted", "data": result}), 200
    except Exception:
        return jsonify({"message": "unable to delete", "data": {}}), 500


def disk_by_name(name):
    try:
        return Disks.query.filter(Disks.name == name).one()
    except:
        return None
