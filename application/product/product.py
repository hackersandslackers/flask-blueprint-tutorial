"""Product pages."""
from flask import Blueprint, render_template
from flask import current_app as app
from application.products import list_products

# Blueprint Configuration
product_bp = Blueprint('product_bp', __name__,
                       template_folder='templates',
                       static_folder='static')


@product_bp.route('/product/<int:product_id>/', methods=['GET'])
def product_page(product_id):
    """Product description page."""
    product = list_products(app)[product_id]
    return render_template(
        'product.jinja2',
        product=product,
        template='profile-template'
    )
