from flask import Blueprint, jsonify, request
import json

create_bp = Blueprint('create', __name__)


@create_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()

    with open('products.json', 'r') as f:
        products = json.load(f)

    product = {
        'id': len(products) + 1,
        'name': data['name'],
        'description': data['description'],
        'price': data['price'],
        'quantity': data['quantity']
    }

    products.append(product)

    with open('products.json', 'w') as f:
        json.dump(products, f, indent=4)

    return jsonify({'message': 'Product created successfully', 'data': product})
