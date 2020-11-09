from flask import Blueprint, jsonify

bp = Blueprint('heartbeat', __name__)

@bp.route('/heartbeat', methods=['GET'])
def heartbeat():
    return jsonify({'status': 'healthy'})