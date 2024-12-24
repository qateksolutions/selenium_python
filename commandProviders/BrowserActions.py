import logging

logger = logging.getLogger("Browser")

class BrowserActions:
    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, url):
        self.driver.delete_all_cookies()
        self.driver.get(url)
        logger.info("Navigating to: " + url)
        self.driver.maximize_window()

    def close_browser(self):
        self.driver.quit()



