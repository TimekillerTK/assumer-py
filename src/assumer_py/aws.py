import boto3
from botocore import exceptions
import assumer_py.colours as col

sts = boto3.client('sts')

# Check identity of current user
def check_sts_identity():
    try:
        identity = sts.get_caller_identity()
    except exceptions.UnauthorizedSSOTokenError as error:
        print(f'{col.red}')
        
    return identity