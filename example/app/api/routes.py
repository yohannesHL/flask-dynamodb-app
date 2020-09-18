from flask import (Blueprint, current_app, jsonify)

api = Blueprint('example_api', __name__, url_prefix='/')


@api.route('/health', methods=('GET', ))
def get_health():
    return jsonify(container=current_app.config.get('CONTAINER_URL'),
                   project=current_app.config.get('PROJECT_URL'),
                   status='healthy')


@api.route('/secret', methods=('GET', ))
def get_secret():
    table = current_app.tables.get('devops_challenge')

    if table is None:
        raise Exception('table not found')

    result = table.get_item(Key={'code_name': 'thedoctor'})
    return jsonify(result.get('Item'))
