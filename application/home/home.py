"""Routes for home pages."""
from flask import Blueprint, render_template


# Blueprint Configuration
home_bp = Blueprint('home_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@home_bp.route('/', methods=['GET'])
def home():
    """Homepage route."""
    return render_template('index.jinja2',
                           title='Flask-Blueprint Tutorial | Home',
                           template='home-template home',
                           body="Home")


@home_bp.route('/about', methods=['GET'])
def about():
    """About page route."""
    return render_template('index.jinja2',
                           title='Flask-Blueprint Tutorial | About',
                           template='about-template home',
                           body="About")


@home_bp.route('/etc', methods=['GET'])
def etc():
    """Etc page route."""
    return render_template('index.jinja2',
                           title='Flask-Blueprint Tutorial | Etc',
                           template='etc-template home',
                           body="Etc")
