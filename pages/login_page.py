from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in browser.current_url, "Login url is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.EMAIL_FORM)
        password_form = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        confirm_password_form = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FORM)
        email_form.send_keys(email)
        password_form.send_keys(password)
        confirm_password_form.send_keys(password)
        button_redister = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button_redister.click()