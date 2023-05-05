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


def test_list_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    with open('./products.json', 'r') as f:
        expected_products = json.load(f)
    assert response.json == expected_products
