from pages.authorization_page import authorization


def test_authorization():
    authorization.open_authorization_page()
    authorization.fill_login('eliseevqa')
    authorization.fill_password('SpamSpamSpam')
    authorization.click_submit()
    authorization.assert_success_authorization()

    # browser.open('/')
    # browser.element('//a[@data-pop="pop-login" and contains(text(), "Вход / Регистрация")]').click()
    # browser.element('[name="USER_LOGIN"]').type('eliseevqa')
    # browser.element('[name="USER_PASSWORD"]').type('SpamSpamSpam')
    # browser.element('[name="Login"]').click()
    # browser.element('//a[@data-pop="pop-login" and contains(text(), "Личный кабинет")]').should(be.visible)
