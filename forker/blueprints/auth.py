from flask import Blueprint
from flask import (
    current_app, session, request, redirect, url_for, jsonify
)
from forker.core.github import GitHub

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/', methods=['GET'])
def auth():
    if 'access_token' in session:
        return (jsonify({}), 200)
    return (jsonify({}), 401)

@bp.route('/login', methods=['GET'])
def login():
    scope = current_app.config.get('GITHUB_SCOPES')
    return GitHub(current_app).authorize(scope)

@bp.route('/callback', methods=['GET'])
def callback():
    session_code = request.args.get('code')
    response = GitHub(current_app).access_token(session_code)
    session['access_token'] = response.json()['access_token']
    session['scope'] = response.json()['scope']
    return redirect('/')
