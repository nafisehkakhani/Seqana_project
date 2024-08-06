# Seqana Data Engineering Challenge

![Banner](img/Spatial_Distribution_of_SOC.png)

## Project Description
This project is a data engineering challenge that involves processing and analyzing soil data. The goal is to clean, preprocess, and visualize the data to gain insights into soil properties and ultimately create a soil database using SQL.

## Features
- Data cleaning and preprocessing
- Data normalization and database creation
- Geospatial data processing and visualization
- Interactive map generation

## Project Directory Structure

```
Seqana-Project/
├── img/
│   └── Spatial_Distribution_of_SOC.png
├── main.py
├── utils/
│   └── utils.py
├── run_project.sh
├── exploratory_data_analysis.ipynb
├── requirements.txt
├── README.md
├── soil_data.db
├── test_sql.py
├── map.html
├── Seqana.sql
└── .gitignore
```

## Data Exploration
The initial data exploration and analysis are documented in the `exploratory_data_analysis.ipynb` Jupyter notebook. This notebook contains:
- Detailed examination of the raw soil data.
- Data cleaning steps, including handling missing values and correcting data types.
- Visualizations to understand the distribution and relationships within the data.

## Data Normalization and Database Formation
After exploring and cleaning the data, the next step is data normalization and database formation. This process is handled in the `main.py` script:
- **Data Normalization**: The cleaned data is organized into three tables: Countries, Profiles, and Layers. The Countries table, despite having only one country, provides a scalable structure for future data. The Profiles table stores information about unique soil profiles and links to the Countries table. Each profile can have multiple layers, which are detailed in the Layers table linked to the Profiles table. This organization reduces redundancy, ensures data integrity, and makes it easier to manage and query the data.
- **Database Creation**: The normalized data is then inserted into an SQLite database `soil_data.db` by running `main.py`. The database schema is defined in the `Seqana.sql` script, which sets up the database structure when executed.

## Testing the Database
To ensure the database is correctly set up and functioning, we have included a `test_sql.py` script. This script performs the following tests:
- Verifies the integrity of the database structure.
- Checks for the correct insertion of data into the tables.
- Runs sample queries to ensure data can be retrieved as expected.

## Setup and Run

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/nafisehkakhani/Seqana_project.git
    cd Seqana_project
    ```

2. **Create and Activate Conda Environment**:
    ```sh
    conda create --name seqana_test_env
    conda activate seqana_test_env
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Project**:
    ```sh
    ./run_project.sh <path_to_excel_file>
    ```

## Notes
- Ensure you have `conda` installed and configured on your system.
- Replace `<path_to_excel_file>` with the actual path to your Excel file.