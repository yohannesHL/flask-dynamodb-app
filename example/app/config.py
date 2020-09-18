from os import environ


class Config:
    '''The default configuration object for the app.
    '''
    CONTAINER_URL = environ.get('CONTAINER_URL')
    PROJECT_URL = environ.get('PROJECT_URL')
    TABLE_NAME = environ.get('TABLE_NAME')
    AWS_REGION = environ.get('AWS_REGION')
    AWS_KEY = environ.get('AWS_KEY')
    AWS_SECRET = environ.get('AWS_SECRET')
