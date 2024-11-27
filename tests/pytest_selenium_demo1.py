from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

class TestSelenium:
    @pytest.fixture()
    def driver(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(10)
        #teardown
        yield driver
        driver.quit()

    def test_google_search(self, driver):
        driver.get("https://www.google.com/")
        searchBox = driver.find_element(By.ID, "APjFqb")
        searchBox.send_keys("Automation")
        searchBox.send_keys(Keys.RETURN)
        time.sleep(2)
        print("Test Completed")