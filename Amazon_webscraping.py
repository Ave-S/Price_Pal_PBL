from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def search_amazon_selenium(query, num_results=10):
    driver = webdriver.Firefox()  # You may need to download the appropriate webdriver for your browser
    driver.get("https://www.amazon.in")

    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    results = []
    for index, result in enumerate(driver.find_elements(By.CSS_SELECTOR, 'div[data-asin]')[:num_results], start=1):
        title = result.find_element(By.CSS_SELECTOR, 'h2 span.a-text-normal')
        price = result.find_element(By.CSS_SELECTOR, 'span.a-offscreen')
        link = result.find_element(By.CSS_SELECTOR, 'h2 a[data-component-type="s-product-image"]').get_attribute("href")

        results.append({
            "index": index,
            "title": title.text.strip(),
            "price": price.text.strip(),
            "link": link
        })

    driver.quit()
    return results

if __name__ == "__main__":
    search_query = input("Enter your Amazon search query: ")
    search_results = search_amazon_selenium(search_query)

    if search_results:
        print("\nTop 10 Results:")
        for result in search_results:
            print(f"{result['index']}. {result['title']} - {result['price']} - {result['link']}")
    else:
        print("No results found.")
