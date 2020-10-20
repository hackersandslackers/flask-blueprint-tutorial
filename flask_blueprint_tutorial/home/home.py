"""General page routes."""
from flask import Blueprint
from flask import current_app as app
from flask import render_template

from flask_blueprint_tutorial.api import fetch_products

# Blueprint Configuration
home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)


@home_bp.route("/", methods=["GET"])
def home():
    """Homepage."""
    products = fetch_products(app)
    return render_template(
        "index.jinja2",
        title="Flask Blueprint Demo",
        subtitle="Demonstration of Flask blueprints in action.",
        template="home-template",
        products=products,
    )


@home_bp.route("/about", methods=["GET"])
def about():
    """About page."""
    return render_template(
        "index.jinja2",
        title="About",
        subtitle="This is an example about page.",
        template="home-template page",
    )


@home_bp.route("/contact", methods=["GET"])
def contact():
    """Contact page."""
    return render_template(
        "index.jinja2",
        title="Contact",
        subtitle="This is an example contact page.",
        template="home-template page",
    )
