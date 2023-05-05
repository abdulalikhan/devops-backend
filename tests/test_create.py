import pytest
import json
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from app import app as flask_app


@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client


def test_create_product(client):
    data = {
        'name': 'Test Product',
        'description': 'This is a test product',
        'price': 19.99,
        'quantity': 10
    }

    response = client.post('/products', json=data)

    assert response.status_code == 200

    expected_message = 'Product created successfully'
    new_id = 0
    with open('products.json', 'r') as f:
        products = json.load(f)
        new_id = len(products)
    expected_data = {
        'id': new_id,
        'name': 'Test Product',
        'description': 'This is a test product',
        'price': 19.99,
        'quantity': 10
    }
    assert response.json == {
        'message': expected_message, 'data': expected_data}

    response = client.delete(f'/products/{new_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Product deleted successfully'
