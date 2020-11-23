from app import app
from flask import jsonify
import json,jwt
from collections import namedtuple
from datetime import datetime

class Utils:
    def jsonToObject(data,objectName):
        return json.loads(data, object_hook=lambda d: namedtuple(objectName, d.keys())(*d.values()))

    def checkDifferenceBetweenDates(d1, d2):
        d1 = datetime.strptime(d1, "%Y-%m-%dT%H:%M:%S")
        d2 = datetime.strptime(d2, "%Y-%m-%dT%H:%M:%S")
        if d2 > d1:
            return True
        return False