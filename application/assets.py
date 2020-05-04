"""Compile static assets for app."""
from flask_assets import Environment, Bundle


def compile_static_assets(app):
    """Create stylesheets."""
    assets = Environment(app)
    Environment.auto_build = True
    Environment.debug = False
    common_less_bundle = Bundle('src/less/*.less',
                                filters='less,cssmin',
                                output='dist/css/style.css',
                                extra={'rel': 'stylesheet/less'})
    account_less_bundle = Bundle('account_bp/less/profile.less',
                                 filters='less,cssmin',
                                 output='dist/css/profile.css',
                                 extra={'rel': 'stylesheet/less'})
    home_less_bundle = Bundle('home_bp/less/home.less',
                              filters='less,cssmin',
                              output='dist/css/home.css',
                              extra={'rel': 'stylesheet/less'})
    product_less_bundle = Bundle('product_bp/less/product.less',
                                 filters='less,cssmin',
                                 output='dist/css/product.css',
                                 extra={'rel': 'stylesheet/less'})
    assets.register('common_less_bundle', common_less_bundle)
    assets.register('account_less_bundle', account_less_bundle)
    assets.register('home_less_bundle', home_less_bundle)
    assets.register('product_less_bundle', product_less_bundle)
    common_less_bundle.build()
    account_less_bundle.build()
    home_less_bundle.build()
    product_less_bundle.build()
