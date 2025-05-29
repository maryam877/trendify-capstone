import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl


def load_clean_data(path='outputs/final_orders_clean.csv'):
    """Load the cleaned dataset for analysis."""
    return pd.read_csv(path)


def plot_late_deliveries(df):
    sns.set_theme(style="whitegrid")
    counts = df['is_late'].value_counts(normalize=True).sort_index()
    labels = ['On Time', 'Late']
    values = [counts.get(0, 0), counts.get(1, 0)]
    colors = ['#1f77b4', '#aec7e8']  # blue, light blue

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(labels, values, color=colors, width=0.5, edgecolor='black')

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.015,
                f"{height:.1%}", ha='center', fontsize=12, fontweight='bold')

    ax.set_title('Share of Late Deliveries', fontsize=14, fontweight='bold')
    ax.set_ylabel('Proportion')
    ax.set_ylim(0, 1.05)
    ax.spines[['top', 'right']].set_visible(False)
    ax.yaxis.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()




def plot_reviews_distribution(df):
    """Enhanced: Distribution of review scores."""
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set(style="whitegrid")
    plt.figure(figsize=(7, 4))
    ax = sns.countplot(x='review_score', data=df, palette='Blues_d')

    for p in ax.patches:
        ax.annotate(f'{int(p.get_height()):,}',
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='bottom', fontsize=10)

    plt.title('Review Score Distribution', fontsize=14, weight='bold')
    plt.xlabel('Review Score')
    plt.ylabel('Number of Orders')
    plt.tight_layout()
    plt.show()


def plot_delay_vs_review(df):
    sns.set_theme(style="ticks")

    # Blue-based sentiment buckets
    blue_palette = {
        'good': '#0a9396',      # teal blue
        'neutral': '#5aa9e6',   # light sky blue
        'bad': '#005f73'        # deep navy
    }

    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    sns.boxplot(x='review_score_bucket', y='delivery_delay', data=df,
                palette=blue_palette, showfliers=False, linewidth=1)

    ax.set_title('Delivery Delay vs Review Sentiment', fontsize=14, fontweight='bold')
    ax.set_xlabel('Review Sentiment', fontsize=12)
    ax.set_ylabel('Delivery Delay (days)', fontsize=12)
    ax.axhline(0, linestyle='--', color='gray', lw=1)
    ax.spines[['top', 'right']].set_visible(False)
    plt.tight_layout()
    plt.show()



mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['axes.titlesize'] = 14
mpl.rcParams['axes.labelsize'] = 12
mpl.rcParams['xtick.labelsize'] = 11
mpl.rcParams['ytick.labelsize'] = 11


import matplotlib.pyplot as plt
import seaborn as sns

def plot_underperforming_sellers(df):
    # Drop rows without seller_id
    df = df.dropna(subset=['seller_id'])

    # Calculate performance metrics
    seller_stats = df.groupby('seller_id').agg(
        avg_delay=('delivery_delay', 'mean'),
        num_orders=('order_id', 'count'),
        bad_review_rate=('review_score', lambda x: (x <= 2).mean())
    ).reset_index()

    # Filter to sellers with at least 50 orders
    seller_stats = seller_stats[seller_stats['num_orders'] >= 50]

    # Sort by average delay and bad review rate
    top_delay = seller_stats.sort_values('avg_delay', ascending=False).head(10)
    top_bad_reviews = seller_stats.sort_values('bad_review_rate', ascending=False).head(10)

    # Plot: Top 10 by Avg Delay
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_delay, x='avg_delay', y='seller_id', palette='Blues_d')
    plt.title('Top 10 Sellers by Average Delivery Delay')
    plt.xlabel('Average Delay (days)')
    plt.ylabel('Seller ID')
    plt.tight_layout()
    plt.show()

    # Plot: Top 10 by Bad Review Rate
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_bad_reviews, x='bad_review_rate', y='seller_id', palette='Blues_d')
    plt.title('Top 10 Sellers by Bad Review Rate (1-2 stars)')
    plt.xlabel('Proportion of Bad Reviews')
    plt.ylabel('Seller ID')
    plt.tight_layout()
    plt.show()




def state_performance(df):
    state_stats = df.groupby('seller_state').agg(
        avg_delay=('delivery_delay', 'mean'),
        bad_reviews=('review_score', lambda x: (x <= 2).mean())
    ).reset_index()

    worst_states = state_stats.sort_values(by='avg_delay', ascending=False).head(10)

    plt.figure(figsize=(12, 6))
    sns.barplot(x='avg_delay', y='seller_state', data=worst_states, palette='Blues_d')
    plt.title('Top 10 States by Avg Delivery Delay')
    plt.xlabel('Average Delay (days)')
    plt.ylabel('State')
    plt.tight_layout()
    plt.show()



