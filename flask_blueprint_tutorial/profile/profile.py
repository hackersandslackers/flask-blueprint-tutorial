"""Routes for logged-in profile."""
from faker import Faker
from flask import Blueprint, render_template

fake = Faker()

# Blueprint Configuration
profile_blueprint = Blueprint("profile_blueprint", __name__, template_folder="templates", static_folder="static")


@profile_blueprint.route("/profile", methods=["GET"])
def user_profile():
    """Logged-in user profile page."""
    user = fake.simple_profile()
    job = fake.job()
    return render_template(
        "profile.jinja2",
        title="User Profile",
        template="profile-template",
        user=user,
        job=job,
    )
