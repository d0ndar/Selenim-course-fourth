from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"Ожидали увидеть ссылку с включением login"

    def should_be_login_form(self):
        assert (self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_LINK)
                and self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_LINK)),\
                f"Не смог найти поле пароля\email для входа"

    def should_be_register_form(self):
        assert (self.is_element_present(*LoginPageLocators.REGISTRARTION_EMAIL_LINK)
                and self.is_element_present(*LoginPageLocators.REGISTRARTION_PASSWORD_LINK)
                and self.is_element_present(*LoginPageLocators.REGISTRARTION_REPEAT_PASSWORD_LINK)),\
                f"Не смог найти поле пароля\email для регистрации"