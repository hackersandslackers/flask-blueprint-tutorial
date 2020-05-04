"""General page routes."""
from flask import Blueprint, render_template
from flask import current_app as app
from application.products import list_products

# Blueprint Configuration
home_bp = Blueprint('home_bp', __name__,
                    template_folder='templates',
                    static_folder='static', url_prefix='')


@home_bp.route('/', methods=['GET'])
def home():
    """Homepage."""
    products = list_products(app)
    return render_template('index.jinja2',
                           title='Flask-Blueprint Tutorial | Home',
                           subtitle='My Fake Ecommerce Store',
                           template='home-template',
                           products=products,
                           headline="Flask Blueprint Tutorial")


@home_bp.route('/about', methods=['GET'])
def about():
    """About page."""
    return render_template('index.jinja2',
                           headline="About Page",
                           subtitle='This is an example about page.',
                           title='Flask-Blueprint Tutorial | About',
                           template='home-template page',
                           body="About")


@home_bp.route('/contact', methods=['GET'])
def contact():
    """Contact page."""
    return render_template('index.jinja2',
                           headline="Etc Page",
                           subtitle='This is an example contact page.',
                           title='Flask-Blueprint Tutorial | Etc',
                           template='home-template page',
                           body="Etc")
