"""Compile static assets for app."""
from flask_assets import Environment, Bundle


def compile_static_assets(app):
    """Create stylesheets."""
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    common_less_bundle = Bundle('src/less/*.less',
                                filters='less,cssmin',
                                output='dist/css/account.css',
                                extra={'rel': 'stylesheet/less'})
    account_less_bundle = Bundle('account_bp/less/profile.less',
                                 filters='less,cssmin',
                                 output='dist/css/profile.css',
                                 extra={'rel': 'stylesheet/less'})
    landing_less_bundle = Bundle('landing_bp/less/landing.less',
                                 filters='less,cssmin',
                                 output='dist/css/landing.css',
                                 extra={'rel': 'stylesheet/less'})
    assets.register('common_less_bundle', common_less_bundle)
    assets.register('account_less_bundle', account_less_bundle)
    assets.register('landing_less_bundle', landing_less_bundle)
    common_less_bundle.build()
    account_less_bundle.build()
    landing_less_bundle.build()
