import sqlite3
from tabulate import tabulate

# Connect to the database
conn = sqlite3.connect('soil_data.db')
cursor = conn.cursor()

# Check if tables exist
tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
print("Tables:")
print(tabulate(tables, headers=["Table Name"], tablefmt="pretty"))

# Verify the table structure
for table in ['Countries', 'Profiles', 'Layers']:
    schema = cursor.execute(f"PRAGMA table_info({table});").fetchall()
    print(f"\nSchema of {table}:")
    print(tabulate(schema, headers=["cid", "name", "type", "notnull", "dflt_value", "pk"], tablefmt="pretty"))

# Insert test data for Profiles and Layers tables and handle exceptions
try:
    cursor.execute("INSERT INTO Profiles (country_id, X, Y, orgc_dataset_id, orgc_profile_code) VALUES (1, 10.0, 20.0, 'dataset_001', 'profile_001');")
    cursor.execute("INSERT INTO Layers (profile_id, profile_layer_id, upper_depth, lower_depth, layer_name) VALUES (1, 1, 0.0, 10.0, 'Layer 1');")
    conn.commit()
except sqlite3.Error as e:
    print("An error occurred:", e)

# Retrieve and print data to verify insertion (showing up to 5 rows for Profiles and Layers)
for table in ['Countries', 'Profiles', 'Layers']:
    data = cursor.execute(f"SELECT * FROM {table} LIMIT 5;").fetchall()  # Limit to first 5 rows
    print(f"\nData in {table}: (showing up to 5 rows)")
    print(tabulate(data, headers=[desc[0] for desc in cursor.description], tablefmt="pretty"))

# Close the connection
conn.close()