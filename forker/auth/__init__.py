from flask import Blueprint
from .github import GitHub
from flask import current_app, request, redirect, url_for

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET'])
def login():
    return GitHub(current_app).authorize('public_repo')

@bp.route('/callback', methods=['GET'])
def callback():
    session_code = request.args.get('code')
    print(session_code)
    response = GitHub(current_app).access_token(session_code)
    print(response.json())
    return redirect('/')
