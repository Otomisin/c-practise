import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Function to scrape data from IOM's DTM website
@st.cache(allow_output_mutation=True)
def scrape_data_new():
    url = 'https://dtm.iom.int/reports?search=&sort_by=field_published_date&sort_order=DESC'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'https://www.google.com/'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    report_items = soup.find_all('div', class_='report-item1')
    reports_data = []

    for item in report_items:
        title = item.find('a', class_='title').text.strip()
        report_html = str(item)
        links = re.findall(r'href="(/reports/[^"]+)"', report_html)
        report_link = f'https://dtm.iom.int{links[0]}' if links else None
        date_info = item.find('div', class_='date').text.split('·')
        date = pd.to_datetime(date_info[0].strip(), errors='coerce')
        region = date_info[1].strip() if len(date_info) > 1 else 'Unknown'
        country_name = date_info[2].strip() if len(date_info) > 2 else 'Unknown'
        report_type = date_info[3].strip() if len(date_info) > 3 else 'Unknown'
        summary = item.find('div', class_='content').text.strip()

        reports_data.append({
            'Title': title,
            'Summary': summary,
            'Link': report_link,
            'Published Date': date,
            'Country Name': country_name,
            'Region': region,
            'Report Type': report_type
        })

    return pd.DataFrame(reports_data)

# Setting up the Streamlit UI
def main():
    st.title("Displacement Tracking Matrix (DTM) Reports Dashboard")
    st.write("This dashboard displays the latest reports from the IOM's Displacement Tracking Matrix website.")

    if st.button("Load Data"):
        df = scrape_data_new()
        st.write(df)
    else:
        st.write("Click the button above to load the latest DTM reports.")

if __name__ == "__main__":
    main()
