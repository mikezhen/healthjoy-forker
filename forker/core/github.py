import requests
from flask import Flask, redirect, Response
from urllib.parse import urlencode

class GitHub:
    """Interacts with GitHub for authentication and actions

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
        """Redirects to GitHub auth page"""
        params = {'client_id': self.client_id}
        if scope:
            params['scope'] = scope
        
        url = f'{self.auth_url}/authorize?{urlencode(params)}'
        return redirect(url)
    
    def access_token(self, code: str) -> requests.Response:
        """Retrieves access token with temporary session code"""
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

    def create_fork(self, access_token: str) -> requests.Response:
        owner = self.app.config.get('GITHUB_FORK_OWNER')
        repo = self.app.config.get('GITHUB_FORK_NAME')
        headers = {
            'Authorization': self._format_authorization_header(access_token)
        }
        url = f'{self.api_url}/repos/{owner}/{repo}/forks'
        response = requests.post(url, headers=headers)
        ## Check for response status: https://docs.github.com/en/free-pro-team@latest/rest/reference/repos#forks
        return response

    def _format_authorization_header(self, access_token: str):
        """Format authorization header with access token"""
        return f'token {access_token}'

    def get_user(self, access_token: str) -> requests.Response:
        headers = {
            'Accept': 'application/json',
            'Authorization': self._format_authorization_header(access_token)
        }
        url = f'{self.api_url}/user'
        response = requests.get(url, headers=headers)
        print(url)
        print(response.status_code)
        return response