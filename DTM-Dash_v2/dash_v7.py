import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime, timedelta

# Web Crawler Functions
@st.cache(allow_output_mutation=True, show_spinner=True)
def scrape_data_new():
    url = 'https://dtm.iom.int/reports?search=&sort_by=field_published_date&sort_order=DESC'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            dtm_soup = BeautifulSoup(response.content, 'html.parser')
            dtm_reports = dtm_soup.find_all('div', class_='report-item1')
            reports_data = []

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

            return pd.DataFrame(reports_data), None
        else:
            return pd.DataFrame(), f"HTTP Error: Status code {response.status_code}"
    except requests.RequestException as e:
        return pd.DataFrame(), f"Request failed: {e}"
    except Exception as e:
        return pd.DataFrame(), f"Failed to scrape data: {e}"

# Streamlit app setup
def app():
    st.set_page_config(page_title='DTM Report Dashboard', page_icon='📊', layout="centered")
    
    df, error_message = scrape_data_new()
    if error_message:
        st.error(error_message)
        return
    if df.empty:
        st.warning("No data available. Please check the scraper or data source.")
        return

    now = datetime.now()
    two_days_ago = now - timedelta(days=2)
    try:
        recent_reports = df[df['Published Date'] >= two_days_ago]
        total_recent_reports = len(recent_reports)
        total_report_crawled = len(df)
    except Exception as e:
        st.error(f"Error processing dates in the data: {e}")
        return

    least_date = df['Published Date'].min().strftime('%Y-%m-%d') if not df['Published Date'].isnull().all() else "No Dates Available"
    last_date = df['Published Date'].max().strftime('%Y-%m-%d') if not df['Published Date'].isnull().all() else "No Dates Available"

    st.image('https://raw.githubusercontent.com/Otomisin/c-practise/main/DTM-Dash/IOMlogo.png', width=70)
    st.title('DTM Report Dashboard')
    st.caption(f'Reports updated as of: {now.strftime("%Y-%m-%d")}')
    st.write(f" **DATE:** {last_date} - {least_date} | **{total_report_crawled} Reports** Crawled | **{total_recent_reports} Reports** in the last 48hrs")
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

        if st.sidebar.button('Reload Data'):
            st.caching.clear_cache()
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
        formatted_date = row['Published Date'].strftime('%d-%b-%Y') if pd.notna(row['Published Date']) else "Date Not Available"
        st.markdown(f"**{formatted_date} | {row['Country Name']} | {row['Report Type']}**")
        st.write(row['Summary'])
        st.markdown(f"[Read More]({row['Link']})", unsafe_allow_html=True)

    csv = filtered_data.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
    st.sidebar.download_button(
        label="Download filtered data as CSV",
        data=csv,
        file_name='filtered_data.csv',
        mime='text/csv',
    )

if __name__ == '__main__':
    app()
