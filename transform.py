import pandas as pd
from pathlib import Path

RAW = Path.home() / 'Desktop/real-time-sales-analytics-pipeline/data/raw/sales.csv'
OUT = Path.home() / 'Desktop/real-time-sales-analytics-pipeline/data/processed/sales_clean.csv'

df = pd.read_csv(RAW)

# Basic cleaning
df = df.drop_duplicates()
df['sale_date'] = pd.to_datetime(df['sale_date'])
df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0)

# Derived column
df['year_month'] = df['sale_date'].dt.strftime('%Y-%m')

OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT, index=False)

print('Cleaned rows:', len(df))
print('Saved to:', OUT)
