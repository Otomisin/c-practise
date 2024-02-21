import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

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

# Streamlit app setup
def app():
    st.title('Interactive Report Dashboard')

    # Reload button with data loading
    if st.button('Reload Data'):
        with st.spinner('Loading data...'):
            st.session_state['data'] = scrape_data()
            st.success('Data reloaded successfully!')

    # Load data initially if not already loaded
    if 'data' not in st.session_state:
        st.session_state['data'] = scrape_data()

    # Data loaded into DataFrame
    df = st.session_state['data']

    # Sidebar filters
    st.sidebar.subheader('Filters')
    all_countries_option = st.sidebar.checkbox('Select All Countries', value=True)
    country_options = df['Country Name'].unique()
    if all_countries_option:
        selected_countries = st.sidebar.multiselect('Select Country:', options=country_options, default=country_options)
    else:
        selected_countries = st.sidebar.multiselect('Select Country:', options=country_options)
    
    # Date range filter
    min_date = df['Published Date'].min().timestamp()
    max_date = df['Published Date'].max().timestamp()
    date_range = st.sidebar.slider('Select Date Range:', min_value=min_date, max_value=max_date, 
                                   value=(min_date, max_date), format="MM/DD/YYYY")
    start_date, end_date = pd.to_datetime([date_range[0], date_range[1]], unit='s')

    # Filter data based on selections
    filtered_data = df[(df['Country Name'].isin(selected_countries)) & 
                       (df['Published Date'] >= start_date) & 
                       (df['Published Date'] <= end_date)]

    # Displaying filtered data
    for index, row in filtered_data.iterrows():
        st.subheader(row['Title'])
        st.write(f"Published Date: {row['Published Date'].strftime('%d-%b-%Y')}")
        st.write(f"Country: {row['Country Name']}")
        st.write(row['Summary'])
        st.markdown(f"[Read More]({row['Link']})", unsafe_allow_html=True)

    # CSV Download
    st.sidebar.markdown('## Download Data')
    csv = filtered_data.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
        label="Download filtered data as CSV",
        data=csv,
        file_name='filtered_data.csv',
        mime='text/csv',
    )

    # For PDF display, you would generate a PDF file from `filtered_data` here and provide a download link.
    # This step is theoretical in this context and requires backend processing to create a PDF.

if __name__ == '__main__':
    app()
