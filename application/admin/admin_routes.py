"""Routes for logged-in account pages."""
from flask import Blueprint, render_template
from flask import current_app as app
from .assets import compile_admin_assets

# Blueprint Configuration
admin_bp = Blueprint('admin_bp', __name__,
                     template_folder='templates',
                     static_folder='static',
                     url_prefix='/admin')
compile_admin_assets(app)


@admin_bp.route('/dashboard', methods=['GET'])
def dashboard():
    """Admin dashboard route."""
    return render_template('dashboard.html',
                           title='Flask-Blueprint Tutorial | Admin Dashboard',
                           template='dashboard-template account',
                           body="Account")
