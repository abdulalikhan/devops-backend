import json
import pytest
from app import app as flask_app


@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client


def test_delete_product(client):
    data = {'name': 'Test Product', 'description': 'This is a test product',
            'price': 9.99, 'quantity': 10}
    response = client.post('/products', json=data)
    assert response.status_code == 200
    product_id = response.json['data']['id']

    response = client.delete(f'/products/{product_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Product deleted successfully'

    response = client.get('/products')
    assert response.status_code == 200
    with open('products.json', 'r') as f:
        expected_products = json.load(f)
    assert response.json == expected_products
    for product in expected_products:
        assert product['id'] != product_id
