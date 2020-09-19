import unittest
from unittest.mock import patch
from app.db import get_dynamodb, init_db


class MockResource():
    def Table(self, name):
        return {'name': name}


class TestDB(unittest.TestCase):
    @patch('flask.Flask')
    def test_init_db(self, Flask):
        mock_application = Flask()
        mock_application.config = {'TABLE_NAME': 'exampletable'}
        init_db(MockResource(), mock_application)

        self.assertDictEqual(
            mock_application.tables.get('devops_challenge'),
            {'name': 'exampletable'},
        )

    @patch('boto3.resource')
    def test_get_dynamodb(self, resource):
        get_dynamodb('region', 'key', 'secret')

        self.assertTrue(resource.called)
        resource.assert_called_with('dynamodb',
                                    region_name='region',
                                    aws_access_key_id='key',
                                    aws_secret_access_key='secret')
