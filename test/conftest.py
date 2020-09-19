from app.main import create_app
import pytest


@pytest.fixture
def application():
    app = create_app()
    app.config['TESTING'] = True
    return app


class MockTable():
    def get_item(self, Key=None):
        return {
            'Item': {
                'code_name': 'thedoctor',
                'secret_code': 'j37ACF8aHLb38JN3'
            }
        }


def init_test_db(resource, app):
    table = 'devops_challenge'
    app.tables = {table: MockTable()}


@pytest.fixture
def client(application):
    with application.test_client() as client:
        with application.app_context():
            init_test_db(None, application)
        yield client
