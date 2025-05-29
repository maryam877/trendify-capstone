from etl.load import (
    load_orders,
    load_order_items,
    load_order_reviews,
    load_sellers
)

from etl.transform import run_transform_pipeline

from etl.analyze import (
    plot_late_deliveries,
    plot_reviews_distribution,
    plot_delay_vs_review,
    plot_underperforming_sellers
)

def main():
    orders = load_orders()
    items = load_order_items()
    reviews = load_order_reviews()
    sellers = load_sellers()

    df = run_transform_pipeline(orders, reviews, items, sellers)

    plot_late_deliveries(df)
    plot_reviews_distribution(df)
    plot_delay_vs_review(df)
    plot_underperforming_sellers(df)

if __name__ == '__main__':
    main()

