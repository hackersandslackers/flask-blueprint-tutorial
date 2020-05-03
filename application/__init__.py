"""Initialize Flask app."""
from flask import Flask
import flask_assets




def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = flask_assets.Environment()
    assets.init_app(app)

    with app.app_context():
        # Import parts of our application
        from .account import account
        from .home import home
        from .assets import compile_static_assets

        app.register_blueprint(account.account_bp)
        app.register_blueprint(home.home_bp)

        # Compile static assets
        if app.config['FLASK_ENV'] == 'development':
            compile_static_assets(assets)

        return app
