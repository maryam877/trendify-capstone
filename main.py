from etl.load import (
    load_orders,
    load_order_items,
    load_order_reviews
)

from etl.transform import (
    merge_orders_items,
    merge_orders_reviews,
    compute_delivery_metrics,
    categorize_review_scores
)

import pandas as pd


def main():
    # 1. Load raw data
    orders = load_orders('data/olist_orders_dataset.csv')
    items = load_order_items('data/olist_order_items_dataset.csv')
    reviews = load_order_reviews('data/olist_order_reviews_dataset.csv')

    # 2. Merge tables
    df = merge_orders_items(orders, items)
    df = merge_orders_reviews(df, reviews)

    # 3. Feature engineering
    df = compute_delivery_metrics(df)
    df = categorize_review_scores(df)

    # 4. Export clean file
    df.to_csv('outputs/final_orders_clean.csv', index=False)
    print("✅ Clean dataset exported to outputs/final_orders_clean.csv")


if __name__ == "__main__":
    main()
