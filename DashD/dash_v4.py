import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Scraping script
# ---------------
url = 'https://dtm.iom.int/reports?search=&sort_by=field_published_date&sort_order=DESC'

# Correctly make the request and store the response
response = requests.get(url)
response.encoding = 'utf-8'  # Force response encoding to UTF-8
dtm_soup = BeautifulSoup(response.content, 'html.parser')

# Corrected search for divs by class name, assuming you're looking for items within a specific structure
dtm_reports = dtm_soup.find_all('div', class_='report-item1')

# Initialize a list to hold our extracted data
reports_data = []

# Iterate through each report and extract information
for report in dtm_reports:
    title = report.find('a', class_='title').text.strip()
    report_html = str(report)  # Convert the BeautifulSoup object to string
    links = re.findall(r'href="(/reports/[^"]+)"', report_html)  # Apply regex to find all 'href' attribute values
    
    # Initialize report_link as None or a default value
    report_link = None
    if links:
        report_link = f'https://dtm.iom.int{links[0]}'  # Use the first link found
    
    date = report.find('div', class_='date').text.split('·')[0].strip()
    summary_content = report.find('div', class_='content').text.strip()
    country_anchors = report.find_all('a', href=True)
    country_name = 'Unknown'  # Default value in case country name is not found
    if country_anchors:
        country_name = country_anchors[-1].text.strip()  # Extract the text content of the last anchor tag
        
    # Append the extracted information to our list
    reports_data.append({
        'Title': title,
        'Summary': summary_content,
        'Link': report_link,
        'Published Date': pd.to_datetime(date),  # Convert to datetime immediately
        'Country Name': country_name
    })

# Create a DataFrame from the reports data
df = pd.DataFrame(reports_data)

# Streamlit app
def app():
    st.title('Interactive Report Dashboard')

    # Sidebar filters
    st.sidebar.subheader('Filters')
    all_countries_option = st.sidebar.checkbox('Select All Countries', value=True)
    country_options = df['Country Name'].unique()
    if all_countries_option:
        selected_countries = st.sidebar.multiselect('Select Country:', options=country_options, default=country_options)
    else:
        selected_countries = st.sidebar.multiselect('Select Country:', options=country_options, default=[country_options[0]])
    
    report_id = st.sidebar.text_input('Enter Report ID:', '')
    
    # Convert date range to timestamps
    min_date = df['Published Date'].min().timestamp()
    max_date = df['Published Date'].max().timestamp()
    date_range = st.sidebar.slider('Select Date Range:', min_value=min_date, max_value=max_date, 
                                   value=(min_date, max_date), format="MM/DD/YYYY")

    # Unpack the date range tuple and convert back to datetime for filtering
    start_date, end_date = pd.to_datetime([date_range[0], date_range[1]], unit='s')

    # Filtering data
    filtered_data = df[(df['Country Name'].isin(selected_countries)) & 
                       (df['Published Date'] >= start_date) & (df['Published Date'] <= end_date)]

    # Displaying filtered data
    for index, row in filtered_data.iterrows():
        st.subheader(row['Title'])
        st.write(f"Published Date: {row['Published Date'].strftime('%d-%b-%Y')}")
        st.write(f"Country: {row['Country Name']}")
        st.write(row['Summary'])
        st.markdown(f"[Read More]({row['Link']})", unsafe_allow_html=True)

    # Download button for CSV
    st.sidebar.markdown('## Download Data')
    if st.sidebar.button('Download Data as CSV'):
        csv = filtered_data.to_csv(index=False).encode('utf-8')
        st.sidebar.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='filtered_data.csv',
            mime='text/csv',
        )

if __name__ == '__main__':
    app()
