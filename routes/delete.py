from flask import Blueprint, jsonify, request
import json

delete_bp = Blueprint('delete', __name__)


@delete_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    with open('products.json', 'r') as f:
        products = json.load(f)

    for product in products:
        if product['id'] == id:
            products.remove(product)
            with open('products.json', 'w') as f:
                json.dump(products, f, indent=4)
            return jsonify({'message': 'Product deleted successfully'})

    return jsonify({'message': 'Product not found'})
