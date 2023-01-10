"""Application entry point."""
from flask_blueprint_tutorial import init_app

app = init_app()

if __name__ == "__wsgi__":
    app.run(host="127.0.0.1")
