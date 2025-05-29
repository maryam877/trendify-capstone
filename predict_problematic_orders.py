import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load functions
from etl.load import (
    load_orders,
    load_order_items,
    load_order_reviews,
    load_sellers
)

# Transformation functions
def merge_orders_items(orders_df, items_df):
    return pd.merge(orders_df, items_df, on='order_id', how='left')

def merge_orders_reviews(orders_df, reviews_df):
    return pd.merge(orders_df, reviews_df, on='order_id', how='left')

def compute_delivery_metrics(df):
    df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
    df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['delivery_delay'] = (df['order_delivered_customer_date'] - df['order_estimated_delivery_date']).dt.days
    df['wait_time'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days
    df['is_late'] = df['delivery_delay'].apply(lambda x: 1 if x > 0 else 0)
    return df

def categorize_review_scores(df):
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
    return pd.merge(orders_items_df, sellers_df, on='seller_id', how='left')

def run_transform_pipeline():
    orders = load_orders()
    items = load_order_items()
    reviews = load_order_reviews()
    sellers = load_sellers()

    df = merge_orders_items(orders, items)
    df = merge_orders_sellers(df, sellers)
    df = merge_orders_reviews(df, reviews)
    df = compute_delivery_metrics(df)
    df = categorize_review_scores(df)
    df['problematic'] = ((df['is_late'] == 1) | (df['review_score'] <= 2)).astype(int)
    df.to_csv('outputs/final_orders_clean.csv', index=False)
    print("✅ Clean dataset exported to outputs/final_orders_clean.csv")
    return df

def build_problematic_order_model(df):
    features = ['wait_time', 'price', 'freight_value']
    df = df.dropna(subset=features + ['problematic'])
    X = df[features]
    y = df['problematic']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print("\nConfusion Matrix:")
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.show()
    return model

if __name__ == '__main__':
    df = run_transform_pipeline()
    build_problematic_order_model(df)
