import os
#from sqlalchemy.dialects.mssql import pymssql
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    DATABASE = 'pythonDb'
    PASSWORD = '123'
    USER = 'user_api'
    HOSTNAME = 'db-python'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s'%(USER, PASSWORD, HOSTNAME, DATABASE)
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user_api:123@db/UserDb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    AUTH_URL = 'http://user-api:5000/auth'
    USER_URL = 'http://user-api:5000/'
    JWT_SECRET_KEY = 'p9Bv<3Mid9%$i02'
    