import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service


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


def test_example(driver):
    # Write your test code here
    driver.get("https://www.google.com")
    assert driver.title == "Google"
