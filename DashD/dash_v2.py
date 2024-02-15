import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import random
import string

# Scraping script
url = 'https://dtm.iom.int/reports?search=&sort_by=field_published_date&sort_order=DESC'
response = requests.get(url)
response.encoding = 'utf-8'  # Force response encoding to UTF-8   
dtm_soup = BeautifulSoup(response.content, 'html.parser')
dtm_reports = dtm_soup.find_all('div', class_='report-item1')

reports_data = []
regex = r'href="(/reports/[^"]+)"'

for report in dtm_reports:
    title = report.find('a', class_='title').text.strip()
    report_html = str(report)  # Convert the BeautifulSoup object to string
    links = re.findall(regex, report_html)
    for link in links:
        report_link = f'https://dtm.iom.int{link}'  # Concatenate to form full URL
    date = report.find('div', class_='date').text.split('·')[0].strip()
    title_content = report.find('div', class_='content').text.strip()
    country_anchors = report.find_all('a', href=True)
    if country_anchors:
        country_name = country_anchors[-1].text

        # Generate ID using the first three letters of the country_name and random characters
        country_id = country_name[:3] + ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))

    reports_data.append({
        'Title': title,
        'Summary': title_content,
        'Link': report_link,
        'Published Date': date,
        'country_name': country_name,
        'Country ID': country_id
    })

# Creating DataFrame
df = pd.DataFrame(reports_data)

# Streamlit app
def app():
    st.title('Interactive Report Dashboard')

    # Sidebar filters
    country = st.sidebar.multiselect('Select Country:', options=df['country_name'].unique(), default=df['country_name'].unique())
    # thematic = st.sidebar.multiselect('Select Thematic:', options=df['Thematics'].unique(), default=df['Thematics'].unique())

    # Filtering data
    filtered_data = df[(df['country_name'].isin(country))]

    # Displaying filtered data
    for index, row in filtered_data.iterrows():
        st.subheader(row['Title'])
        st.write(f"Published Date: {row['Published Date']}")
        st.write(f"Country: {row['country_name']}")
        st.write(row['Summary'])
        st.markdown(f"[Read More]({row['Link']})", unsafe_allow_html=True)

    # Download button for CSV
    st.sidebar.markdown('## Download Data')
    download_btn = st.sidebar.button('Download Data as CSV')

    if download_btn:
        # Add Data Points and Reviewed Data Point columns
        df['Data Points'] = 0  # Replace with your data points
        df['Reviewed Data Point'] = 0  # Replace with your reviewed data points
        df.to_csv('filtered_data.csv', index=False)
        st.sidebar.success('Data downloaded successfully.')

if __name__ == '__main__':
    app()
