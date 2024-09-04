from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logging.basicConfig(level=logging.INFO)

def create_facebook_listing(listing):
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    driver.get('https://www.facebook.com/marketplace/create/item/')

    # Log in securely
    try:
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        email_field.send_keys('your-email@example.com')
        password_field = driver.find_element_by_name('pass')
        password_field.send_keys('yourpassword')
        password_field.send_keys(Keys.RETURN)

        logging.info('Logged in successfully.')
    except Exception as e:
        logging.error(f"Login failed: {e}")
        driver.quit()
        return

    # Fill out the form fields
    try:
        title_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'title'))
        )
        title_field.send_keys(listing.title)

        description_field = driver.find_element_by_name('description')
        description_field.send_keys(listing.description)

        price_field = driver.find_element_by_name('price')
        price_field.send_keys(str(listing.price))

        # Upload image
        image_upload = driver.find_element_by_xpath('//input[@type="file"]')
        image_upload.send_keys(listing.image_url)

        # Submit the listing
        submit_button = driver.find_element_by_xpath('//button[text()="Post"]')
        submit_button.click()

        logging.info('Facebook listing created successfully.')

        time.sleep(5)
    except Exception as e:
        logging.error(f"Error creating Facebook listing: {e}")
    finally:
        driver.quit()
