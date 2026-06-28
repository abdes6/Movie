import os
import pytest

os.environ['USE_MOCK_FALLBACK'] = 'true'

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def popular_data(client):
    resp = client.get('/api/movie/popular')
    assert resp.status_code == 200
    return resp.get_json()
