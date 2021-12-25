import json


def retrieve_all_products():
    with open('products.json', 'r') as all_products:
        json.load(all_products)

def retrieve_requested_product():
    with open('products.json', 'r') as r_product:
        json.load(r_product.product_id)