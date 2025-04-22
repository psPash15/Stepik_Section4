import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage
from .pages.base_page import BasePage


#initial_url = ProductPageLocators.PRODUCT_URL
#urls = [f"{initial_url}/?promo=offer{i}" for i in range(10)]

@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_item()
    page.check_name_equality()
    page.check_price_equality()
