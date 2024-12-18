


# app/routes/product_routes.py

from flask import jsonify
from . import bp  # Import the blueprint object defined in __init__.py.

@bp.route('/products')
def list_products():
    """Return a list of products."""
    return jsonify({'products': ['Product1', 'Product2', 'Product3']})  # Example response.
