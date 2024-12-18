


# app/routes/user_routes.py

from flask import jsonify
from . import bp  # Import the blueprint object defined in __init__.py.

@bp.route('/users')
def list_users():
    """Return a list of users."""
    return jsonify({'users': ['User1', 'User2', 'User3']})  # Example response.

@bp.route('/users/<int:user_id>')
def get_user(user_id):
    """Return details for a specific user."""
    return jsonify({'user': f'User {user_id}'})  # Example response for a specific user.
