## AWS CLI-Access Key Config
- https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
- https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html

## virtial environment set-up(window)
```
python -m venv deploy-aws-cdk-env
```
```
deploy-aws-cdk-env\Scripts\activate
```
```
pip install aws-cdk.core
```
```
pip install constructs
```
### Vertify CDK Version
```
cdk --version
```
### create project (mkdir cognito-dynamo-python)
```
mkdir your_project_name
```
### Initializating CDK Project
```
cdk init --language python
```

### Initializing deployment
```
.\source.bat
```
```
pip install -r requirements.txt
```
```
cdk synthesize
```
### Bootstrap with Default Profile and deploy
```
cdk bootstrap
```
```
cdk deploy
```

### Bootstrap with Specific Profile and Deploy
```
cdk bootstrap your_profile
```
```
cdk deploy your_profile
```