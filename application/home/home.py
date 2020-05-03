"""Routes for landing pages."""
from flask import Blueprint, render_template


# Blueprint Configuration
landing_bp = Blueprint('landing_bp', __name__,
                                template_folder='templates',
                                static_folder='static')


@landing_bp.route('/', methods=['GET'])
def home():
    """Homepage route."""
    return render_template('index.jinja2',
                           title='Flask-Blueprint Tutorial | Home',
                           template='home-template landing',
                           body="Home")


@landing_bp.route('/about', methods=['GET'])
def about():
    """About page route."""
    return render_template('index.jinja2',
                           title='Flask-Blueprint Tutorial | About',
                           template='about-template landing',
                           body="About")


@landing_bp.route('/etc', methods=['GET'])
def etc():
    """Etc page route."""
    return render_template('index.jinja2',
                           title='Flask-Blueprint Tutorial | Etc',
                           template='etc-template landing',
                           body="Etc")
