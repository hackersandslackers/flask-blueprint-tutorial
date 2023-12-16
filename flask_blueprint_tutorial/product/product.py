"""Product pages."""
from flask import Blueprint
from flask import current_app as app
from flask import render_template

from flask_blueprint_tutorial.api import fetch_products

# Blueprint Configuration
product_blueprint = Blueprint("product_blueprint", __name__, template_folder="templates", static_folder="static")


@product_blueprint.route("/products/<int:product_id>/", methods=["GET"])
def product_page(product_id: int) -> str:
    """
    Product detail page for a given product ID.

    :params int product_id: Unique product ID.

    :returns: str
    """
    product = fetch_products(app)[product_id]
    return render_template(
        "product.jinja2",
        title=product["name"],
        product=product,
        template="product-template",
    )
