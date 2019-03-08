from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from helpers.data import data_search
class HomePage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_item = "twotabsearchtextbox"
    _search_button = "input[value='Go']"
    _product = "img[alt="+"'"+data_search.string_search+"'"+"]"
    _no_result_item = "//span[@class='a-size-medium a-color-base' and contains(text()," +"'"+\
                       data_search.invalid_search+"'"+")]"
    _no_result_found = "//span[@class='a-size-medium a-color-base' and contains(text(), 'No results for ')]"


    def search_item(self, search_item):
        self.sendKeys(search_item, self._search_item, locatorType='id')

    def click_search_button(self):
        self.elementClick(self._search_button, locatorType="css")

    def clear_text_area(self):
        self.clearFIeld(self._search_item, locatorType="id")

    def product_search(self, product_search):
        self.clear_text_area()
        self.search_item(product_search)
        self.click_search_button()

    def verify_search(self):
        result = self.isElementPresent(self._product, locatorType="css")
        return result

    def no_result_check(self):
        result = self.isElementPresent(self._no_result_item, locatorType="xpath")
        return result

    def no_result_found(self):
        result = self.isElementPresent(self._no_result_found, locatorType="xpath")
        return result
