from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from helpers.data import data_search
class ProductPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _product = "img[alt="+"'"+data_search.string_search+"'"+"]"
    _one_time_purchase = "//span[@class='modeTitle a-text-bold' and contains(text(), 'One-time Purchase')]"
    _one_time_purchase_radio_button = "(//i[@class='a-icon a-icon-radio'])[2]"
    _one_time_option = "//*[@id='onetimeOption']/label/i"
    _add_to_cart_button = "input[id='add-to-cart-button']"
    _cart_count_0 ="//span[@id='nav-cart-count' and contains(text(),'0')]"
    _cart_count_1 ="//span[@id='nav-cart-count' and contains(text(),'1')]"


    def click_item(self):
        self.elementClick(self._product, locatorType="css")

    def click_onetime_radio_button(self):
        self.elementClick(self._one_time_purchase, locatorType="xpath")

    def click_add_to_cart(self):
        self.elementClick(self._add_to_cart_button, locatorType="css")

    def product_click(self):
        self.click_item()

    def add_to_cart(self):
        self.click_onetime_radio_button()
        self.click_add_to_cart()

    def verify_item_page(self):
        result = self.isElementPresent(self._product, locatorType="css")
        return result

    def verify_empty_cart(self):
        result = self.isElementPresent(self._cart_count_0, locatorType="xpath")
        return result

    def verify_add_item_cart(self):
        result = self.isElementPresent(self._cart_count_1, locatorType="xpath")
        return result


