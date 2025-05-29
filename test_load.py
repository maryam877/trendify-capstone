from etl.load import load_orders
df = load_orders()
print(df.head())