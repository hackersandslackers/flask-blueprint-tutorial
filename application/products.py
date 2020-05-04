import requests


def list_products(app):
    """Grab six random products from BestBuy."""
    endpoint = "https://api.bestbuy.com/v1/products(customerReviewAverage>=4&customerReviewCount>100&longDescription=*)"
    params = {
        'show': "customerReviewAverage,customerReviewCount,name,sku,image,description,manufacturer,longDescription,salePrice,sku",
        "apiKey": app.config['BEST_BUY_API_KEY'],
        "format": "json",
        "pageSize": 6,
        "totalPages": 1,
        "sort": "customerReviewAverage.dsc"}
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    r = requests.get(endpoint, params=params, headers=headers)
    products = r.json()['products']
    return products
