from selenium.webdriver.common.by import By
import logging
from commandProviders.ActOn import ActOn

username_textbox = (By.ID, "uname")
password_textbox = (By.ID, "pwd")
login_button = (By.XPATH, "//input[@value='Login']")

logger = logging.getLogger("LoginPage")

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        ActOn.element(self.driver, username_textbox).type_data(username)
        logger.info("Entered username: " + username)

    def enter_password(self, password):
        ActOn.element(self.driver, password_textbox).type_data(password)
        logger.info("Entered password: " + password)

    def click_login_button(self):
        ActOn.element(self.driver, login_button).click()
        logger.info("Clicked on the Login button")
