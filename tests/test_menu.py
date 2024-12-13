import pytest
from pages.main_page import main_menu


@pytest.mark.parametrize('value, id', main_menu.get_menu_items(),
                         ids=[item[1] for item in main_menu.get_menu_items()])
def test_menu_item_click_and_title_validation(value, id):
    main_menu.open_page()
    main_menu.menu_item_click_and_title_validation(value)