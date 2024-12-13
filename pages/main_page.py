from selene import browser, have, query, be


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
    def get_search_item_success():
        return [
            ('Macbook', 'Macbook_search'),
            ('Сертификат', 'Certificates_search'),
            ('Наушники', 'Headphones_search'),
            ('Xiaomi', 'Xiaomi_search'),
            ('Колонка', 'Smart_speaker_search'),
        ]

    @staticmethod
    def menu_item_click_and_title_validation(value):
        """ Метод для проверки работоспособности всех меню в хедере сайта """

        menu_items = browser.all('.sh-menu__item')
        for item in menu_items:
            if item.get(query.text) == value:
                item.click()
                browser.element('.page-head__title').should(have.text(value))
                return
        raise AssertionError(f'Пункт меню {value} отсутствует')

    @staticmethod
    def product_search_success(value: str):
        """ Метод для проверки поиска """

        browser.element('#smart-title-search-input').type(value).press_enter()
        element_text = browser.element('.prod-card__title')
        if value.lower() in element_text.get(query.text).lower():
            return
        else:
            raise AssertionError(f'Элемент {value} не найден')

    @staticmethod
    def product_search_failure(value):
        browser.element('#smart-title-search-input').type(value).press_enter()
        browser.element('.not-find-res').should(be.visible).should(have.text('К сожалению, на ваш поисковый запрос ничего не найдено.'))


main_menu = MainPage()