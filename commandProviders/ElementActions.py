from selenium.common import NoSuchElementException

class ElementActions:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def get_element(self):
        self.driver.implicitly_wait(10)
        try:
            return self.driver.find_element(str(self.locator[0]), str(self.locator[1]))
        except NoSuchElementException:
            raise Exception("No element found for the locator: " + self.locator)

    def click(self):
        self.get_element().click()

    def type_data(self, value):
        self.get_element().clear()
        self.get_element().send_keys(value)