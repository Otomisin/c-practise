import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

# Function to scrape data
@st.cache_data
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
    st.set_page_config(page_title='DTM Report Dashboard', page_icon='📊', layout="centered")
    st.title('Interactive Report Dashboard')
    st.caption(f'Reports updated as of: {datetime.now().strftime("%Y-%m-%d")}')

    # Display logo and custom message in the sidebar
    # st.sidebar.image('path_to_logo.png', use_column_width=True)  # Uncomment and replace path
    st.sidebar.markdown("### ABOUT")
    st.sidebar.info("This dashboard provides an interactive way to explore reports. Select filters from the sidebar to customize the display. You can download as a csv")
    
    st.markdown("---")
    st.sidebar.markdown("---")
    
    # Custom sidebar with reload option
    # st.sidebar.markdown("<h2 style='text-align: left;'>Data Management</h2>", unsafe_allow_html=True)
    if st.sidebar.button('Reload Data'):
        # This will clear the cache and reload the data
        st.cache_data.clear()
        st.experimental_rerun()

    # Load data
    df = scrape_data()
    
    # Sidebar for filtering
    st.sidebar.markdown("<h2 style='text-align: left;'>Filters</h2>", unsafe_allow_html=True)
    country_options = df['Country Name'].unique()
    


    # Select all countries option
    all_countries = st.sidebar.checkbox("Select All Countries", True)
    if all_countries:
        selected_countries = st.sidebar.multiselect('Select Country:', options=country_options, default=country_options)
    else:
        selected_countries = st.sidebar.multiselect('Select Country:', options=country_options)

    # Filter data based on selections
    filtered_data = df[df['Country Name'].isin(selected_countries)]

    # Displaying filtered data
    for index, row in filtered_data.iterrows():
        st.subheader(row['Title'])
        st.write(f"Published Date: {row['Published Date'].strftime('%d-%b-%Y')}")
        st.write(f"Country: {row['Country Name']}")
        st.write(row['Summary'])
        st.markdown(f"[Read More]({row['Link']})", unsafe_allow_html=True)

    # Download option for filtered data
    st.sidebar.markdown("### Download Data")
    csv = filtered_data.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
        label="Download filtered data as CSV",
        data=csv,
        file_name='filtered_data.csv',
        mime='text/csv',
    )
    
    col1, col2, col3 = st.sidebar.columns([1,2,1])
    with col1:
        st.image('IOMlogo.png', width=70)
    with col2:
      st.markdown(" Made by ***DTM-AKO***")

if __name__ == '__main__':
    app()
