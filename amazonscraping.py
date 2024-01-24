from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from webdriver.manager.chrome import ChromeDriverManager
import time
import random


# Set up the Selenium WebDriver (make sure to download the appropriate driver for your browser)
# For Chrome, download chromedriver: https://sites.google.com/chromium.org/driver/
# For Firefox, download geckodriver: https://github.com/mozilla/geckodriver/releases
   # Change this to the path where your driver is located
service = Service(executable_path='./chromedriver.exe')
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox()

driver.get("https://www.amazon.in/")

# Find the search input field and enter your search query
search_box = driver.find_element(By.CSS_SELECTOR,'#twotabsearchtextbox')
search_query = input("Enter product name: ")  # Replace with the product you want to search
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(2)  # You might need to adjust the wait time based on your internet speed

# Find the first search result and get its URL
try:
    first_result = driver.find_element(By.CSS_SELECTOR,'.widgetId\=search-results_3 > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h2:nth-child(2) > a:nth-child(1)')
    product_url = first_result.get_attribute("href")
except Exception as e:
    print("Error:", e)


# Open the website
driver.get(product_url)
delay_between_requests = 3
#random.uniform(4, 6)
time.sleep(delay_between_requests)
# Locate the element containing the numbers using its XPath or other attributes
# Replace 'your_xpath' with the actual XPath of the element you want to scrape
element_xpath = '/html/body/div[2]/div/div[5]/div[3]/div[4]/div[13]/div/div/div[4]/div[1]/span[3]/span[2]/span[2]'
number_element = driver.find_element(By.XPATH, element_xpath)

# Extract the text from the element
numbers_text = number_element.text

# Close the browser window
driver.quit()

# Print the scraped numbers
print(f"Price: ₹ {numbers_text}")




