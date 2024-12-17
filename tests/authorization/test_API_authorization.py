import os
import time
import allure
import requests
from dotenv import load_dotenv
from selene import browser
from utils.utils import response_logging, response_attaching

load_dotenv()
url = os.getenv('URL')
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')


@allure.label("owner", "aa.eliseev")
@allure.feature('Авторизация')
@allure.tag("Smoke")
@allure.title('Авторизация пользователя через API и проверка успешной авторизации в браузере')
def test_authorization_with_api(setup_browser):
    with allure.step('Авторизация через API'):

        data = {
            'AUTH_FORM': 'Y',
            'TYPE': 'AUTH',
            'backurl': '/personal/profile/index.php',
            'USER_LOGIN': login,
            'USER_PASSWORD': password
        }

        result = requests.post(
            url=url + '/personal/profile/index.php?login=yes',
            data=data,
            allow_redirects=False
        )
        response_logging(result)
        response_attaching(result)

        assert result.status_code == 200

    """ Все записываем с словарь, чтобы переиспользовать в дальнейшем """
    with allure.step('Получение авторизационных куки'):
        cookies = result.cookies.get_dict()

    """ Можно передать корректную куку для авторизации - способ ниже """
    # with allure.step('Подстановка авторизационных куки в браузер'):
    #     browser.open('/')
    #     browser.driver.add_cookie({'name': 'PHPSESSID', 'value': cookies['PHPSESSID'], 'domain': '.pitergsm.ru', 'path': '/'})
    #     browser.open("/")
    #     browser.open("/")
    #     time.sleep(2)

    """ Либо можно передать все куки в браузер полученные в ответ """
    with allure.step('Подстановка авторизационных куки в браузер'):
        browser.open('/')
        for name, value in cookies.items():
            browser.driver.add_cookie({'name': name, 'value': value, 'domain': '.pitergsm.ru', 'path': '/'})
        browser.open("/")
        time.sleep(2)