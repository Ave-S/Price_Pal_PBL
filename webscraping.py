from selenium import webdriver
from selenium.webdriver.common.by import By

# Replace 'your_website_url' with the actual URL of the website you want to scrape
website_url = 'https://www.amazon.in/Huion-Inspiroy-Graphics-Battery-Free-Sensitivity/dp/B07R7L3HY7/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=eKxJN&content-id=amzn1.sym.cd312cd6-6969-4220-8ac7-6dc7c0447352%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=cd312cd6-6969-4220-8ac7-6dc7c0447352&pf_rd_r=A4SGA5JPZ8NZ5R2KRM0M&pd_rd_wg=NjqWX&pd_rd_r=bdbbf170-6850-4f8b-b1d0-f96ec61be264&pd_rd_i=B07R7L3HY7'

# Set up the Selenium WebDriver (make sure to download the appropriate driver for your browser)
# For Chrome, download chromedriver: https://sites.google.com/chromium.org/driver/
# For Firefox, download geckodriver: https://github.com/mozilla/geckodriver/releases
driver_path = '/path/to/chromedriver'  # Change this to the path where your driver is located
driver = webdriver.Chrome(executable_path=driver_path)

# Open the website
driver.get(website_url)

# Locate the element containing the numbers using its XPath or other attributes
# Replace 'your_xpath' with the actual XPath of the element you want to scrape
element_xpath = '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]'
number_element = driver.find_element(By.XPATH, element_xpath)

# Extract the text from the element
numbers_text = number_element.text

# Close the browser window
driver.quit()

# Print the scraped numbers
print(f"Scraped Numbers: {numbers_text}")
