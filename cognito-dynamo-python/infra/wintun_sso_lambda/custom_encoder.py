import json
from decimal import Decimal

""" custom encoder """
class CustomEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,Decimal):
            return float(obj)
        return json.JSONEncoder.default(self,obj)