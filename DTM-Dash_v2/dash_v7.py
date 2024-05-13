import streamlit as st
import pandas as pd

# Function to simulate scraping data
@st.cache
def scrape_data_new():
    # Dummy data
    data = {
        'Title': ['Report 1', 'Report 2', 'Report 3'],
        'Published Date': ['2024-05-10', '2024-05-11', '2024-05-12'],
        'Summary': ['Summary 1', 'Summary 2', 'Summary 3'],
        'Link': ['Link 1', 'Link 2', 'Link 3'],
        'Country Name': ['Country 1', 'Country 2', 'Country 3'],
        'Region': ['Region 1', 'Region 2', 'Region 3'],
        'Report Type': ['Type 1', 'Type 2', 'Type 3']
    }
    return pd.DataFrame(data)

# Streamlit app setup
def app():
    st.set_page_config(page_title='DTM Report Dashboard', page_icon='📊', layout="wide")
    st.title('DTM Report Dashboard')

    # Get data
    df = scrape_data_new()

    # Display head of the DataFrame
    st.write("## Head of the DataFrame")
    st.write(df.head())

if __name__ == '__main__':
    app()
