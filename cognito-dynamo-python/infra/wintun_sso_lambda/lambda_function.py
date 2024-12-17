import logging,json
from api_resources import api_paths,api_requests
from build_response import buildResponse
from services.cognito import user_login,user_confirm_signup,user_signup

# Python Logging Service
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    # logger.info(event)
    httpMethod = event['httpMethod']
    path = event['path']
    if httpMethod == api_requests['get'] and path == api_paths['health']:
        response = buildResponse(200,{"status":"success","message":"API is healthly and working ok."})
    elif httpMethod == api_requests['post'] and path == api_paths['register']:
        req_body = json.loads(event["body"])
        resp = user_signup(req_body["username"],req_body["password"])
        if resp["status"]=="error":
            return buildResponse(400,{"status":"error","message":"register error."})
        return buildResponse(201,{"status":"success","message":"register success.","result":resp["result"]})
    elif httpMethod == api_requests['post'] and path == api_paths['register_confirm']:
        req_body = json.loads(event["body"])
        resp = user_confirm_signup(req_body["username"],req_body["code"])
        if resp["status"]=="error":
            return buildResponse(400,{"status":"error","message":"register confirm error."})
        return buildResponse(200,{"status":"success","message":"regiser confirm success.","result":resp["result"]})
    elif httpMethod == api_requests['post'] and path == api_paths['login']:
        req_body = json.loads(event["body"])
        resp = user_login(req_body["username"],req_body["password"])
        if resp["status"]=="error":
            return buildResponse(400,{"status":"error","message":"login error."})
        return buildResponse(200,{"status":"success","message":"login success.","result":resp["result"]})
    else:
        response= buildResponse(400,{"status":"error","message":"Out of api!"})
    return response