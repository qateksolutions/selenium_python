from commandProviders.BrowserActions import BrowserActions
from commandProviders.ElementActions import ElementActions


class ActOn:
    @staticmethod
    def browser(driver):
        return BrowserActions(driver)

    @staticmethod
    def element(driver, locator):
        return ElementActions(driver, locator)