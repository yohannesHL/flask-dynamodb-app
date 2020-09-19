from flask import (Flask)
from app.db import init_db, get_dynamodb
from app.api.routes import (api as api_blueprint)


def create_app():

    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    app.register_blueprint(api_blueprint)
    return app


app = create_app()

dynamodb = get_dynamodb(
    app.config.get('AWS_REGION'),
    app.config.get('AWS_KEY'),
    app.config.get('AWS_SECRET'),
)

init_db(dynamodb, app)

if __name__ == '__main__':
    app.run()
