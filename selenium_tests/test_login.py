from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def test_login_page():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    driver.get("http://webapp:5000/login")
    # Check if username input is present
    username_field = driver.find_element(By.NAME, "username")
    assert username_field is not None

    driver.quit()
