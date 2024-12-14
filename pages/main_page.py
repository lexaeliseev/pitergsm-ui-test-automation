import allure
from selene import browser, have, query, be


class MainPage:

    def open_page(self):
        with allure.step("Открыть браузер"):
            browser.open('/')
            return self

    @staticmethod
    def get_menu_items():
        with allure.step("Получить список пунктов меню"):
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
        with allure.step("Получить список значений для поиска"):
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
        with allure.step(f"Проверка наличие и корректный переход при клике на иконку меню = {value}"):
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
        with allure.step(f"Проверка успешного поиска по значению = {value}"):
            browser.element('#smart-title-search-input').type(value)
            browser.element('.sh-search__btn').click()
            first_element = browser.element('.prod-card__title')
            if value.lower() in first_element.get(query.text).lower():
                return
            else:
                raise AssertionError(f'Элемент {value} не найден')

    @staticmethod
    def product_search_failure(value):
        with allure.step("Проверка отображения системной ошибки при неуспешном поиске"):
            browser.element('#smart-title-search-input').type(value)
            browser.element('.sh-search__btn').click()
            browser.element('.not-find-res').should(be.visible).should(
                have.text('К сожалению, на ваш поисковый запрос ничего не найдено.'))


main_menu = MainPage()