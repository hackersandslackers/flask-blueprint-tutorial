"""Initialize Flask app."""
from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our application
        from .admin import admin_routes
        from .main import main_routes
        app.register_blueprint(admin_routes.admin_bp)
        app.register_blueprint(main_routes.main_bp)
        from .assets import compile_asset_bundles

        # Compile static assets
        if app.config['FLASK_ENV'] == 'development':
            compile_asset_bundles(app)

        return app
