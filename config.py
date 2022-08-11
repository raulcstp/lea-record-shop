import os

db_user_name = os.environ["db_user_name"]
db_password = os.environ["db_password"]
db_name = os.environ["db_name"]
db_endpoint = os.environ["db_endpoint"]
key = "VIMs2hEyLh7o"


SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{db_user_name}:{db_password}@{db_endpoint}/{db_name}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key
DEBUG = True
