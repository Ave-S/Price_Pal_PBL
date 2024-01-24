#!/usr/bin/env python
# coding: utf-8

# In[14]:


pip install selenium


# In[15]:


pip install webdriver-manager


# In[3]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# Replace 'your_website_url' with the actual URL of the website you want to scrape
website_url = 'https://www.amazon.in/Huion-Inspiroy-Graphics-Battery-Free-Sensitivity/dp/B07R7L3HY7/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=eKxJN&content-id=amzn1.sym.cd312cd6-6969-4220-8ac7-6dc7c0447352%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=cd312cd6-6969-4220-8ac7-6dc7c0447352&pf_rd_r=A4SGA5JPZ8NZ5R2KRM0M&pd_rd_wg=NjqWX&pd_rd_r=bdbbf170-6850-4f8b-b1d0-f96ec61be264&pd_rd_i=B07R7L3HY7'

# Set up the Selenium WebDriver (make sure to download the appropriate driver for your browser)
# For Chrome, download chromedriver: https://sites.google.com/chromium.org/driver/
# For Firefox, download geckodriver: https://github.com/mozilla/geckodriver/releases
   # Change this to the path where your driver is located
service = Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the website
driver.get(website_url)
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
print(f"Scraped Numbers: {numbers_text}")


# In[ ]:




