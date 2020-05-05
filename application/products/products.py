"""Product pages."""
from flask import Blueprint, render_template
from flask import current_app as app
from application.api import fetch_products

# Blueprint Configuration
product_bp = Blueprint('products_bp', __name__,
                       template_folder='templates',
                       static_folder='static')


@product_bp.route('/products/<int:product_id>/', methods=['GET'])
def product_page(product_id):
    """Product description page."""
    product = fetch_products(app)[product_id]
    return render_template(
        'products.jinja2',
        product=product,
        template='profile-template'
    )
