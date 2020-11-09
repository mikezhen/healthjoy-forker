from os import environ

GITHUB_AUTH_URL = 'https://github.com/login/oauth'
GITHUB_API_URL = 'https://api.github.com'
GITHUB_FORK_OWNER = 'mikezhen'
GITHUB_FORK_NAME = 'healthjoy-forker'
GITHUB_SCOPES = 'public_repo'

SECRET_KEY = environ.get('SECRET_KEY')
GITHUB_CLIENT_ID = environ.get('GITHUB_CLIENT_ID')
GITHUB_CLIENT_SECRET = environ.get('GITHUB_CLIENT_SECRET')
