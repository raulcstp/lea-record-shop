from app import app
from ..views import helper


@app.route("/v1/authenticate", methods=["POST"])
def authenticate():
    return helper.auth()
