from flask import Blueprint
from flask import current_app, request, redirect, url_for
from forker.core.github import GitHub

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET'])
def login():
    return GitHub(current_app).authorize('public_repo,read:user')

@bp.route('/callback', methods=['GET'])
def callback():
    session_code = request.args.get('code')
    print(session_code)
    response = GitHub(current_app).access_token(session_code)
    print(response.json())
    return redirect('/')
