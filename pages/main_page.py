from selene import browser, be, have, query


class MainPage:

    def open_page(self):
        browser.open('/')
        return self

    @staticmethod
    def get_menu_items():
        return [
            ('iPhone', 'iPhone'),
            ('iPad', 'iPad'),
            ('Mac', 'Mac'),
            ('Умные часы', 'Smart_Watches'),
            ('Аудио', 'Audio'),
            ('Смартфоны', 'Smartphones'),
            ('Электроника', 'Electronics'),
            ('Приставки и игры', 'Consoles_and_Games'),
            ('Техника для дома', 'Home_Appliances'),
            ('Гаджеты', 'Gadgets'),
            ('Телевизоры', 'TV'),
            ('Планшеты и ноутбуки', 'Tablets_and_Laptops'),
            ('Аксессуары', 'Accessories'),
            ('Сертификаты', 'Certificates')
        ]

    @staticmethod
    def menu_visible_menu_icon(value):
        menu_items = browser.all('.sh-menu__item')
        for item in menu_items:
            if item.get(query.text) == value:
                item.click()
                browser.element('.page-head__title').should(have.text(value))
                return
        raise AssertionError

    @staticmethod
    def assert_menu_item_count(count):
        menu_items = browser.all('.sh-menu__item')
        assert len(menu_items) == count


main_menu = MainPage()