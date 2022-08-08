import os
import random
import string

db_user_name = os.environ['db_user_name']
db_password = os.environ['db_password']
db_name = os.environ['db_name']
db_endpoint = os.environ['db_endpoint']
gen = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(gen) for i in range(12))


SQLALCHEMY_DATABASE_URI = f'postgresql://{db_user_name}:{db_password}@{db_endpoint}/{db_name}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key
DEBUG = True
