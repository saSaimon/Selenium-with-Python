from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Set the path to the Microsoft Edge WebDriver executable
from selenium.webdriver.common.by import By

driver_path = r'C:\WebDriver\msedgedriver.exe'
service = Service(driver_path)

# Create a new instance of the Edge browser
driver = webdriver.Edge(service=service)

# Navigate to a website
driver.get('https://www.google.com')

# Find an element by name and type a search query
search_box = driver.find_element(By.CSS_SELECTOR,'[class="gLFyf"]')
search_box.send_keys('Selenium')

# Submit the search query by pressing Enter
search_box.submit()

# Wait for the search results to load
driver.implicitly_wait(10)

# Print the page title and URL of the first search result
first_result = driver.find_element(By.CSS_SELECTOR,'[class="yuRUbf"]')
print('Title:', first_result.get_attribute('title'))
print('URL:', first_result.get_attribute('href'))

# Close the browser window
driver.quit()
