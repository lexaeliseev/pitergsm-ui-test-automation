import pytest

from pages.main_page import main_menu


def test_menu_item_count():
    main_menu.open_page()
    main_menu.assert_menu_item_count(14)


@pytest.mark.parametrize('value, id', main_menu.get_menu_items(),
                         ids=[item[1] for item in main_menu.get_menu_items()])
def test_visible_menu_icon(value, id):
    main_menu.open_page()
    main_menu.menu_visible_menu_icon(value)