import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service


class MyTest(unittest.TestCase):

    def setUp(self):
        # Set the path to the Microsoft Edge WebDriver executable
        driver_path = r'C:\WebDriver\msedgedriver.exe'
        service= Service(driver_path)
        # Set up a new instance of the Edge browser driver
        self.driver = webdriver.Edge(service=service)

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

    def test_example(self):
        # Write your test code here
        self.driver.get("https://www.google.com")
        self.assertEqual(self.driver.title, "Google")


if __name__ == '__main__':
    unittest.main()
