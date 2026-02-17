import sqlite3
import pandas as pd
import os

# 1. Connect to your D: drive database
db_path = os.path.join('data', 'inventory_system.db')
conn = sqlite3.connect(db_path)

# 2. SQL Join: Merging 12,000+ rows of data
# We join products with sales (summed) and current inventory levels
query = '''
SELECT 
    p.product_id, p.category, p.price, p.lead_time,
    i.current_stock,
    SUM(s.quantity) as total_units_sold
FROM products p
JOIN inventory i ON p.product_id = i.product_id
JOIN sales s ON p.product_id = s.product_id
GROUP BY p.product_id
'''
df = pd.read_sql_query(query, conn)
conn.close()

# 3. Data Cleaning (Just like your aircraft project)
# Fill missing prices with the median of their category
df['price'] = df['price'].fillna(df.groupby('category')['price'].transform('median'))
# Fix negative stock (set anything below 0 to 0)
df['current_stock'] = df['current_stock'].clip(lower=0)

# 4. Feature Engineering
# Calculate 'Sales Velocity' (Average units sold per day over 90 days)
df['sales_velocity'] = df['total_units_sold'] / 90

# Create our ML Target: 'stockout_risk'
# Logic: If (Stock / Velocity) < 7 days, it's a high risk (1), else (0)
df['stockout_risk'] = ((df['current_stock'] / df['sales_velocity']) < 7).astype(int)

# 5. Save the Cleaned Dataset for Phase 3
df.to_csv('data/cleaned_inventory.csv', index=False)
print("Cleaned data saved successfully.")