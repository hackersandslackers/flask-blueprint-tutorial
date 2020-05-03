"""Compile static assets for app."""
from flask_assets import Environment, Bundle


def compile_static_assets(assets):
    """Create stylesheets."""
    common_less_bundle = Bundle('src/less/*.less',
                                filters='less,cssmin',
                                output='dist/css/style.css',
                                extra={'rel': 'stylesheet/less'})
    account_less_bundle = Bundle('account_bp/less/profile.less',
                                 filters='less,cssmin',
                                 output='account_bp/dist/css/profile.css',
                                 extra={'rel': 'stylesheet/less'})
    home_less_bundle = Bundle('home_bp/less/home.less',
                              filters='less,cssmin',
                              output='home_bp/dist/css/home.css',
                              extra={'rel': 'stylesheet/less'})
    assets.register('common_less_bundle', common_less_bundle)
    assets.register('account_less_bundle', account_less_bundle)
    assets.register('home_less_bundle', home_less_bundle)
    common_less_bundle.build()
    account_less_bundle.build()
    home_less_bundle.build()
