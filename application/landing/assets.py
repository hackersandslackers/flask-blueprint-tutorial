"""Compile static assets for app."""
from flask_assets import Environment, Bundle


def compile_landing_assets(app):
    """Configure landing asset bundles."""
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    # Stylesheets Bundle
    less_bundle = Bundle('src/less/landing.less',
                         filters='less,cssmin',
                         output='dist/css/landing.css',
                         extra={'rel': 'stylesheet/less'})
    # JavaScript Bundle
    js_bundle = Bundle('src/js/main.js',
                       filters='jsmin',
                       output='dist/js/main.min.js')
    # Register assets
    assets.register('less_all', less_bundle)
    assets.register('js_all', js_bundle)
    # Build assets in development mode
    if app.config['FLASK_ENV'] == 'development':
        less_bundle.build(force=True)
        js_bundle.build()


def compile_account_assets(app):
    """Configure logged-in asset bundles."""
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    # Stylesheets Bundle
    less_bundle = Bundle('src/less/account.less',
                         filters='less,cssmin',
                         output='dist/css/account.css',
                         extra={'rel': 'stylesheet/less'})
    # Register assets
    assets.register('less_all', less_bundle)
    # Build assets in development mode
    if app.config['FLASK_ENV'] == 'development':
        less_bundle.build(force=True)


def compile_assets(app):
    """Compile all asset bundles."""
    compile_landing_assets(app)
    compile_account_assets(app)
