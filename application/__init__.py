"""Initialize app."""
from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our application
        from .account import account_routes
        from .landing import landing_routes
        from .landing.assets import compile_assets
        app.register_blueprint(account_routes.account_bp)
        app.register_blueprint(landing_routes.landing_bp)
        compile_assets(app)

        return app
