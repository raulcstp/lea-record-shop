from functools import wraps
from app import app
from flask import request, jsonify
from .customers import customer_by_username
import jwt
from werkzeug.security import check_password_hash


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"message": "token is missing", "data": []}), 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
            current_user = customer_by_username(username=data["username"])
            if not current_user.is_active:
                return (
                    jsonify({"message": "This user is inactive", "data": []}),
                    401,
                )
        except Exception:
            return (
                jsonify({"message": "token is invalid or expired", "data": []}),
                401,
            )
        return f(current_user, *args, **kwargs)

    return decorated


def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return (
            jsonify(
                {
                    "message": "could not verify",
                    "WWW-Authenticate": 'Basic auth="Login required"',
                }
            ),
            401,
        )
    user = customer_by_username(auth.username)
    if not user:
        return jsonify({"message": "user not found", "data": []}), 401

    if user and check_password_hash(user.password, auth.password) and user.is_active:
        token = jwt.encode({"username": user.username}, app.config["SECRET_KEY"])
        return jsonify(
            {"message": "Validated successfully", "token": token.decode("UTF-8")}
        )

    return (
        jsonify(
            {
                "message": "could not verify",
                "WWW-Authenticate": 'Basic auth="Login required"',
            }
        ),
        401,
    )
