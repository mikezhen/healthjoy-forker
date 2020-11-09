from forker.core.app import create_app
import os

config_file = os.path.abspath('forker/config.py')
app = create_app(config_file)