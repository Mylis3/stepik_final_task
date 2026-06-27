from .base_page import BasePage
from .locators_product import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_cart(self):
        self.should_be_add_to_cart_button()
        self.should_be_clickable_add_to_cart_button()

        button = self.browser.find_element(
            *ProductPageLocators.ADD_BASKET_BUTTON
        )
        button.click()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_BASKET_BUTTON
        ), "'Add to cart' button is not presented"

    def should_be_clickable_add_to_cart_button(self):
        button = self.browser.find_element(
            *ProductPageLocators.ADD_BASKET_BUTTON
        )
        assert button.is_enabled(), \
            "'Add to cart' button is disabled"

    def should_be_correct_book_name(self):
        cart_book_name = self.browser.find_element(
            *ProductPageLocators.CART_BOOK_NAME
        ).text
        book_name = self.browser.find_element(
            *ProductPageLocators.BOOK_NAME
        ).text

        assert book_name == cart_book_name, \
            "Incorrect book name in basket"

    def should_be_correct_book_price(self):
        cart_price = self.browser.find_element(
            *ProductPageLocators.CART_PRICE
        ).text
        book_price = self.browser.find_element(
            *ProductPageLocators.BOOK_PRICE
        ).text

        assert book_price == cart_price, \
            "Incorrect cart price"
