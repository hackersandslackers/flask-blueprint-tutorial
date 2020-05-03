"""Initialize Flask app."""
from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our application
        from .account import account
        from .landing import landing
        from .api import api
        from .assets import compile_static_assets

        app.register_blueprint(account.account_bp)
        app.register_blueprint(landing.landing_bp)
        app.register_blueprint(api.api_bp)
        from .assets import compile_static_assets

        # Compile static assets
        if app.config['FLASK_ENV'] == 'development':
            compile_static_assets(app)

        return app
