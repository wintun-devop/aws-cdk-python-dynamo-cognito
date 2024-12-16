import json
from custom_encoder import CustomEncoder

#Response Build 
def buildResponse(statusCode,body=None):
    response = {
        "statusCode":statusCode,
        "headers":{
            "Content-Type": "application/json",
            "Accesss-Control-Allow-Origin": "*"
        }
    }
    if body is not None:
        response["body"]=json.dumps(body,cls=CustomEncoder)
    return response