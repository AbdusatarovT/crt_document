import os
from os import environ

USER = environ.get('USER')
PASSWORD = environ.get('PASSWORD')
DB = environ.get('DB')

POSTGRES = {
    'user': USER,
    'pw': PASSWORD,
    'db': DB,
    'host': 'localhost',
    'port': '5432',
}

SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


SECRET_KEY = environ.get('SECRET_KEY')

SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
BASE_DIR = os.path.abspath('.')

