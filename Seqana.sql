-- Drop existing tables if they exist
DROP TABLE IF EXISTS Layers;
DROP TABLE IF EXISTS Profiles;
DROP TABLE IF EXISTS Countries;

-- Create Countries table
CREATE TABLE Countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_name TEXT UNIQUE NOT NULL
);

-- Create Profiles table
CREATE TABLE Profiles (
    profile_id INTEGER PRIMARY KEY,
    country_id INTEGER NOT NULL,
    X REAL NOT NULL,
    Y REAL NOT NULL,
    orgc_dataset_id TEXT NOT NULL,
    orgc_profile_code TEXT NOT NULL,
    FOREIGN KEY (country_id) REFERENCES Countries(country_id)
);

-- Create Layers table
CREATE TABLE Layers (
    layer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_id INTEGER NOT NULL,
    profile_layer_id INTEGER NOT NULL,
    upper_depth REAL NOT NULL,
    lower_depth REAL NOT NULL,
    layer_name TEXT NOT NULL,
    litter TEXT,
    orgc_value_avg REAL,
    orgc_method TEXT,
    orgc_date DATE,
    FOREIGN KEY (profile_id) REFERENCES Profiles(profile_id)
);


