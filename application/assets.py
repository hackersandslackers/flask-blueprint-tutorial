"""Compile static assets for app."""
from flask_assets import Environment, Bundle


def compile_asset_bundles(app):
    """Configure landing asset bundles."""
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    # Stylesheets Bundle
    landing_less_bundle = Bundle('src/less/landing.less',
                                 filters='less,cssmin',
                                 output='dist/css/landing.css',
                                 extra={'rel': 'stylesheet/less'})
    admin_less_bundle = Bundle('src/less/account.less',
                               filters='less,cssmin',
                               output='dist/css/account.css',
                               extra={'rel': 'stylesheet/less'})
    # Register assets
    assets.register('landing_less_bundle', landing_less_bundle)
    assets.register('admin_less_bundle', admin_less_bundle)
    # Build asset bundles
    landing_less_bundle.build()
    admin_less_bundle.build()
