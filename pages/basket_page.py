from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import BasketPageLocators
import math
import time

class BasketPage(BasePage):
    #проверяем что в корзине нет товаров
    def should_be_no_element_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
       "There is something in the basket"

    #проверяем текст, что корзина пуста
    def should_be_message_empty_basket (self):
        assert self.is_element_present(*BasketPageLocators.BASKET_STATUS), \
       "Basket not empty"