import pandas as pd
import json
import numpy as np
from dateutil.parser import parse
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import contextily as ctx
import seaborn as sns
import folium
from folium.plugins import MarkerCluster
  

# Function to extract the first date from the dictionary-like structure
def extract_date(date_str):
    try:
        # Extract parts between curly braces
        dates = date_str.replace("{", "").replace("}", "").split(",")
        # Extract and return the first date found
        for date_part in dates:
            date_str = date_part.split(":")[1].strip()
            # Normalize date format (e.g., from "1992/02/17" to "1992-02-17")
            date_str = date_str.replace("/", "-")
            return date_str
    except (IndexError, ValueError, TypeError):
        return None

# Function to try multiple date formats
def try_parse_date(date_str):
    known_formats = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d"]
    for fmt in known_formats:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except (ValueError, TypeError):
            continue
    # Fallback to dateutil parser
    try:
        return parse(date_str, fuzzy=True)
    except (ValueError, TypeError):
        return pd.NaT
    

# Function to clean and preprocess the data
def preprocess_data(data):
    # Extract and convert date columns to datetime format
    date_columns = ['orgc_date']
    for col in date_columns:
        data[col] = data[col].apply(lambda x: try_parse_date(extract_date(str(x))) if pd.notnull(x) else pd.NaT)
    
    data = data.dropna(subset=['orgc_value'])
    data = data.dropna(subset=['orgc_value_avg'])
    data = data.dropna(subset=['orgc_profile_code'])

    # Handle missing data
    data = data.fillna({
        'country_name': 'Unknown',
        'profile_id': -1,
        'profile_layer_id': -1,
        'orgc_method': '{}',
        'layer_name': 'Same',
        'litter': 'Same'
    })

    # Clean and preprocess orgc_method column
    data['orgc_method'] = data['orgc_method'].apply(lambda x: json.dumps(x) if isinstance(x, dict) else str(x))

    # # Convert profile_id and profile_layer_id to string
    # data['profile_id'] = data['profile_id'].astype(float)
    # data['profile_layer_id'] = data['profile_layer_id'].astype(float)

    # Omit data where lower_depth is less than upper_depth
    data = data[data['lower_depth'] >= data['upper_depth']]

    data[['profile_id', 'profile_layer_id']] = data[['profile_id', 'profile_layer_id']].astype(int)
    data['orgc_profile_code'] = data['orgc_profile_code'].astype('string')

    data = data[data['orgc_value_avg'] <= 600]

    return data