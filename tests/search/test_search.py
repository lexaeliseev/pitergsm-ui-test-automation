import allure
import pytest

from pages.main_page import main_menu


@allure.label("owner", "aa.eliseev")
@allure.feature('Поиск')
@allure.tag("Smoke")
@pytest.mark.parametrize(
    'value',
    [item[0] for item in main_menu.get_search_item_success()],
    ids=[item[1] for item in main_menu.get_search_item_success()]
)
def test_search_success(value):
    allure.dynamic.title(f'Проверка успешного поиска на сайте при вводе: {value}')
    main_menu.open_page()
    main_menu.product_search_success(value)


@allure.label("owner", "aa.eliseev")
@allure.feature('Поиск')
@allure.tag("Smoke")
@pytest.mark.parametrize(
    'value',
    ['неудачный поиск', 'testtesttest'],
    ids=['invalid_search_term', 'irrelevant_search_term']
)
def test_search_failure(value):
    allure.dynamic.title(f'Проверка неудачного поиска на сайте при вводе: {value}')
    main_menu.open_page()
    main_menu.product_search_failure(value)
