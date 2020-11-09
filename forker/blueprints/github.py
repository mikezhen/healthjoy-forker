from flask import Blueprint
from flask import (
    current_app, session, jsonify
)
from forker.core.github import GitHub

bp = Blueprint('github', __name__, url_prefix='/github')

@bp.route('/fork', methods=['POST'])
def fork():
    if 'access_token' in session:
        github = GitHub(current_app)
        user = github.get_user(session['access_token'])
        if user.ok:
            fork = github.create_fork(session['access_token'])
            if fork.ok:
                return (fork.content, fork.status_code, fork.headers.items())
    session.pop('access_token', None)  # Force re-authentication if fail
    return (jsonify({}), 401)