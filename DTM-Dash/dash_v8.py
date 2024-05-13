import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import random
from datetime import datetime, timedelta

# Web Crawler Functions
# Function to scrape data
@st.cache(allow_output_mutation=True, show_spinner=True)
def scrape_data_new(pages=1):
    base_url = 'https://dtm.iom.int/reports'
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
        # More user agents can be added here
    ]
    proxies = {
        'http': 'http://10.10.1.10:3128',  # Update with actual proxy address
        'https': 'https://10.10.1.11:1080',  # Update with actual proxy address
    }
    headers = {
        'User-Agent': random.choice(user_agents)
    }
    reports_data = []

    for page in range(pages):
        url = f'{base_url}?page={page}' if page > 0 else base_url

        response = requests.get(url, headers=headers, proxies=proxies)
        if response.status_code != 200:
            st.error(f'Failed to fetch data from {url}. Status code: {response.status_code}')
            continue  # Skip this page on error
        
        response.encoding = 'utf-8'
        dtm_soup = BeautifulSoup(response.content, 'html.parser')
        dtm_reports = dtm_soup.find_all('div', class_='report-item1')

        for report in dtm_reports:
            title = report.find('a', class_='title').text.strip()
            report_html = str(report)
            links = re.findall(r'href="(/reports/[^"]+)"', report_html)
            report_link = f'https://dtm.iom.int{links[0]}' if links else None
            date_info = report.find('div', class_='date').text.split('·')
            date = pd.to_datetime(date_info[0].strip(), errors='coerce', format='%b %d, %Y')
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

    return pd.DataFrame(reports_data)

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
