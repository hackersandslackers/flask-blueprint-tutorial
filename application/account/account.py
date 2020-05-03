"""Routes for logged-in account panel."""
from flask import Blueprint, render_template

# Blueprint Configuration
account_bp = Blueprint('account_bp', __name__,
                       template_folder='templates',
                       static_folder='./static')


@account_bp.route('/profile', methods=['GET'])
def user_profile():
    """Logged-in user profile page example."""
    user = {'name': 'Todd Birchard',
            'avatar': 'https://hackersandslackers-cdn.storage.googleapis.com/2020/04/todd@2x.jpg',
            'profession': 'Engineer',
            'location': 'NYC',
            'website': 'https://hackersandslackers.com/'}
    return render_template(
        'profile.jinja2',
        title='User Profile',
        template='dashboard-template account',
        user=user
    )
