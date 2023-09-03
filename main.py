"""Application entry point."""
from flask_blueprint_tutorial import flask_app


def init_app():
    """Initialize Flask application."""
    app = flask_app()
    app.run(host="127.0.0.1", port=6416, debug=True)


if __name__ == "__main__":
    init_app()
