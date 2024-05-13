import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta

# Web Crawler Functions
@st.cache_data()  # Using built-in Streamlit caching
def scrape_data_new(pages=15):
    base_url = 'https://dtm.iom.int/reports'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    reports_data = []
    for page in range(0, pages + 1):
        params = {
            'search': '',
            'sort_by': 'field_published_date',
            'sort_order': 'DESC',
            'page': '' if page == 0 else page
        }
        response = requests.get(base_url, headers=headers, params=params)
        response.encoding = 'utf-8'
        dtm_soup = BeautifulSoup(response.content, 'html.parser')
        dtm_reports = dtm_soup.find_all('div', class_='report-item1')

        for report in dtm_reports:
            title = report.find('a', class_='title').text.strip()
            report_html = str(report)
            links = re.findall(r'href="(/reports/[^"]+)"', report_html)
            report_link = f'https://dtm.iom.int{links[0]}' if links else None
            date_info = report.find('div', class_='date').text.split('·')
            date = pd.to_datetime(date_info[0].strip(), errors='coerce', format='%b %d %Y')
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
    st.set_page_config(page_title='DTM Report Dashboard', page_icon='📊', layout="centered")
    df = scrape_data_new()
    now = datetime.now()
    st.image('https://raw.githubusercontent.com/Otomisin/c-practise/main/DTM-Dash/IOMlogo.png', width=70)
    st.title('DTM Report Dashboard')
    st.caption(f'Reports updated as of: {now.strftime("%Y-%m-%d")}')

    # Date range picker
    start_date, end_date = st.sidebar.date_input("Select Date Range", [now - timedelta(days=30), now])
    df = df[(df['Published Date'] >= start_date) & (df['Published Date'] <= end_date)]

    country_options = df['Country Name'].unique()
    selected_countries = st.sidebar.multiselect('Filter by Country:', options=country_options, default=country_options)
    df = df[df['Country Name'].isin(selected_countries)]

    st.write(f"Filtered by date: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')} | {len(df)} Reports")
    st.markdown("---")

    # Display filtered reports
    for index, row in df.iterrows():
        st.markdown(f"### {row['Title']}")
        formatted_date = row['Published Date'].strftime('%d-%b-%Y') if pd.notna(row['Published Date']) else "Date Not Available"
        st.markdown(f"**{formatted_date} | {row['Country Name']} | {row['Report Type']}**")
        st.write(row['Summary'])
        st.markdown(f"[Read More]({row['Link']})", unsafe_allow_html=True)

    # CSV download
    csv = df.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
    st.sidebar.download_button(
        label="Download filtered data as CSV",
        data=csv,
        file_name='filtered_data.csv',
        mime='text/csv',
    )

if __name__ == '__main__':
    app()
