import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Function to scrape data
@st.cache_data()
def scrape_data(pages=10):
    url = 'https://apnews.com/hub/migration'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    data = []

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    page_items = soup.find_all('div', class_='PageList-items-item')

    for item in page_items:
        page_promo = item.find('div', class_='PagePromo')
        if page_promo:
            link_tag = page_promo.find('a', class_='Link')
            link = link_tag['href'] if link_tag else 'No link available'
            title_tag = page_promo.find('h3', class_='PagePromo-title')
            title = title_tag.text.strip() if title_tag else 'No title available'
            description_tag = page_promo.find('div', class_='PagePromo-description')
            description = description_tag.text.strip() if description_tag else 'No description available'

            # Correct targeting of the date element using the data-date attribute
            date_tag = page_promo.find('span', attrs={'data-date': True})
            date = date_tag.text if date_tag else 'Date not available'

            data.append({
                'Title': title,
                'Date': date
            })

    return pd.DataFrame(data)

# Streamlit app setup
def app():
    st.set_page_config(page_title='AP News Migration Hub', page_icon='📰', layout="wide")
    st.title('AP News Migration Hub')

    # Get data
    df = scrape_data()

    # Display head of the DataFrame
    st.write("## Head of the DataFrame")
    st.write(df.head())

if __name__ == '__main__':
    app()
