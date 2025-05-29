import pandas as pd

def load_orders(path='data/olist_orders_dataset.csv'):
    """Load the orders dataset"""
    return pd.read_csv(path)

def load_order_items(path='data/olist_order_items_dataset.csv'):
    """Load the order items dataset"""
    return pd.read_csv(path)

def load_order_reviews(path='data/olist_order_reviews_dataset.csv'):
    """Load the order reviews dataset"""
    return pd.read_csv(path)

def load_customers(path='data/olist_customers_dataset.csv'):
    """Load the customers dataset"""
    return pd.read_csv(path)

def load_sellers(path='data/olist_sellers_dataset.csv'):
    """Load the sellers dataset"""
    return pd.read_csv(path)

def load_products(path='data/olist_products_dataset.csv'):
    """Load the products dataset"""
    return pd.read_csv(path)

def load_category_translation(path='data/product_category_name_translation.csv'):
    """Load category name translation"""
    return pd.read_csv(path)

def load_geolocation(path='data/olist_geolocation_dataset.csv'):
    """Load geolocation dataset"""
    return pd.read_csv(path)

def load_order_payments(path='data/olist_order_payments_dataset.csv'):
    """Load payment info"""
    return pd.read_csv(path)
