from etl.load import (
    load_orders,
    load_order_items,
    load_order_reviews,
    load_sellers
)

from etl.transform import run_transform_pipeline
import pandas as pd

def main():
    orders = load_orders('data/olist_orders_dataset.csv')
    items = load_order_items('data/olist_order_items_dataset.csv')
    reviews = load_order_reviews('data/olist_order_reviews_dataset.csv')
    sellers = load_sellers('data/olist_sellers_dataset.csv')

    df = run_transform_pipeline(orders, reviews, items, sellers)

    df.to_csv('outputs/final_orders_clean.csv', index=False)
    print("✅ Clean dataset exported!")

if __name__ == "__main__":
    main()


