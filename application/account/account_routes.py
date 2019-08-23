"""Routes for logged-in account pages."""
from flask import Blueprint, render_template
from flask import current_app as app
from .assets import compile_account_assets

# Blueprint Configuration
account_bp = Blueprint('account_bp', __name__,
                       template_folder='templates',
                       static_folder='static',
                       url_prefix='/account')
compile_account_assets(app)


@account_bp.route('/account/dashboard', methods=['GET'])
def dashboard():
    """Account dashboard route."""
    return render_template('dashboard.html',
                           title='Flask-Blueprint Tutorial | Account Dashboard',
                           template='dashboard-template account',
                           body="This page is in your account blueprint")
