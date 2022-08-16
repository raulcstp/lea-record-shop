from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)


@app.before_first_request
def before_first_request():
    db.create_all()


from .routes import customers, disks, home, auth, orders
