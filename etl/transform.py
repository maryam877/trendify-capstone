import pandas as pd

def merge_orders_items(orders_df, items_df):
    """Join orders with order items"""
    return pd.merge(orders_df, items_df, on='order_id', how='left')

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
