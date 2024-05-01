@st.cache(allow_output_mutation=True, show_spinner=True)
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
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # your parsing logic here
            return pd.DataFrame(), None
        else:
            return pd.DataFrame(), f"HTTP Error: Status code {response.status_code}"
    except requests.RequestException as e:
        return pd.DataFrame(), f"Request failed: {e}"

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
