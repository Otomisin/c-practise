import streamlit as st
import requests

def check_website_status():
    url = 'https://dtm.iom.int/reports'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'https://google.com/'
    }
    response = requests.get(url, headers=headers)
    return response.status_code

def app():
    st.title('Website Status Checker')
    status_code = check_website_status()
    if status_code == 200:
        st.success(f'The website is reachable. Status Code: {status_code}')
    else:
        st.error(f'Failed to reach the website. Status Code: {status_code}')

if __name__ == '__main__':
    app()
