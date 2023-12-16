"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment


def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        # Import parts of our application
        from .assets import compile_static_assets
        from .home import home
        from .product import product
        from .profile import profile

        # Register Blueprints
        app.register_blueprint(profile.profile_blueprint)
        app.register_blueprint(home.home_blueprint)
        app.register_blueprint(product.product_blueprint)

        # Compile static assets
        compile_static_assets(assets)

        return app
