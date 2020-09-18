from flask import (jsonify, g)
from . import api


@api.route('/secret', methods=('GET'))
def secret():
    result = g.table_devops.get_item(Key={'code_name': 'thedoctor'})
    return jsonify(result['Item'])
