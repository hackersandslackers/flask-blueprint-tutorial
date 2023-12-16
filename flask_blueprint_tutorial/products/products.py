"""Product pages."""
from flask import Blueprint
from flask import current_app as app
from flask import render_template

from flask_blueprint_tutorial.api import fetch_products

# Blueprint Configuration
product_bp = Blueprint("products_blueprint", __name__, template_folder="templates", static_folder="static")


@product_bp.route("/products/<int:product_id>/", methods=["GET"])
def product_page(product_id: int) -> str:
    """
    Product detail page for a given product ID.

    :params int product_id: Unique product ID.

    :returns: str
    """
    product = fetch_products(app)[product_id]
    return render_template(
        "products.jinja2",
        title=product["name"],
        product=product,
        template="profile-template",
    )
