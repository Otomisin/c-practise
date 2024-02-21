import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

# Function to scrape data
def scrape_data():
    url = 'https://dtm.iom.int/reports?search=&sort_by=field_published_date&sort_order=DESC'
    response = requests.get(url)
    response.encoding = 'utf-8'
    dtm_soup = BeautifulSoup(response.content, 'html.parser')
    dtm_reports = dtm_soup.find_all('div', class_='report-item1')
    reports_data = []

    for report in dtm_reports:
        title = report.find('a', class_='title').text.strip()
        report_html = str(report)
        links = re.findall(r'href="(/reports/[^"]+)"', report_html)
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

@st.cache
def today():
    return datetime.now().strftime("%Y-%m-%d")

# Streamlit app setup
def app():
    st.set_page_config(page_title='Interactive Report Dashboard', page_icon='📊', layout="wide")
    st.title('Interactive Report Dashboard')
    st.caption(f'Reports updated as of: {today()}')

    # Custom sidebar
    st.sidebar.markdown("<h1 style='text-align: left;'>FILTERS</h1>", unsafe_allow_html=True)
    st.sidebar.markdown('*Use the filters below to customize the displayed reports.*')
    st.sidebar.divider()

    # Custom style
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # Data manipulation and display as before
    if 'data' not in st.session_state or st.button('Reload Data'):
        st.session_state['data'] = scrape_data()

    df = st.session_state['data']
    # (The rest of your data manipulation and Streamlit UI code goes here)

    # Example: Sidebar for filtering
    country_options = df['Country Name'].unique()
    selected_countries = st.sidebar.multiselect('Select Country:', options=country_options, default=country_options)

    # Display logo and custom message in the sidebar
    st.sidebar.image('path_to_logo.png', use_column_width=True)  # Update 'path_to_logo.png' with the actual path or URL
    st.sidebar.markdown("### About")
    st.sidebar.info("This dashboard provides an interactive way to explore reports. Select filters from the sidebar to customize the display.")

    # Example: Display filtered data
    filtered_data = df[df['Country Name'].isin(selected_countries)]
    for index, row in filtered_data.iterrows():
        st.subheader(row['Title'])
        st.write(f"Published Date: {row['Published Date'].strftime('%d-%b-%Y')}")
        st.write(f"Country: {row['Country Name']}")
        st.write(row['Summary'])
        st.markdown(f"[Read More]({row['Link']})", unsafe_allow_html=True)

if __name__ == '__main__':
    app()
