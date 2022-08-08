from datetime import datetime
from app import db
from flask import request, jsonify
from app.models.disks import Disks, disk_schema, disks_schema
from app.utils.sql import create_filters


def get_disks():
    filters = {
        "name": request.args.get("name"),
        "genre": request.args.get("genre"),
        "release_year": request.args.get("release_year"),
        "artist": request.args.get("artist"),
    }
    filters = {key: value for key, value in filters.items() if value}
    
    if filters:
        filters = create_filters(model=Disks, filters=filters)
        disks = Disks.query.filter(*filters, Disks.visibility_date < datetime.now()).all()
    else:
        disks = Disks.query.filter(Disks.visibility_date < datetime.now()).all()

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
    name = request.json.get("name")
    genre = "rock"
    release_year = "2020"
    artist = "test"
    quantity = 1
    visibility_date = ""

    disk = disk_by_name(name)
    if disk:
        result = disk_schema.dump(disk)
        return jsonify({"message": "disk already exists", "data": {}})

    disk = Disks(
        name=name,
        genre=genre,
        release_year=release_year,
        artist=artist,
        quantity=quantity,
        visibility_date=visibility_date
    )

    try:
        db.session.add(disk)
        db.session.commit()
        result = disk_schema.dump(disk)
        return jsonify({"message": "successfully registered", "data": result}), 201
    except Exception:
        return jsonify({"message": "unable to create", "data": {}}), 500


def update_disk(id):
    name = request.json["name"]
    disk = Disks.query.get(id)

    if not disk:
        return jsonify({"message": "disk doesn't exist", "data": {}}), 404

    try:
        disk.name = name
        db.session.commit()
        result = disk_schema.dump(disk)
        return jsonify({"message": "successfully updated", "data": result}), 201
    except Exception:
        return jsonify({"message": "unable to update", "data": {}}), 500


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
