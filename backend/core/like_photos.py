from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import logging

logger = logging.getLogger(__name__)

def like_photos(username, password):
    logger.info("Starting Selenium script")  # Log script start
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(2)

    try:
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')

        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        time.sleep(4)

        logger.info("Logged in successfully")  # Log successful login

        # Logic to search for users with <500 followers and >1000 following
        # Example: search using hashtags or explore page

        # After finding such users, like their photos
        # Example placeholder logic:
        driver.get('https://www.instagram.com/explore/tags/somehashtag/')
        time.sleep(2)

        posts = driver.find_elements(By.CLASS_NAME, 'v1Nh3')
        for post in posts:
            post.click()
            time.sleep(2)
            like_button = driver.find_element(By.XPATH, "//span[@aria-label='Like']")
            like_button.click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
            time.sleep(1)

        result = "Liked photos successfully"
    except Exception as e:
        logger.error(f"An error occurred: {e}")  # Log any error
        result = str(e)
    finally:
        driver.quit()
    
    logger.info("Finished Selenium script")  # Log script end
    return result
