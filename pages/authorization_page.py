import allure
from selene import browser, be


class AuthorizationPage:

    def open_page(self):
        with allure.step("Открыть браузер"):
            browser.open('/')
            browser.element('//a[@data-pop="pop-login" and contains(text(), "Вход / Регистрация")]').click()
            return self

    def fill_login(self, login):
        with allure.step(f"Ввести значение в поле login = {login}"):
            browser.element('[name="USER_LOGIN"]').type(login)
            return self

    def fill_password(self, password):
        with allure.step(f"Ввести значение в поле login = {password}"):
            browser.element('[name="USER_PASSWORD"]').type(password)
            return self

    @staticmethod
    def click_submit():
        with allure.step('Нажать на кнопку Login'):
            browser.element('[name="Login"]').click()

    @staticmethod
    def assert_success_authorization():
        with allure.step('Проверка успешной авторизации на сайте'):
            browser.element('//a[@data-pop="pop-login" and contains(text(), "Личный кабинет")]').should(be.visible)


authorization = AuthorizationPage()