from flask import jsonify
from . import api
from app import settings


@api.route('/health', methods=('GET'))
def health():
    return jsonify(container=settings.CONTAINER_URL,
                   project=settings.PROJECT_URL,
                   status='healthy')
