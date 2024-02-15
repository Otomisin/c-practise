import pandas as pd
from sqlalchemy import create_engine
import os
from datetime import datetime, timedelta

# Function to load data from a folder
def load_data(folder_path):
    files = os.listdir(folder_path)
    data = pd.DataFrame()

    for file in files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)  # adjust based on your file type
        data = pd.concat([data, df])

    return data

# Function to connect to the database
def connect_to_database(database_url):
    engine = create_engine(database_url)
    return engine

# Function to store data in the database
def store_data_in_database(data, table_name, engine):
    data.to_sql(table_name, con=engine, if_exists='replace', index=False)

# Function to display table information
def display_table_info(table_name, engine):
    table_info = pd.read_sql_query(f"SELECT * FROM {table_name}", con=engine)
    print(table_info)

# Function to update the table with new data from the last two days
def update_table_with_new_data(data, table_name, engine):
    today = datetime.now()
    two_days_ago = today - timedelta(days=2)

    latest_data = data[data['timestamp'] >= two_days_ago]

    latest_data.to_sql(table_name, con=engine, if_exists='append', index=False)

# Main function
def main():
    folder_path = "path/to/your/folder"
    database_url = "postgresql://username:password@localhost:5432/your_database"
    table_name = "your_table"

    # Load data from the folder
    data = load_data(folder_path)

    # Connect to the database
    engine = connect_to_database(database_url)

    # Store data in the database
    store_data_in_database(data, table_name, engine)

    # Display table information
    display_table_info(table_name, engine)

    # Update the table with new data from the last two days
    update_table_with_new_data(data, table_name, engine)

if __name__ == "__main__":
    main()
