import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.login import LoginPage

class TestNetlify:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    @pytest.mark.parametrize("username, password", [
        ("test", "test"),
    ])

    def test_login(self, driver, username, password):
        login_page = LoginPage(driver)
        login_page.open_page("https://trytestingthis.netlify.app/")
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_button()
        assert "Successful" in driver.page_source
