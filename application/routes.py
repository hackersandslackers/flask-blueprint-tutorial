"""Routes for logged-in application."""
from flask import Blueprint, render_template
from flask_login import current_user
from flask import current_app as app
from .assets import compile_auth_assets
from flask_login import login_required


# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')
compile_auth_assets(app)


@main_bp.route('/', methods=['GET'])
@login_required
def dashboard():
    """Serve logged in Dashboard."""
    return render_template('dashboard.html',
                           title='Flask-Login Tutorial.',
                           template='dashboard-template',
                           current_user=current_user,
                           body="You are now logged in!")
