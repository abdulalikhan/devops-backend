import json
import pytest
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from app import app as flask_app


@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client


def test_update_product(client):
    new_product_data = {'name': 'New Product',
                        'description': 'A new product', 'price': 9.99, 'quantity': 10}
    response = client.post('/products', json=new_product_data)
    assert response.status_code == 200

    new_product_id = response.json['data']['id']

    update_data = {'quantity': 5}
    response = client.patch(f'/products/{new_product_id}', json=update_data)
    assert response.status_code == 200
    assert response.json['message'] == 'Product updated successfully'

    response = client.get(f'/products')
    assert response.status_code == 200

    updated_product_data = response.json[-1]
    assert updated_product_data['quantity'] == 5

    response = client.delete(f'/products/{new_product_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Product deleted successfully'
