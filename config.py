"""Class-based Flask app configuration."""
from os import environ, path, system

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))


class Config:
    """Configuration from environment variables."""

    # General Config\
    ENVIRONMENT = environ.get("ENVIRONMENT")

    # Flask Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    FLASK_APP = "wsgi.py"

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG = False

    # Flask-Assets
    LESS_BIN = system("which lessc")
    ASSETS_DEBUG = False
    LESS_RUN_IN_DEBUG = False
    if ENVIRONMENT == "development" and LESS_BIN is None:
        raise ValueError("Application running in `development` mode cannot create assets without `lessc` installed.")

    # Hardcoded data
    PRODUCT_DATA_FILEPATH = f"{BASE_DIR}/data/products.json"
