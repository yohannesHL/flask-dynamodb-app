import boto3


def get_dynamodb(aws_region, aws_access_key, aws_secret_key):
    '''Returns the AWS dynamodb resource using supplied credentials.
    
    Args:
        aws_region (str): Region name (ex: eu-west-2)
        aws_access_key (str): AWS access key for the resource
        aws_secret_key: AWS secret access key for the given access key
    Returns:
        boto3.resources.base.ServiceResource: A dynamodb service resource.
    '''
    return boto3.resource('dynamodb',
                          region_name=aws_region,
                          aws_access_key_id=aws_access_key,
                          aws_secret_access_key=aws_secret_key)


def init_db(resource, app):
    '''Initialise the db .
    Args:
        resource (boto3.resources.base.ServiceResource): A dynamodb resource
        app (flask.Flask): The flask application instance
    '''

    app.tables = dict(
        devops_challenge=resource.Table(app.config.get('TABLE_NAME')))
