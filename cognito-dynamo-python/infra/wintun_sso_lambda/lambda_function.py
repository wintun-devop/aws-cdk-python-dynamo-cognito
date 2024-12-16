import logging,json
from api_resources import api_paths,api_requests
from build_response import buildResponse

# Python Logging Service
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info(event)
    httpMethod = event['httpMethod']
    path = event['path']
    if httpMethod == api_requests['get'] and path == api_paths['health']:
        response = buildResponse(200,{"message":"API is healthly and working ok."})
    else:
        response= buildResponse(400,{"message":"Out of api!"})
    return response