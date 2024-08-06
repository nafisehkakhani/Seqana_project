-- Drop tables if they exist
DROP TABLE IF EXISTS Profiles;
DROP TABLE IF EXISTS Profile_Layers;
DROP TABLE IF EXISTS OrgC;

-- Create Profiles Table
CREATE TABLE Profiles (
    profile_id INTEGER PRIMARY KEY,
    X REAL NOT NULL,
    Y REAL NOT NULL,
    country_name TEXT NOT NULL
);

-- Create Profile Layers Table
CREATE TABLE Profile_Layers (
    profile_layer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_id INTEGER,
    upper_depth REAL,
    lower_depth REAL,
    layer_name TEXT,
    litter TEXT,
    FOREIGN KEY (profile_id) REFERENCES Profiles(profile_id)
);

-- Create OrgC Table
CREATE TABLE OrgC (
    layer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_layer_id INTEGER,
    orgc_value TEXT NOT NULL,
    orgc_value_avg REAL NOT NULL,
    orgc_method TEXT,
    orgc_date DATE,
    orgc_dataset_id TEXT NOT NULL,
    orgc_profile_code TEXT,
    FOREIGN KEY (profile_layer_id) REFERENCES Profile_Layers(profile_layer_id) 
);


-- -- Create OrgC Table
-- CREATE TABLE OrgC (
--     layer_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     profile_layer_id INTEGER,
--     orgc_value TEXT NOT NULL,
--     orgc_value_avg REAL NOT NULL,
--     orgc_method TEXT,
--     orgc_date DATE NOT NULL,
--     orgc_dataset_id TEXT NOT NULL,
--     orgc_profile_code TEXT NOT NULL,
--     FOREIGN KEY (profile_layer_id) REFERENCES Profile_Layers(profile_layer_id)
-- );