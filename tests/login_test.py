import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from commandProviders.ActOn import ActOn
from pageObjects.login import LoginPage

class TestNetlify:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        yield driver
        driver.quit()

    @pytest.mark.parametrize("username, password", [
        ("test", "test"),
    ])

    def test_login(self, driver, username, password):
        ActOn.browser(driver).open_browser("https://trytestingthis.netlify.app/")
        login_page = LoginPage(driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_button()
        assert "Successful" in driver.page_source
