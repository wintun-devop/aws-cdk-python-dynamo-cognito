import boto3
from botocore.exceptions import ClientError
from env import client_id,user_pool_id

cognito_client = boto3.client('cognito-idp')

""" login """
def user_login(username, password):
    try:
        response = cognito_client.initiate_auth(
        ClientId=client_id,
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
        'USERNAME': username,
        'PASSWORD': password
        })
        print("login_success",response)
        return {"status":"success","code":200,"result":response}
    except ClientError as error:
        print("login_error",error)
        return {"status":"error","code":400}
    
""" singup """
def user_signup(username,password):
    try:
        response = cognito_client.sign_up(
            ClientId=client_id,
            Username=username,
            Password=password
        )
        print("reg_succes",response)
        return {"status":"success","code":200,"result":response}
    except ClientError as error:
        print("register_error",error)
        return {"status":"error","code":400}
    
""" confirm signup """
def user_confirm_signup(username,code):
    try:
        response = cognito_client.confirm_sign_up(
        ClientId=client_id,
        Username=username,
        ConfirmationCode=code
        )
        print("confirm_singup_succes",response)
        return {"status":"success","code":200,"result":response}
    except ClientError as error:
        print("confirm_singup_error",error)
        return {"status":"error","code":400}
    