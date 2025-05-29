import pandas as pd

def merge_orders_items(orders_df, items_df):
    """Join orders with order items and include seller_id"""
    return pd.merge(orders_df, items_df[['order_id', 'product_id', 'seller_id', 'price']], on='order_id', how='left')


def merge_orders_reviews(orders_df, reviews_df):
    """Join orders with reviews"""
    return pd.merge(orders_df, reviews_df, on='order_id', how='left')

def compute_delivery_metrics(df):
    """Create delivery delay and wait time columns, late delivery flag"""
    df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
    df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

    df['delivery_delay'] = (df['order_delivered_customer_date'] - df['order_estimated_delivery_date']).dt.days
    df['wait_time'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days
    df['is_late'] = df['delivery_delay'].apply(lambda x: 1 if x > 0 else 0)

    return df

def categorize_review_scores(df):
    """Add review_score_bucket column: good, neutral, bad"""
    def label(score):
        if score <= 2:
            return 'bad'
        elif score == 3:
            return 'neutral'
        else:
            return 'good'
    df['review_score_bucket'] = df['review_score'].apply(label)
    return df



def merge_orders_sellers(orders_items_df, sellers_df):
    """Join orders+items with sellers"""
    orders_items_sellers = pd.merge(
        orders_items_df,
        sellers_df,
        on='seller_id',
        how='left',
        suffixes=('', '_seller')  # avoid seller_id_x/y
    )
    return orders_items_sellers




def run_transform_pipeline(orders_df, reviews_df, items_df, sellers_df):
    """Run the full transformation pipeline on the data"""

    # Step 1: Merge orders with items and sellers first
    df = merge_orders_items(orders_df, items_df)
    df = merge_orders_sellers(df, sellers_df)
    print("🧪 Columns after merging sellers:", df.columns.tolist())
    print("🧪 Sample rows with seller_id:")
    print(df[['order_id', 'seller_id']].dropna().head())

    # Step 2: Merge with reviews
    df = merge_orders_reviews(df, reviews_df)

    # Step 3: Feature engineering
    df = compute_delivery_metrics(df)
    df = categorize_review_scores(df)

    return df

