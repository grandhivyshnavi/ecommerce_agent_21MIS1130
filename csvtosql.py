import sqlite3
import pandas as pd

# Connect to (or create) the database
conn = sqlite3.connect('sales.db')

# Load CSVs into DataFrames
ad_sales = pd.read_csv('Ad_Sales_Metrics.csv')
total_sales = pd.read_csv('Total_Sales_Metrics.csv')
eligibility = pd.read_csv('Eligibility_Table.csv')

# Write to SQL tables
ad_sales.to_sql('ad_sales', conn, if_exists='replace', index=False)
total_sales.to_sql('total_sales', conn, if_exists='replace', index=False)
eligibility.to_sql('eligibility', conn, if_exists='replace', index=False)

conn.close()
print("✅ All CSV files loaded into sales.db")
