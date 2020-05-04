"""Routes for logged-in account profile."""
from flask import Blueprint, render_template
from faker import Faker
fake = Faker()

# Blueprint Configuration
account_bp = Blueprint('account_bp', __name__,
                       template_folder='templates',
                       static_folder='./static')


@account_bp.route('/profile', methods=['GET'])
def user_profile():
    """Logged-in user profile page."""
    user = fake.simple_profile()
    job = fake.job()
    return render_template(
        'profile.jinja2',
        title='User Profile',
        template='profile-template',
        user=user,
        job=job
    )
