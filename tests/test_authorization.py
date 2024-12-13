import os
import allure
from pages.authorization_page import authorization


@allure.label("owner", "aa.eliseev")
@allure.feature('Авторизация')
@allure.tag("Smoke")
@allure.title('Успешная авторизация на сайте')
def test_authorization():
    authorization.open_page()
    authorization.fill_login(os.getenv('LOGIN'))
    authorization.fill_password(os.getenv('PASSWORD'))
    authorization.click_submit()
    authorization.assert_success_authorization()