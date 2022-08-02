"""Config settings for for development, testing and production environments."""
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

HERE = Path(__file__).parent

class Config:
    """Base configuration."""
    CACHE_TYPE = os.getenv("CACHE_TYPE")
    CACHE_DEFAULT_TIMEOUT = os.getenv("CACHE_DEFAULT_TIMEOUT")
    
class TestingConfig(Config):
    """Testing configuration."""
    
    TESTING = True


class DevelopmentConfig(Config):
    """Development configuration."""



class ProductionConfig(Config):
    """Production configuration."""



ENV_CONFIG_DICT = dict(
    development=DevelopmentConfig, testing=TestingConfig, production=ProductionConfig
)


def get_config(config_name):
    """Retrieve environment configuration settings."""
    return ENV_CONFIG_DICT.get(config_name, ProductionConfig)