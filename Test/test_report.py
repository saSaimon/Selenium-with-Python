import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from pytest_html import HTMLReport


@pytest.fixture
def driver():
    # Set the path to the Microsoft Edge WebDriver executable
    driver_path = r'C:\WebDriver\msedgedriver.exe'
    service = Service(driver_path)
    # Set up a new instance of the Edge browser driver
    driver = webdriver.Edge(service=service)
    yield driver
    # Close the browser window after the test is complete
    driver.quit()


@pytest.mark.parametrize("search_term", ["pytest", "selenium", "python"])
def test_google_search(driver, search_term):
    # Write your test code here
    driver.get("https://www.google.com")
    assert driver.title == "Google"
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys(search_term)
    elem.submit()
    assert search_term in driver.title


if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])
