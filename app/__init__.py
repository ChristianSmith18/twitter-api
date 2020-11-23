from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object(Config)
app.debug = True
db = SQLAlchemy(app)

from app.routes import Twitter
