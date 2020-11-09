from flask import Flask
from forker.blueprints import (
    auth, heartbeat
)

def create_app(config_file: str=None) -> Flask:
    """Factory to create app instead of global instance.

    

    Args:
        config_file: Python file to load the config. If omitted,
            default config is used

    Returns:
        Flask application instance
    """
    app = Flask(__name__, static_folder='../../web/build', static_url_path='/')

    app.config.from_pyfile('../defaults.cfg')
    app.register_blueprint(auth.bp)
    app.register_blueprint(heartbeat.bp)

    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    return app
