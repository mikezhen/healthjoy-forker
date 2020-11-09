from flask import Blueprint
from flask import current_app
from forker.core.github import GitHub

bp = Blueprint('github', __name__, url_prefix='/github')

@bp.route('/fork', methods=['POST'])
def fork():
    return GitHub(current_app).create_fork()