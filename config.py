"""Class-based Flask app configuration."""
from os import environ, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))


class Config:
    """Configuration from environment variables."""

    # General Config\
    ENVIRONMENTS = environ.get("ENVIRONMENT")

    # Flask Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    FLASK_APP = "wsgi.py"

    # Flask-Assets
    LESS_BIN = environ.get("LESS_BIN")
    ASSETS_DEBUG = False
    LESS_RUN_IN_DEBUG = False

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = False

    # Hardcoded data
    PRODUCT_DATA_FILEPATH = f"{BASE_DIR}/data/products.json"
