from flask import (Flask, g)
from .ap import (api as api_blueprint)
import boto3

app = Flask(__name__)

app.register_blueprint(api_blueprint)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

g.table_devops = dynamodb.Table('devops-challenge')

if __name__ == '__main__':
    app.run()
