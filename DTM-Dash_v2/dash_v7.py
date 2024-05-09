import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta

# Web Crawler Functions
# Function to scrape data
@st.cache_data()  # Updated to use the built-in Streamlit caching
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
        title = report.find('a', class_='title').text.strip()
        report_html = str(report)
        links = re.findall(r'href="(/reports/[^"]+)"', report_html)
        report_link = f'https://dtm.iom.int{links[0]}' if links else None
        date_info = report.find('div', class_='date').text.split('·')
        region = date_info[1].strip() if len(date_info) > 1 else 'Unknown'
        country_name = date_info[2].strip() if len(date_info) > 2 else 'Unknown'
        report_type = date_info[3].strip() if len(date_info) > 3 else 'Unknown'
        summary_content = report.find('div', class_='content').text.strip()

        reports_data.append({
            'Title': title,
            'Summary': summary_content,
            'Link': report_link,
            'Country Name': country_name,
            'Region': region,
            'Report Type': report_type
        })

    return pd.DataFrame(reports_data)

# Streamlit app setup
def app():
    st.set_page_config(page_title='DTM Report Dashboard', page_icon='📊', layout="centered")
    df = scrape_data_new()

    st.image('https://raw.githubusercontent.com/Otomisin/c-practise/main/DTM-Dash/IOMlogo.png', width=70)
    st.title('DTM Report Dashboard')
    st.caption(f'Reports are continually updated.')
    st.markdown("---")

    with st.sidebar:
        st.markdown("### DATA POINT - TOOLS")
        with st.expander("**About this App**"):
            st.write("""
                This dashboard provides an interactive way to explore reports published by IOM DTM. 
                Select filters from the sidebar to customize the display. You can download data as CSV.
        
                For more information, visit [DTM](https://dtm.iom.int/).
        
                ### Contact
                For queries, please contact us at [here](https://dtm.iom.int/contact).
                """)
        st.markdown("---")

        if st.sidebar.button('Reload Data'):
            st.experimental_rerun()

    country_options = df['Country Name'].unique()

    all_countries = st.sidebar.checkbox("Select All Countries", True)
    if all_countries:
        selected_countries = st.sidebar.multiselect('Select Country:', options=country_options, default=country_options)
    else:
        selected_countries = st.sidebar.multiselect('Select Country:', options=country_options)

    filtered_data = df[df['Country Name'].isin(selected_countries)]

    for index, row in filtered_data.iterrows():
        st.markdown(f"### {row['Title']}")
        st.markdown(f"**{row['Country Name']} | {row['Report Type']}**")
        st.write(row['Summary'])
        st.markdown(f"[Read More]({row['Link']})", unsafe_allow_html=True)

    st.sidebar.markdown("### Download Data")
    csv = filtered_data.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
    st.sidebar.download_button(
        label="Download filtered data as CSV",
        data=csv,
        file_name='filtered_data.csv',
        mime='text/csv',
    )

if __name__ == '__main__':
    app()
