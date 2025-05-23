from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REPEAT_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    REGISTER_SUCCESS_BOX = (By.CSS_SELECTOR,".icon-ok-sign")
    LOG_OUT_BUTTON = (By.CSS_SELECTOR, "#logout_link")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ITEM_BASKETNAME = (By.CSS_SELECTOR, '.fade.in .alertinner strong')
    ITEM_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    TOTAL_PRICE = (By.CSS_SELECTOR, '.fade.in .alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.fade.in .alertinner strong')
    
class BasePageLocators ():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
        
class BasketPageLocators():
    BASKET_STATUS = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "#content_inner .basket-title.hidden-xs .row")
