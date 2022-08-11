from app import app
from app.views import disks


@app.route("/v1/disks", methods=["GET"])
def get_disks():
    return disks.get_disks()


@app.route("/v1/disks/<id>", methods=["GET"])
def get_disk(id):
    return disks.get_disk(id)


@app.route("/v1/disks", methods=["POST"])
def post_disks():
    return disks.post_disk()


@app.route("/v1/disks/<id>", methods=["DELETE"])
def delete_disks(id):
    return disks.delete_disk(id)


@app.route("/v1/disks/<id>", methods=["PUT"])
def update_disks(id):
    return disks.update_disk(id)
