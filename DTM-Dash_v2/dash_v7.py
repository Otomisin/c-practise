import streamlit as st
import requests

def check_website_status():
    url = 'https://dtm.iom.int/reports'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5'
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
