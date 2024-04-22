import pandas as pd
from sqlalchemy import create_engine, text

# Load the data from the CSV file
file_path = 'D:/Fuck this thing/filtered_data.csv'
df = pd.read_csv(file_path)

# Simplify column names: replace spaces and special characters with underscores
df.columns = df.columns.str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('/', '_per_')

# Confirm new column names
print("New column names:", df.columns)

# Database connection string
username = 'r_khevaria'
password = 'islandENGLISH72'
host = 'dev.cs.smu.ca'
port = '3306'
database = 'r_khevaria'
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

# SQL command to create a new table with simplified column names
sql_command = """
CREATE TABLE IF NOT EXISTS rentListings (
    Price DECIMAL(10, 2),
    Property_Type VARCHAR(255),
    Rooms INT,
    Den_Included BOOLEAN,
    Number_of_Bathrooms INT,
    Latitude DECIMAL(9, 6),
    Longitude DECIMAL(9, 6),
    Size_sqft INT,
    Walk_Score INT,
    Transit_Score INT,
    Bike_Score INT,
    Time_to_Nearest_Hospital INT,
    Time_to_Nearest_Police_Station INT,
    Time_to_Nearest_Store INT,
    Time_to_Nearest_Pharmacy INT
);
"""

# Execute the SQL command to create the table if it doesn't exist
with engine.connect() as connection:
    connection.execute(text(sql_command))

# Load the data into the new database table
df.to_sql('rentListings', con=engine, if_exists='append', index=False)

print("Data loaded successfully into the 'rentListings' table.")
