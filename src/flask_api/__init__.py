"""Flask app initialization via factory pattern."""
from flask import Flask
from flask_caching import Cache
from src.flask_api.config import get_config

cache  = Cache()

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(get_config(config_name))

    from src.flask_api.api import api_bp

    app.register_blueprint(api_bp)
    
    cache.init_app(app)
    
    return app