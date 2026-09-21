from .base_page import BasePage
# from .locators import MainPageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # Позитивная проверка: Ожидаем, что есть текст о том что корзина пуста
    def should_be_empty_basket_message(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_TEXT
        ), "'Basket is empty'"

# Отрицательная проверка: Ожидаем, что в корзине нет товаров (найти селектор товара в корзине и убедиться что его нет на странице)
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_WITH_ITEMS), \
            "Item in the basket is presented, but should not be"
