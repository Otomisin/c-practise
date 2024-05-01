import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta
from dateutil import parser

# Logging setup
import logging
logging.basicConfig(level=logging.INFO)

# Function to scrape data
@st.cache
def scrape_data_new():
    url = 'https://dtm.iom.int/reports?search=&sort_by=field_published_date&sort_order=DESC'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    dtm_soup = BeautifulSoup(response.content, 'html.parser')
    dtm_reports = dtm_soup.find_all('div', class_='report-item1')
    reports_data = []

    for report in dtm_reports:
        try:
            title = report.find('a', class_='title').text.strip()
            report_html = str(report)
            links = re.findall(r'href="(/reports/[^"]+)"', report_html)
            report_link = f'https://dtm.iom.int{links[0]}' if links else None
            date_info = report.find('div', class_='date').text.split('·')
            date_text = date_info[0].strip()
            date = parser.parse(date_text, fuzzy=True)
            region = date_info[1].strip() if len(date_info) > 1 else 'Unknown'
            country_name = date_info[2].strip() if len(date_info) > 2 else 'Unknown'
            report_type = date_info[3].strip() if len(date_info) > 3 else 'Unknown'
            summary_content = report.find('div', class_='content').text.strip()

            reports_data.append({
                'Title': title,
                'Summary': summary_content,
                'Link': report_link,
                'Published Date': date,
                'Country Name': country_name,
                'Region': region,
                'Report Type': report_type
            })
        except Exception as e:
            logging.error("Error processing a report: %s", e)
            continue  # Skip report if any error occurs

    return pd.DataFrame(reports_data)

# Streamlit app setup
def app():
    st.set_page_config(page_title='DTM Report Dashboard', page_icon='📊', layout="centered")
    df = scrape_data_new()

    # Debug: Display DataFrame columns and first few rows
    st.write("DataFrame Columns:", df.columns)
    st.write("First few rows of the DataFrame:", df.head())

    if 'Published Date' not in df.columns:
        st.error("Data does not contain the 'Published Date' column.")
        st.stop()

    # Further processing as needed...
    # (Rest of your Streamlit app code here...)

if __name__ == '__main__':
    app()
