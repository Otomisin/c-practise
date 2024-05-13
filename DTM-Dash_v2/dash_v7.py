import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def setup_webdriver():
    # Set up headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1200")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--no-sandbox")  # required if running as root user. otherwise you would get no sandbox errors.
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Create a new instance of the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def check_website_status():
    driver = setup_webdriver()
    url = 'https://dtm.iom.int/reports'
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    status = driver.title
    driver.quit()
    return status

def app():
    st.title('Website Status Checker with Selenium')
    page_title = check_website_status()
    if page_title:
        st.success(f'The website was reached successfully. Page Title: {page_title}')
    else:
        st.error('Failed to reach the website.')

if __name__ == '__main__':
    app()
