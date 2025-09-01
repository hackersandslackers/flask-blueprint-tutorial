"""General page routes."""

from flask import Blueprint
from flask import current_app as app
from flask import render_template

from flask_blueprint_tutorial.api import fetch_products

# Blueprint Configuration
home_blueprint = Blueprint("home_blueprint", __name__, template_folder="templates", static_folder="static")


@home_blueprint.route("/", methods=["GET"])
def home() -> str:
    """
    Serve `Home` page template.

    :returns: str
    """
    products = fetch_products(app)
    return render_template(
        "index.jinja2",
        title="Flask Blueprint Demo",
        subtitle="Demonstration of Flask blueprints in action.",
        template="home-template",
        products=products,
    )


@home_blueprint.route("/about", methods=["GET"])
def about() -> str:
    """
    Serve `About` page template.

    :returns: str
    """
    return render_template(
        "index.jinja2",
        title="About",
        subtitle="This is an example about page.",
        template="home-template page",
    )


@home_blueprint.route("/contact", methods=["GET"])
def contact() -> str:
    """
    Serve `Contact` page template.

    :returns: str
    """
    return render_template(
        "index.jinja2",
        title="Contact",
        subtitle="This is an example contact page.",
        template="home-template page",
    )
