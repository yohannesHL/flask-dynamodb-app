from flask import (Flask)
from db import get_dynamodb
from api.routes import (api as api_blueprint)

app = Flask(__name__)
app.config.from_object('config.Config')
db = get_dynamodb(
    app.config.get('AWS_REGION'),
    app.config.get('AWS_KEY'),
    app.config.get('AWS_SECRET'),
)

app.tables = dict(devops_challenge=db.Table(app.config.get('TABLE_NAME')))

app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run()
