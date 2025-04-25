from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage, ProductPageLocators):

    def add_item(self):
        try:
            self.browser.implicitly_wait(5)
            button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
            button.click()
        except NoSuchElementException:
            print("Basket element not found")

        try:
            self.solve_quiz_and_get_code()
        except NoAlertPresentException:
            print("No alert appeared")

    def check_name_equality(self):
        name1 = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        name2 = self.browser.find_element(*ProductPageLocators.ITEM_BASKETNAME).text
        assert name1 == name2, 'Name is not the same'
        
    def check_price_equality(self):
        price1 = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        price2 = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE).text
        assert price1 == price2, 'Price is not the same'
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
            
    def should_dissapear_of_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"