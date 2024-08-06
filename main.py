from utils.utils import *
import pandas as pd
import sqlite3
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description='Normalize data and insert into SQLite database.')
parser.add_argument('file_path', type=str, help='Path to the raw Excel data file')
args = parser.parse_args()

# Load the raw data
raw_data = pd.read_excel(args.file_path)

# Preprocess the data
clean_data = preprocess_data(raw_data)

# Normalize the data
# Step 2.1: Create Countries DataFrame
countries_df = clean_data[['country_name']].drop_duplicates().reset_index(drop=True)
countries_df['country_id'] = countries_df.index + 1

# Step 2.2: Create Profiles DataFrame
clean_data = clean_data.merge(countries_df, on='country_name', how='left')
profiles_df = clean_data[['profile_id', 'country_id', 'X', 'Y', 'orgc_dataset_id', 'orgc_profile_code']].drop_duplicates().reset_index(drop=True)

# Step 2.3: Create Layers DataFrame
layers_df = clean_data[['profile_id', 'profile_layer_id', 'upper_depth', 'lower_depth', 'layer_name', 'litter', 'orgc_value_avg', 'orgc_method', 'orgc_date']]

# Create the SQLite database and insert the data
conn = sqlite3.connect('soil_data.db')
cursor = conn.cursor()

# Read and execute the schema.sql script
with open('Seqana.sql', 'r') as file:
    sql_script = file.read()
cursor.executescript(sql_script)

# Insert data into Countries table
countries_df.to_sql('Countries', conn, if_exists='append', index=False)

# Insert data into Profiles table
profiles_df.to_sql('Profiles', conn, if_exists='append', index=False)

# Insert data into Layers table
layers_df.to_sql('Layers', conn, if_exists='append', index=False)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data has been successfully inserted into the SQLite database.")
