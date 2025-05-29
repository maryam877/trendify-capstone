from etl.analyze import (
    load_clean_data,
    plot_late_deliveries,
    plot_reviews_distribution,
    plot_delay_vs_review
)

def main():
    df = load_clean_data()
    plot_late_deliveries(df)
    plot_reviews_distribution(df)
    plot_delay_vs_review(df)

if __name__ == '__main__':
    main()
