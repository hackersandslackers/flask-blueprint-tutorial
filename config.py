"""Class-based Flask app configuration."""

import subprocess
from os import environ, path

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
    if ENVIRONMENT == "development":
        # Check if `lessc` is installed
        LESS_BIN = subprocess.call("which lessc", shell=True)
        if LESS_BIN is None:
            raise ValueError("Flask requires `lessc` to be installed to compile styles.")
        else:
            # Check if `nodejs` is installed
            NODE_JS = subprocess.call("which node", shell=True)
            if NODE_JS is None:
                raise ValueError(
                    "Application running in `development` mode cannot create assets without `node` installed."
                )

    # Hardcoded data
    PRODUCT_DATA_FILEPATH = f"{BASE_DIR}/data/products.json"
