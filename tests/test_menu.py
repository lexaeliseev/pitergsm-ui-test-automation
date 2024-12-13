import allure
import pytest
from pages.main_page import main_menu


@allure.label("owner", "aa.eliseev")
@allure.feature('Меню сайта')
@allure.tag("Smoke")
@pytest.mark.parametrize(
    'value, ids',
    main_menu.get_menu_items(),
    ids=[item[1] for item in main_menu.get_menu_items()]
)
def test_menu_item_click_and_title_validation(value, ids):
    allure.dynamic.title(f'Проверка клика на пункт меню и валидация заголовка при значении {value}')
    main_menu.open_page()
    main_menu.menu_item_click_and_title_validation(value)