"""Routes for API."""
from flask import Blueprint, jsonify, make_response


# Blueprint Configuration
api_bp = Blueprint('api_bp', __name__, url_prefix='/api')


@api_bp.route('/user', methods=['GET'])
def user():
    """API user endpoint."""
    return make_response(jsonify({'hello': 'yes'}))
