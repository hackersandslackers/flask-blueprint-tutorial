"""Compile static assets for app."""
from flask_assets import Environment, Bundle


def compile_static_assets(app):
    """Create stylesheets."""
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    less_bundle = Bundle('src/less/*.less',
                         filters='less,cssmin',
                         output='dist/css/account.css',
                         extra={'rel': 'stylesheet/less'})
    assets.register('less_all', less_bundle)
    less_bundle.build(force=True)
