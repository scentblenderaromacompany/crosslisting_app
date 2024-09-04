from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logging.basicConfig(level=logging.INFO, filename='offerup_automation.log')

def create_offerup_listing(listing):
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    try:
        driver.get('https://offerup.com/login/')

        # Log in
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        email_field.send_keys('your-email@example.com')
        password_field = driver.find_element_by_name('password')
        password_field.send_keys('yourpassword')
        password_field.send_keys(Keys.RETURN)

        logging.info('Logged in successfully.')

        # Navigate to post page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Post'))
        ).click()

        # Fill out the form fields
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

        # Select category, condition, etc.
        category_dropdown = driver.find_element_by_xpath('//select[@name="category"]')
        category_dropdown.send_keys(listing.category)

        condition_dropdown = driver.find_element_by_xpath('//select[@name="condition"]')
        condition_dropdown.send_keys(listing.condition)

        # Submit the listing
        submit_button = driver.find_element_by_xpath('//button[text()="Post"]')
        submit_button.click()

        logging.info('OfferUp listing created successfully.')

        time.sleep(5)
    except Exception as e:
        logging.error(f'Error during OfferUp listing creation: {e}')
    finally:
        driver.quit()
