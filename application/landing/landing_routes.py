"""Routes for landing pages."""
from flask import Blueprint, render_template
from flask import current_app as app
from .assets import compile_account_assets

# Blueprint Configuration
landing_bp = Blueprint('landing_bp', __name__,
                       template_folder='templates',
                       static_folder='static')
compile_account_assets(app)


@landing_bp.route('/', methods=['GET'])
def home():
    """Homepage route."""
    return render_template('index.html',
                           title='Flask-Blueprint Tutorial | Home',
                           template='home-template landing',
                           body="This page is in your main blueprint")


@landing_bp.route('/about', methods=['GET'])
def about():
    """About page route."""
    return render_template('about.html',
                           title='Flask-Blueprint Tutorial | About',
                           template='about-template landing',
                           body="This page is in your about blueprint")


@landing_bp.route('/etc', methods=['GET'])
def etc():
    """Etc page route."""
    return render_template('etc.html',
                           title='Flask-Blueprint Tutorial | Etc',
                           template='etc-template landing',
                           body="This page is in your etc blueprint")