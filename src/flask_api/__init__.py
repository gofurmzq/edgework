"""Flask app initialization via factory pattern."""
from flask import Flask
from flask_caching import Cache
from flask_api.config import get_config

cache  = Cache()

def create_app(config_name):
    app = Flask("edgeworks", template_folder='tamplate')
    app.config.from_object(get_config(config_name))

    from flask_api.api import api_bp

    app.register_blueprint(api_bp)
    
    cache.init_app(app)
    
    return app