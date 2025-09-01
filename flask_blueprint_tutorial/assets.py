"""Compile static assets."""

from flask import current_app as app
from webassets.bundle import Bundle


def compile_static_assets(assets: Bundle) -> Bundle:
    """
    Create CSS stylesheet bundles from .less files.

    :param Bundle assets: Static asset bundle.

    :returns: Bundle
    """
    assets.auto_build = True
    assets.debug = False
    common_style_bundle = Bundle(
        "src/less/*.less",
        filters="less,cssmin",
        output="dist/css/style.css",
        extra={"rel": "stylesheet/less"},
    )
    home_style_bundle = Bundle(
        "home_blueprint/less/home.less",
        filters="less,cssmin",
        output="dist/css/home.css",
        extra={"rel": "stylesheet/less"},
    )
    profile_style_bundle = Bundle(
        "profile_blueprint/less/profile.less",
        filters="less,cssmin",
        output="dist/css/profile.css",
        extra={"rel": "stylesheet/less"},
    )
    product_style_bundle = Bundle(
        "product_blueprint/less/product.less",
        filters="less,cssmin",
        output="dist/css/product.css",
        extra={"rel": "stylesheet/less"},
    )
    assets.register("common_style_bundle", common_style_bundle)
    assets.register("home_style_bundle", home_style_bundle)
    assets.register("profile_style_bundle", profile_style_bundle)
    assets.register("product_style_bundle", product_style_bundle)
    if app.config["ENVIRONMENT"] == "development":
        common_style_bundle.build()
        home_style_bundle.build()
        profile_style_bundle.build()
        product_style_bundle.build()
    return assets
