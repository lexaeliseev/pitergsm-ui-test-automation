import pytest
from pages.main_page import main_menu


@pytest.mark.parametrize('value, id', main_menu.get_search_item_success(),
                         ids=[item[1] for item in main_menu.get_search_item_success()])
def test_search_success(value, id):
    main_menu.open_page()
    main_menu.product_search_success(value)

@pytest.mark.parametrize('value', ['неудачный поиск', 'мясо мясо мясо'],
                         ids=['invalid_search_term', 'irrelevant_search_term'])
def test_search_failure(value):
    main_menu.open_page()
    main_menu.product_search_failure(value)