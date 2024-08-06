import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('soil_data.db')

# List tables
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Tables in the database:")
print(tables)

# Inspect data from each table
for table_name in tables['name']:
    print(f"\nData from {table_name} table:")
    data = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 10;", conn)
    print(data)

# Close the connection
conn.close()
