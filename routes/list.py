from flask import Blueprint, jsonify
import json

list_bp = Blueprint('list', __name__)


@list_bp.route('/products')
def list_products():
    with open('products.json', 'r') as f:
        products = json.load(f)
    return jsonify(products)