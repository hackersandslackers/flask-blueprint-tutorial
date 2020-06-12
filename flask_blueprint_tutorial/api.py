"""Source app with worthless data."""
import requests


def fetch_products(app):
    """Grab product listings from BestBuy."""
    endpoint = "https://api.bestbuy.com/v1/products(customerReviewAverage>=4&customerReviewCount>100&longDescription=*)"
    params = {
        'show': "customerReviewAverage,customerReviewCount,name,sku,image,description,manufacturer,longDescription,salePrice,sku",
        "apiKey": app.config['BEST_BUY_API_KEY'],
        "format": "json",
        "pageSize": 6,
        "totalPages": 1,
        "sort": "customerReviewAverage.dsc"}
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    req = requests.get(endpoint, params=params, headers=headers)
    products = req.json()['products']
    return products
