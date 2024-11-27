import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestNetlify:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    @pytest.mark.parametrize("username, password", [
        ("test", "test"),
        ("user2", "pass2"),
    ])

    def test_login(self, driver, username, password):
        driver.get("https://trytestingthis.netlify.app/")
        driver.find_element(By.ID, "uname").send_keys(username)
        driver.find_element(By.ID, "pwd").send_keys(password)
        driver.find_element(By.XPATH, "//input[@value='Login']").click()
        assert "Successful" in driver.page_source

