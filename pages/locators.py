from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL_LINK = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_LINK = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON_LINK = (By.CSS_SELECTOR, "[name=login_submit]")

    REGISTRARTION_EMAIL_LINK = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRARTION_PASSWORD_LINK = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRARTION_REPEAT_PASSWORD_LINK = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRARTION_BUTTON_LINK = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ADD_TO_CART = (By.CSS_SELECTOR, 'div.alertinner > strong')
    BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRICE_IN_CART = (By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs')
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")