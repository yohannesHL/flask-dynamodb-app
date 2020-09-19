import pytest


def test_api_get_health(client):

    expected = {
        "container": "https://hub.docker.com/r/yohanhl/flask-dynamodb-app/",
        "project": "https://github.com/yohanneshl/flask-dynamodb-app",
        "status": "healthy"
    }
    res = client.get('/health')
    assert res.json == expected


def test_api_get_secret(client):

    expected = {'code_name': 'thedoctor', 'secret_code': 'j37ACF8aHLb38JN3'}
    res = client.get('/secret')
    assert res.json == expected


def test_api_get_secret__mising_table(application, client):

    application.tables = {}

    with pytest.raises(Exception):
        client.get('/secret')
