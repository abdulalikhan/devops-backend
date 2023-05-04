from flask import Blueprint, jsonify, request
import json

update_bp = Blueprint('update', __name__)


@update_bp.route('/products/<int:id>', methods=['PATCH'])
def update_product(id):
    data = request.get_json()

    with open('products.json', 'r') as f:
        products = json.load(f)

    for product in products:
        if product['id'] == id:
            if 'quantity' in data:
                product['quantity'] = data['quantity']

            with open('products.json', 'w') as f:
                json.dump(products, f, indent=4)

            return jsonify({'message': 'Product updated successfully', 'data': product})

    return jsonify({'message': 'Product not found'})
