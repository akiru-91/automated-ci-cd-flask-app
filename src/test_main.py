import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == 'success'

def test_health(client):
    """Test the health endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_greet(client):
    """Test the greet endpoint"""
    response = client.get('/api/greet/Akiru')
    assert response.status_code == 200
    assert response.json['message'] == 'Hello, Akiru!'
