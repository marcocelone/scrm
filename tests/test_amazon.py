from pages.purchase.home_page import HomePage
from pages.product.result_page import ProductPage
from pages.cart.cart_page import CartPage
from helpers.data import data_search
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):

    # Setup
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.pp = ProductPage(self.driver)
        self.cp = CartPage(self.driver)

    # search item
    @pytest.mark.run(order=1)
    def test_search_product(self):
        self.hp.product_search(data_search.string_search)
        result = self.hp.verify_search()
        assert result == True

    # Item click verify page is product page
    @pytest.mark.run(order=2)
    def test_item_click(self):
        self.pp.product_click()
        result = self.pp.verify_item_page()
        assert result == True

    # Add item to cart and verify is added
    @pytest.mark.run(order=3)
    def test_add_item_to_cart(self):
        #time.sleep(2)
        verify_empty_cart = self.pp.verify_empty_cart()
        assert verify_empty_cart == True
        #time.sleep(5)
        self.pp.add_to_cart()
        #time.sleep(5)
        verify_items_is_added = self.pp.verify_add_item_cart()
        assert verify_items_is_added == True

    # Verify item in cart page
    @pytest.mark.run(order=4)
    def test_verify_cart_item(self):
        self.cp.click_cart()
        verify_items_in_cart = self.cp.verify_item_in_cart()
        assert verify_items_in_cart == True

    # Negative - Invalid item search
    @pytest.mark.run(order=5)
    def test_invalid_item_search(self):
        self.hp.product_search(data_search.invalid_search)
        no_result_found = self.hp.no_result_found()
        assert no_result_found == True
        no_result_check = self.hp.no_result_check()
        assert no_result_check == True









