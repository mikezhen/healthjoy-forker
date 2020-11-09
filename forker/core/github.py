import requests
from flask import Flask, redirect, Response
from urllib.parse import urlencode

class GitHub:
    """Interacts with GitHub for authentication and actions

    Attributes:

    """

    DEFAULT_API_URL = 'https://api.github.com'
    DEFAULT_AUTH_URL = 'https://github.com/login/oauth'

    def __init__(self, app: Flask=None):
        if app:
            self.app = app
            self.api_url = app.config.get('GITHUB_API_URL', self.DEFAULT_API_URL)
            self.auth_url = app.config.get('GITHUB_AUTH_URL', self.DEFAULT_AUTH_URL)
            self.client_id = app.config['GITHUB_CLIENT_ID']
            self.client_secret = app.config['GITHUB_CLIENT_SECRET']
        else:
            self.app = None

    def authorize(self, scope: str=None) -> Response:
        params = {'client_id': self.client_id}
        if scope:
            params['scope'] = scope
        
        url = f'{self.auth_url}/authorize?{urlencode(params)}'
        return redirect(url)
    
    def access_token(self, code: str) -> requests.Response:
        headers = {
            'Accept': 'application/json'
        }
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code
        }
        url = f'{self.auth_url}/access_token?{urlencode(params)}'
        response = requests.post(url, headers=headers)
        return response

    def create_fork(self) -> requests.Response:
        owner = self.app.config.get('GITHUB_REPO_OWNER')
        repo = self.app.config.get('GITHUB_REPO_NAME')
        headers = {
            'Authorization': self._get_authorization_header(self.access_token)
        }
        url = f'{self.api_url}/repos/{owner}/{repo}/forks'
        response = requests.post(url, headers=headers)
        ## Check for response status: https://docs.github.com/en/free-pro-team@latest/rest/reference/repos#forks
        return response

    def _get_authorization_header(self, access_token: str):
        return f'token {access_token}'