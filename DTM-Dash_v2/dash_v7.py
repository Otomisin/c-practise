import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Function to scrape data
def scrape_data():
    url = 'https://dtm.iom.int/reports?search=&sort_by=field_published_date&sort_order=DESC'
    response = requests.get(url)
    response.encoding = 'utf-8'  # Force response encoding to UTF-8
    dtm_soup = BeautifulSoup(response.content, 'html.parser')
    dtm_reports = dtm_soup.find_all('div', class_='report-item1')
    reports_data = []

    for report in dtm_reports:
        title = report.find('a', class_='title').text.strip()
        report_html = str(report)  # Convert the BeautifulSoup object to string
        links = re.findall(r'href="(/reports/[^"]+)"', report_html)  # Apply regex to find all 'href' attribute values
        
        # Initialize report_link as None or a default value
        report_link = 'https://dtm.iom.int' + links[0] if links else None
        
        date = report.find('div', class_='date').text.split('·')[0].strip()
        summary_content = report.find('div', class_='content').text.strip()
        country_anchors = report.find_all('a', href=True)
        country_name = country_anchors[-1].text.strip() if country_anchors else 'Unknown'
        
        reports_data.append({
            'Title': title,
            'Summary': summary_content,
            'Link': report_link,
            'Published Date': pd.to_datetime(date),
            'Country Name': country_name
        })

    return pd.DataFrame(reports_data)

# Streamlit app setup
def app():
    st.title('Interactive Report Dashboard')

    # Add a button to trigger data reload
    if st.button('Reload Data'):
        with st.spinner('Loading data...'):
            # Update the session state with new data
            st.session_state['data'] = scrape_data()
            st.success('Data reloaded successfully!')

    # Load data initially if not already loaded
    if 'data' not in st.session_state:
        st.session_state['data'] = scrape_data()

    # Use the data stored in session state
    df = st.session_state['data']

    # Display some data as a sanity check
    st.write(df.head())

    # Implement the rest of your Streamlit UI logic here
    # For example, filtering options, displaying the data, etc.

if __name__ == '__main__':
    app()
