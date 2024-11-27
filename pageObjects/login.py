from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger("LoginPage")

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "uname")
        self.password_textbox = (By.ID, "pwd")
        self.login_button = (By.XPATH, "//input[@value='Login']")

    def open_page(self, url):
        self.driver.get(url)
        logger.debug("Open the page: " + url)


    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)
        logger.debug("Entered username: " + username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)
        logger.debug("Entered password: " + password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()
        logger.debug("Clicked on the Login button")
