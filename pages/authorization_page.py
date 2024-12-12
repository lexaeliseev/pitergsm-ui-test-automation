from selene import browser, be


class AuthorizationPage:

    def open_authorization_page(self):
        browser.open('/')
        browser.element('//a[@data-pop="pop-login" and contains(text(), "Вход / Регистрация")]').click()
        return self

    def fill_login(self, login):
        browser.element('[name="USER_LOGIN"]').type(login)
        return self

    def fill_password(self, password):
        browser.element('[name="USER_PASSWORD"]').type(password)
        return self

    @staticmethod
    def click_submit():
        browser.element('[name="Login"]').click()

    @staticmethod
    def assert_success_authorization():
        browser.element('//a[@data-pop="pop-login" and contains(text(), "Личный кабинет")]').should(be.visible)


authorization = AuthorizationPage()