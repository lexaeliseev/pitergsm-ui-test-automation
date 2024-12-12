import os
from pages.authorization_page import authorization


def test_authorization():
    authorization.open_authorization_page()
    authorization.fill_login(os.getenv('LOGIN'))
    authorization.fill_password(os.getenv('PASSWORD'))
    authorization.click_submit()
    authorization.assert_success_authorization()