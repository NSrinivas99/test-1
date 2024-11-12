# test_app.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (make sure you have ChromeDriver installed)
driver = webdriver.Chrome()

try:
    # Open the Flask app
    driver.get("http://127.0.0.1:5000")

    # Wait for the metrics to load
    time.sleep(3)

    # Find MSE and R² elements and print their values
    mse_element = driver.find_element(By.ID, "mse")
    r2_element = driver.find_element(By.ID, "r2")

    print("Mean Squared Error (MSE):", mse_element.text)
    print("R² Score:", r2_element.text)

finally:
    # Close the WebDriver
    driver.quit()
