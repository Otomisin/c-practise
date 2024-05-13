import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def setup_webdriver():
    # Specify the path to ChromeDriver explicitly (adjust this path as per your setup)
    chrome_driver_path = '/path/to/chromedriver'  # Adjust this path
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Create a new instance of the Chrome driver
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def check_website_status():
    driver = setup_webdriver()
    url = 'https://dtm.iom.int/reports'
    driver.get(url)
    time.sleep(3)  # Allow time for the page to load
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
