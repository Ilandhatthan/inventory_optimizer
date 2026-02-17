import sqlite3
import random
from datetime import datetime, timedelta
import os

# 1. Setup the database file path
os.makedirs('data', exist_ok=True)
db_path = os.path.join('data', 'inventory_system.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 2. SQL Schema: Create Tables
# This mimics a real retail database structure
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    category TEXT,
    price REAL,
    lead_time INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    product_id INTEGER,
    current_stock INTEGER,
    FOREIGN KEY(product_id) REFERENCES products(product_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    transaction_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    quantity INTEGER,
    date TEXT,
    FOREIGN KEY(product_id) REFERENCES products(product_id)
)
''')

# 3. Generate 100 Products
# We intentionally leave some prices as 'None' (NULL) for Phase 2 cleaning
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Tools']
for i in range(1, 101):
    price = round(random.uniform(10, 500), 2) if random.random() > 0.1 else None
    cursor.execute('INSERT INTO products VALUES (?,?,?,?)', 
                   (i, random.choice(categories), price, random.randint(1, 14)))

# 4. Generate 12,000 Sales Records (Last 90 days)
for i in range(12000):
    date = (datetime.now() - timedelta(days=random.randint(0, 90))).strftime('%Y-%m-%d')
    cursor.execute('INSERT INTO sales (product_id, quantity, date) VALUES (?,?,?)', 
                   (random.randint(1, 100), random.randint(1, 5), date))

# 5. Generate Inventory (Some negative for cleaning practice)
for i in range(1, 101):
    cursor.execute('INSERT INTO inventory VALUES (?,?)', 
                   (i, random.randint(-5, 100)))

conn.commit()
conn.close()
print("inventory_system.db created successfully.")