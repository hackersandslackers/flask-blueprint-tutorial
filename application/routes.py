"""Routes for logged-in application."""
from flask import Blueprint, render_template, session
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
    # session['redis_test'] = 'This is a session variable.'
    return render_template('dashboard.html',
                           title='Flask-Session Tutorial.',
                           template='dashboard-template',
                           current_user=current_user,
                           body="You are now logged in!")


@main_bp.route('/session', methods=['GET'])
@login_required
def session_view():
    """Route which displays session variable value."""
    return render_template('session.html',
                           title='Flask-Session Tutorial.',
                           template='dashboard-template',
                           session_variable=str(session['redis_test']))
