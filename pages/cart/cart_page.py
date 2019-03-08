from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from helpers.data import data_search
class CartPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _cart_icon = "span[class='nav-cart-icon nav-sprite']"
    _item_in_cart = "//span[@class='a-size-medium sc-product-title a-text-bold' and contains(text(),"+"'"+data_search.string_search+"'"+ ")]"


    def click_cart(self):
        self.elementClick(self._cart_icon, locatorType="css")

    def verify_item_in_cart(self):
        result = self.isElementPresent(self._item_in_cart, locatorType="xpath")
        return result



