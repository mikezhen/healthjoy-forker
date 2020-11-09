from flask import Blueprint
from flask import (
    current_app, session, request, redirect, url_for, jsonify
)
from forker.core.github import GitHub

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/', methods=['GET'])
def auth():
    if 'access_token' in session:
        print(session['access_token'])
        # Check to see if access was revoked
        resp = GitHub(current_app).get_user(session['access_token'])
        if resp.ok:
            return (jsonify({}), 200)
        session.pop('access_token', None)
    return (jsonify({}), 401)

@bp.route('/login', methods=['GET'])
def login():
    scope = current_app.config.get('GITHUB_SCOPES')
    return GitHub(current_app).authorize(scope)

@bp.route('/callback', methods=['GET'])
def callback():
    session_code = request.args.get('code')
    resp = GitHub(current_app).access_token(session_code)
    session['access_token'] = resp.json()['access_token']
    session['scope'] = resp.json()['scope']
    print(session['access_token'])
    return redirect('/')
