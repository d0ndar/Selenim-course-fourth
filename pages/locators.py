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