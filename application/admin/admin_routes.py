"""Routes for logged-in account pages."""
from flask import Blueprint, render_template
from flask import current_app as app

# Blueprint Configuration
admin_bp = Blueprint('admin_bp', __name__,
                     template_folder='templates',
                     static_folder='static',
                     url_prefix='/admin')


@admin_bp.route('/dashboard', methods=['GET'])
def dashboard():
    """Admin dashboard route."""
    return render_template('dashboard.jinja2',
                           title='Flask-Blueprint Tutorial | Admin Dashboard',
                           template='dashboard-template account',
                           body="Account")
